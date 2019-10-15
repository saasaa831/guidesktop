from guiauto.gui.base_test import BaseTest
from guiauto.gui.controlDriver import driveControl

class ffAttach(BaseTest):
    folderDialog = {'folder_WindowName': 'Accellion for Outlook Desktop: Choose a folder to attach.',
                    'folder_Button': 'Select Folder', 'folder_Edit': 'Folder:'}
    fileDialog = {'file_WindowName': 'Open', 'file_Button': 'Open', 'file_Edit': 'File name:'}

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.cDriver = driveControl(self.driver, self.parent_handle)

    """Edit"""
    def file_attachment(self, value):
        self.cDriver.edit.type_send_keys_gui_action(value, self.fileDialog['file_WindowName'],
                                                    self.fileDialog['file_Edit'])

    def folder_attachment(self, value):
        self.cDriver.edit.type_send_keys_gui_action(value, self.folderDialog['folder_WindowName'],
                                                    self.folderDialog['folder_Edit'])

    """Button"""
    def file_attach_open_button(self):
        self.cDriver.button.click_open_button(self.fileDialog['file_WindowName'], self.fileDialog['file_Button'])

    def folder_attach_select_folder_button(self):
        self.cDriver.button.click_action_button(self.folderDialog['folder_Button'])