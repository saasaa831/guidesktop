import os, sys, logging, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from guiautomation import guiautomation as gauto
from guiauto.gui.base_test import BaseTest
logger = logging.getLogger(__name__)

def getListOfFiles(dirName):
    try:
        listOfFile = os.listdir(dirName)
        allFiles = list()
        for entry in listOfFile:
            fullPath = os.path.join(dirName, entry)
            if os.path.isdir(fullPath):
                allFiles = allFiles + getListOfFiles(fullPath)
            else:
                allFiles.append(fullPath)
        return allFiles
    except PermissionError as p:pass
    except TypeError as t:pass

def getappPath(olookApp):
    pFiles = ['ProgramFiles', 'ProgramFiles(x86)']
    elem=None
    for xprog in pFiles:
        try:
            dirName = os.environ[xprog]
            listOfFiles = getListOfFiles(dirName)
            for elem in listOfFiles:
                if olookApp in elem:
                    elem=elem
                    break
            return elem
        except TypeError as t:pass

class guiHelper(BaseTest):
    parent_handle = None
    driver = None

    def __init__(self, driver, parent_handle):
        super(guiHelper, self).__init__(driver, parent_handle)
        self.parent_handle = parent_handle

    def window_handle_title(self):
        time.sleep(1)
        self.handles = self.driver.window_handles
        size = len(self.handles)
        #logger.info('winSize:'+str(size))
        if len(self.handles) <= 1:
            self.driver.switch_to.window(self.parent_handle)
            #logger.info('Handle-x1:' + str(self.driver.title))
        else:
            for x in range(size):
                if self.handles[x] != self.parent_handle:
                    self.driver.switch_to.window(self.handles[x])
                    #logger.info('Handle-x2:' + str(self.driver.title))
                break
        return self.driver.title

    def window_title_exists(self, title):
        self.handles = self.driver.window_handles
        size = len(self.handles)
        if len(self.handles) <= 1:
            self.driver.switch_to.window(self.parent_handle)
            #logger.info('Handle-x1:' + str(self.driver.title))
            return self.driver.title
        else: return title

    def getWin_control(self, regex, cotn):
        global controldetails
        mmcWindow = gauto.WindowControl(Name=regex)
        try:
            mmcWindow.SetActive(waitTime=1)
            details=[]
            for control, depth in gauto.WalkControl(mmcWindow):
                if isinstance(control, cotn):
                    controldetails = {'Name':control.Name, 'LocalizedControlType':control.LocalizedControlType,
                                      'AutomationId': control.AutomationId, 'ClassName':control.ClassName,
                                      'ClickablePoint':control.GetClickablePoint()}
                    details.append(controldetails)
            return details, mmcWindow
        except LookupError as ex:
            gauto.EnumAndLogControl(gauto.GetRootControl(), maxDepth=1)

    def window_opened_by_name(self, winName):
        return gauto.WindowControl(Name=winName)

    def control_element_details(self, gcontrol, wintitle=None):
        if wintitle:return self.getWin_control(wintitle, gcontrol)
        else:return self.getWin_control(self.window_handle_title(), gcontrol)

    def get_locator_details(self, elementx, get_control):
            global getbtn
            for xname in get_control:
                if xname['Name'] == elementx or xname['AutomationId'] == elementx:
                    getbtn = {
                              'Name':xname['Name'],
                              'AutomationId':xname['AutomationId'],
                              'ClickablePoint':xname['ClickablePoint'],
                              'LocalizedControlType': xname['LocalizedControlType'],
                              'ClassName': xname['ClassName'],
                              }
                    break
            return getbtn

    def get_locator_element(self, elementx, getcontrol):
        editdetails = self.get_locator_details(elementx, getcontrol)
        if editdetails['AutomationId']:return 'id', editdetails['AutomationId']
        elif editdetails['Name']:return 'name', editdetails['Name']
        elif editdetails['LocalizedControlType']:return 'tagname', editdetails['LocalizedControlType']
        else:return 'classname', editdetails['ClassName']

    def get_cp_locator_element(self, elementx, getcontrol):
        editdetails = self.get_locator_details(elementx, getcontrol)
        #logger.info(editdetails['ClickablePoint'])
        return editdetails['ClickablePoint']

    def find_gui_element(self, locator, element):
        if locator == 'name':
            return self.driver.find_element_by_name(element)
        elif locator == 'classname':
            return self.driver.find_element_by_class_name(element)
        elif locator =='tagname':
            return self.driver.find_element_by_tag_name(element)
        else:
            return self.driver.find_element_by_accessibility_id(element)

    def find_gui_elements(self, locator, element):
        if locator == 'name':
            return self.driver.find_elements_by_name(element)
        elif locator == 'classname':
            return self.driver.find_elements_by_class_name(element)
        elif locator == 'tagname':
            return self.driver.find_elements_by_tag_name(element)
        else:
            return self.driver.find_elements_by_accessibility_id(element)


    def find_window_gui_element(self, cTypex, mmcwindow, locator, element):
        if locator == 'id':
            menuitem = cTypex(searchFromControl=mmcwindow, AutomationId=element)
        elif locator == 'name':
            menuitem = cTypex(searchFromControl=mmcwindow, Name=element)
        elif locator == 'tagname':
            menuitem = cTypex(searchFromControl=mmcwindow, TagName=element)
        else:
            menuitem = cTypex(searchFromControl=mmcwindow, ClassName=element)
        result = gauto.WaitForExist(menuitem, 30)
        return menuitem, result