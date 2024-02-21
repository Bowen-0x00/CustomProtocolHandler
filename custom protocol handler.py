import sys
from urllib.parse import urlparse, parse_qs
import subprocess
from win32com.client import Dispatch
import pygetwindow as gw
import configparser
# import time
from os.path import dirname, join, abspath

current_dir = dirname(abspath(__file__))
parent_dir = dirname(current_dir)
config_path = join(parent_dir, 'config.conf')
config = configparser.ConfigParser()
config.read(config_path)

def bring_window_to_front(window_title):
    window = gw.getWindowsWithTitle(window_title)
    if len(window) > 0:
        window[0].activate()

# print(sys.argv)
parsed_url = urlparse(sys.argv[1])
hostname = parsed_url.hostname
query_string = parsed_url.query
parsed_params = parse_qs(query_string)
file = parsed_params["file"][0].replace('\\', '/')

app = ''
try:
    if "app" in parsed_params:
        app = parsed_params["app"][0]
    if hostname == 'open':
        if app == 'potplayer':
            subprocess.run(f'"{config.get("Path", "potplayer")}" "{file}" /seek={parsed_params["seek"][0]}')
        elif app == 'foxit':
            subprocess.run(f'"{config.get("Path", "foxit")}" "{file}" /A page={parsed_params["page"][0]}')
        elif app == 'PPT':
            ppt = Dispatch('PowerPoint.Application')  
            ppt.Visible = True 
            # ppt.DisplayAlerts = True
            presentation = ppt.Presentations.Open(file)
            page_num = parsed_params["page"][0]
            slide = presentation.Slides(int(page_num))
            slide.Select()
            
            bring_window_to_front("PowerPoint")
            # presentation.slides(page_num).select() 
            # slide.SlideShowTransition.AdvanceOnClick = True
            # slide.SlideShowPage()
            # ppt.Quit()
            # subprocess.run(f'"{config_path["PPT"]}" "{file}" /A page={parsed_params["page"][0]}')
        else:
            subprocess.run(f'start " " /wait "{file}"', shell=True)
except Exception as e:
    print(e)
    # time.sleep(3)
    