#!python3
# -*- coding: utf-8 -*-
import os, sys, time, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # not required after 'pip install uiautomation'
from guiautomation import guiautomation as gauto
from guiautomation.guidriver import drivergui
logger = logging.getLogger(__name__)

def appdriver_starts():
    folder = os.path.join(os.path.expanduser("~"), ".wdm", "guidriver")
    appdriver = 'WinAppDriver.exe'
    """for other language"""
    thisWindow = gauto.GetConsoleWindow()
    cmdWindow = gauto.WindowControl(SubName='cmd.exe')
    time.sleep(1)
    gauto.SendKeys('{Win}r')
    while not isinstance(gauto.GetFocusedControl(), gauto.EditControl):
        time.sleep(1)
    gauto.SendKeys('cmd{Enter}')
    time.sleep(1)
    rect = cmdWindow.BoundingRectangle
    gauto.DragDrop(rect.left + 50, rect.top + 10, 50, 10)
    thisWindow.SetActive(waitTime=1)
    scriptPath = folder
    cmdWindow.SendKeys('cd "{}"'.format(scriptPath) + '{Enter}', 0.05)
    cmdWindow.SendKeys('{}'.format(appdriver) + '{Enter}', 0.05)
    cmdWindow.SetActive(waitTime = 1)

def appdriver_stops():
    try:
        drivergui.stop_server()
        thisWindow = gauto.GetConsoleWindow()
        thisWindow.SetActive(waitTime=1)
        cmdWindow = gauto.WindowControl(SubName='cmd.exe')
        xcloseBtn = cmdWindow.ButtonControl(Name='Close')
        #logger.info('XX:'+str(xcloseBtn))
        cmdWindow.SetActive(waitTime=1)
        xcloseBtn.Click()
    except Exception as e:
        logger.info(str(e))

def sdownProcess(brows):
    os.system("taskkill /f /im " + str(brows))

if __name__ == '__main__':
    appdriver_starts()
    time.sleep(2)
    appdriver_stops()
