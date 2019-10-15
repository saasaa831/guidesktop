from guiauto.util.guiutils import guiHelper
from .controlA2P import *
from .controlR2W import *

class driveControl(guiHelper):
    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.button=ButtonControl(driver, parent_handle)
        self.edit=EditControl(driver, parent_handle)
        self.text=TextControl(driver, parent_handle)
        self.pane=PaneControl(driver, parent_handle)
        self.group=GroupControl(driver, parent_handle)
        self.menuitem=MenuItemControl(driver, parent_handle)
        self.windowbx=WindowControl(driver, parent_handle)
