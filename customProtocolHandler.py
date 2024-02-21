import sys
import os
from urllib.parse import urlparse, parse_qs
import subprocess
from win32com.client import Dispatch
import configparser
from plyer import notification


def bring_window_to_front(window_title):
    import pygetwindow as gw
    window = gw.getWindowsWithTitle(window_title)
    if window:
        window[0].activate()


def process_custom_protocol(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    query_string = parsed_url.query
    parsed_params = parse_qs(query_string)
    file_path = parsed_params.get("file", [""])[0].replace('\\', '/')

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
        else:
            subprocess.run(['start', '""', '/wait', file_path], shell=True)

if __name__ == "__main__":
    url = sys.argv[1]
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.conf'))
    config = configparser.ConfigParser()
    config.read(config_path)
    try:
        process_custom_protocol(url)
    except Exception as e:
        notification.notify(title="Error", message=str(e), timeout=5)