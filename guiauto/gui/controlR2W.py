from guiauto.gui.base_test import BaseTest
from guiauto.util.guiutils import guiHelper
from guiautomation import guiautomation as gauto
import logging
logger = logging.getLogger(__name__)


class TextControl(BaseTest):
    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

    def get_control_list_name(self, elementx, cp=None, wintitle=None):
        if wintitle:geln = self.guihelper.control_element_details(gauto.TextControl, wintitle=wintitle)
        else:geln = self.guihelper.control_element_details(gauto.TextControl)
        if not cp:return self.guihelper.get_locator_element(elementx, geln[0])
        else:return self.guihelper.get_cp_locator_element(elementx, geln[0])

    def getText(self, elementx):
        logger.info('Get Text <' + elementx )
        getcontrolList = self.get_control_list_name(elementx)
        logger.info('Text:' + str(getcontrolList))
        return self.guihelper.find_gui_element(getcontrolList[0], getcontrolList[1]).text

    def get_text_value(self, elementx):
        getcontrolList = self.guihelper.window_opened_by_name(self.window_title)
        textgauto = gauto.TextControl(searchFromControl=getcontrolList, Name=elementx)
        result = gauto.WaitForExist(textgauto, 30)
        if result == True:return textgauto
        else:logger.info('control not found')

class WindowControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

    def Window_Name_Open(self, winName):
        mmcWindow = gauto.WindowControl(Name=winName)
        logger.info(mmcWindow)
        return mmcWindow

class RadioButtonControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class ScrollBarControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class SemanticZoomControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class SeparatorControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class SliderControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class SpinnerControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class SplitButtonControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class StatusBarControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class TabControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class TabItemControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class TableControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class ThumbControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class TitleBarControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class ToolBarControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class ToolTipControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class TreeControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)

class TreeItemControl(BaseTest):

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(driver, parent_handle)
        winHandle = self.guihelper.window_handle_title()
        self.window_title=self.guihelper.window_title_exists(winHandle)
