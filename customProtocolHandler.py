import sys
import os
from urllib.parse import urlparse, parse_qs
import subprocess
from win32com.client import Dispatch
import configparser
from plyer import notification

def convert_to_os_path(string: str):
    converted_path = string.replace('/', os.path.sep).replace('\\', os.path.sep)
    return converted_path

def bring_window_to_front(window_title):
    import pygetwindow as gw
    window = gw.getWindowsWithTitle(window_title)
    if window:
        window[0].activate()


def message(e):
    try:
        notification.notify(title="Error", message=str(e), timeout=5)
    except NotImplementedError:
        with open('error.log', 'w') as f:
            f.write(str(e))

def process_custom_protocol(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    query_string = parsed_url.query
    parsed_params = parse_qs(query_string)
    folder_path: str = convert_to_os_path(parsed_params.get("folder", [""])[0])
    file_path: str = convert_to_os_path(parsed_params.get("file", [""])[0])

    if hostname == 'open':
        app = parsed_params.get("app", [""])[0]
        
        if app == 'potplayer':
            subprocess.run(f'"{config.get("Path", "potplayer")}" "{file_path}" /seek={parsed_params["seek"][0]}')
        elif app == 'foxit':
            subprocess.run(f'"{config.get("Path", "foxit")}" "{file_path}" /A page={parsed_params["page"][0]}')
        elif app == 'PPT':
            ppt = Dispatch('PowerPoint.Application')
            ppt.Visible = True
            presentation = ppt.Presentations.Open(file_path)
            page_num = parsed_params.get("page", [""])[0]
            slide = presentation.Slides(int(page_num))
            slide.Select()
            bring_window_to_front("PowerPoint")
        elif app == 'code':
            subprocess.run(f'code -n "{folder_path}"', shell=True)
            subprocess.run(f'code -r -g "{file_path}":{parsed_params["line"][0]}', shell=True)
        else:
            subprocess.run(f'start "" /wait "{file_path}"', shell=True)

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.conf'))
        config = configparser.ConfigParser()
        config.read(config_path)
        process_custom_protocol(url)
    except Exception as e:
        print(e)
        message(e)
        