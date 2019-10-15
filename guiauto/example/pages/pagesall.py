from guiauto.gui.base_test import BaseTest
from guiauto.util.guiutils import guiHelper
from guiauto.example.pages import emailpage, ffAttachments
class allPages(BaseTest):
    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.guihelper=guiHelper(self.driver, self.parent_handle)
        self.emailWindow=emailpage.emailWindow(self.driver, self.parent_handle)
        self.ffattachments=ffAttachments.ffAttach(self.driver, self.parent_handle)


