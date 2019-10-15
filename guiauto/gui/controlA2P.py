from guiauto.gui.base_test import BaseTest
from guiauto.util.guiutils import guiHelper
from .controlTypes import ControlType
from guiautomation import guiautomation as gauto
import pyautogui

class ButtonControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

    def get_control_list_name(self, elementx, wintitle=None, cp=None):
        if wintitle:geln = self.guihelper.control_element_details(gauto.ButtonControl, wintitle=wintitle)
        else:geln = self.guihelper.control_element_details(gauto.ButtonControl)
        if not cp:return self.guihelper.get_locator_element(elementx, geln[0])
        else:return self.guihelper.get_cp_locator_element(elementx, geln[0])

    def click_action_button(self, elementx, wintitle=None):
        getcontrolList = self.get_control_list_name(elementx, wintitle=wintitle)
        buttonClick = self.guihelper.find_gui_element(getcontrolList[0], getcontrolList[1])
        buttonClick.click()

    def clickable_action_Points(self, elementx):
        getcontrolList = self.get_control_list_name(elementx, cp='Y')
        pyautogui.click(getcontrolList[0], getcontrolList[1])

    def click_open_button(self, wintitle, elementx):
        mmcwin = self.guihelper.window_opened_by_name(winName=wintitle)
        geln = self.get_control_list_name(elementx)
        getlnID='1'
        result = self.guihelper.find_window_gui_element(ControlType.Button, mmcwin, geln[0], getlnID)
        if result[1] == True:result[0].Click()
        else:print('control not found')

class MenuItemControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

    def get_control_list_name(self, elementx, cp=None, wintitle=None):
        if wintitle:geln = self.guihelper.control_element_details(gauto.MenuItemControl, wintitle=wintitle)
        else:geln = self.guihelper.control_element_details(gauto.MenuItemControl)
        if not cp:return self.guihelper.get_locator_element(elementx, geln[0])
        else:return self.guihelper.get_cp_locator_element(elementx, geln[0])

    def click_action_button(self, elementx, wintitle=None):
        getcontrolList = self.get_control_list_name(elementx, wintitle=wintitle)
        getclicked=self.guihelper.find_gui_element(getcontrolList[0], getcontrolList[1])
        getclicked.click()

    def clickable_action_Points(self, elementx):
        getcontrolList = self.get_control_list_name(elementx, cp='Y')
        pyautogui.click(getcontrolList[0], getcontrolList[1])

    def click_gui_action(self, elementx):
        geln = self.guihelper.control_element_details(gauto.MenuItemControl)
        getId = self.guihelper.get_locator_element(elementx, geln[0])
        result =self.guihelper.find_window_gui_element(geln[1], getId[0], getId[1])
        if result[1] == True:result[0].Click()
        else:print('control not found')

class EditControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

    def get_control_list_name(self, elementx, cp=None, wintitle=None):
        if wintitle:geln = self.guihelper.control_element_details(gauto.EditControl, wintitle=wintitle)
        else:geln = self.guihelper.control_element_details(gauto.EditControl)
        if not cp:return self.guihelper.get_locator_element(elementx, geln[0])
        else:return self.guihelper.get_cp_locator_element(elementx, geln[0])

    def type_send_keys(self, elementx, value):
        getcontrolListxx = self.get_control_list_name(elementx)
        typeKey = self.guihelper.find_gui_element(getcontrolListxx[0], getcontrolListxx[1])
        typeKey.send_keys(value)

    def type_send_keys_fileopen_dialog(self, value, fName, wintitle):
        getcontrolListxx = self.get_control_list_name(fName, wintitle=wintitle)
        typeKey = self.guihelper.find_gui_element(getcontrolListxx[0], getcontrolListxx[1])
        typeKey.send_keys(value)

    def type_send_keys_autogui(self, txtvalue):
        pyautogui.typewrite(txtvalue)

    def clickable_action_Points(self, elementx):
        getcontrolList = self.get_control_list_name(elementx, cp='Y')
        pyautogui.click(getcontrolList[0], getcontrolList[1])

    def type_send_keys_gui_action(self, value, elementx, elementx1):
        mmcwin = self.guihelper.window_opened_by_name(winName=elementx)
        geln = self.get_control_list_name(elementx1)
        result = self.guihelper.find_window_gui_element(ControlType.Edit, mmcwin, geln[0], geln[1])
        if result[1] == True:result[0].SendKeys(value)
        else:print('control not found')

class GroupControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle= self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

    def get_group_childrens(self, elementx):
        get_window_details = geln = self.guihelper.control_element_details(gauto.GroupControl)
        gridLista = get_window_details[1].GroupControl(Name=elementx)
        lista = gridLista.GetChildren()
        listx = []
        for xlist in lista:
            listx.append(xlist.Name)
        return listx

class PaneControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle= self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

    def get_current_pane_children_details(self, elementx):
        get_window_details = self.guihelper.control_element_details(gauto.PaneControl)
        return self.get_childrens(get_window_details[1], elementx)

    def get_childrens(self, mmcwindow, elementx):
        gridLista = mmcwindow.PaneControl(AutomationId=elementx)
        lista = gridLista.GetChildren()
        listx = []
        for xlist in lista:
            listx.append(xlist.Name)
        return listx

class AppBarControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class CalendarControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class CheckBoxControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class ComboBoxControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class CustomControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class DataGridControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class DataItemControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class DocumentControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class HeaderControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class HeaderItemControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class HyperlinkControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class ImageControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class ListControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class ListItemControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class MenuBarControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class MenuControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)

class ProgressBarControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__()
        self.guihelper = guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title = self.guihelper.window_title_exists(winHandle)