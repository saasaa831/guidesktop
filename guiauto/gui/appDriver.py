import platform, os, time
from appium import webdriver
from .driverStart import appdriver_starts, appdriver_stops
from guiauto.util import archive, guiutils
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))



class BrowserDriver(object):

    def __init__(self, browser):
        """
            BrowserDriver: Initialize an automated test browser driver
            :type name: str
            :type dc: dict
            """
        self.hostos = platform.system().lower()
        self.platform_detect = platform.machine()
        self.runnerApp()
        desired_caps = {}
        desired_caps["app"] = guiutils.getappPath(browser)
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', desired_capabilities=desired_caps)
        time.sleep(2)

    def runnerApp(self):
        base_path = os.path.join(ROOT_DIR, "driverapp", 'guidriver.zip')
        folder = os.path.join(os.path.expanduser("~"), ".wdm")
        appdriver_stops()
        archive.unpack(base_path, folder)
        appdriver_starts()



