import logging
from guiauto.gui.base_test import BaseTest
from guiauto.util.guiutils import guiHelper
from guiauto.gui.controlDriver import driveControl
logger = logging.getLogger(__name__)

class emailWindow(BaseTest):
    outLookHome = {'Newemail_button': 'New Email',
                   'Newitems_button': 'New Items'}
    newEmailWindow = {'To_button': 'To', 'Cc_button': 'Cc', 'Subject_text': 'Subject',
                      'Body_Edit': 'Page 1 content', 'Send_button': 'Send'}
    newItemsWindow = {'emailMessage_menuitem': 'E-mail Message'}
    accellionGroup = {'accellion_group': 'Accellion', 'off_button': 'Off',
                      'secured_button': 'Secured', 'attach_menuitem': 'Attach', 'attachfile_menuitem': 'Attach File',
                      'attachfolder_menuitem': 'Attach Folder'}
    accellionSecure_dialog = {'SecuredPane_Window': 'Accellion for Outlook', 'SecuredDialog': 'tableLayoutPanel',
                              'SecuredRemoved': 'buttonPanel', 'removeSecure_link': 'Remove Security'}
    fileDialog = {'FileDialog_WindowName': 'Open', 'FileDialog_Button': 'Open',
                  'FileDialog_FileName_Edit': 'File name:'}
    folderDialog = {'FolderDialog_Button': 'Select Folder', 'FolderDialog_FolderName_Edit': 'Folder:'}

    def __init__(self, driver, parent_handle):
        super().__init__(driver, parent_handle)
        self.window_title=driver.title
        self.cDriver = driveControl(self.driver, self.parent_handle)

    """Button"""
    def click_new_email_button(self):
        self.cDriver.button.click_action_button(elementx=self.outLookHome['Newemail_button'], wintitle=self.window_title)

    def click_send_button(self):
        self.cDriver.button.click_action_button(elementx=self.newEmailWindow['Send_button'])

    def click_off_button(self):
        self.cDriver.button.click_action_button(elementx=self.accellionGroup['off_button'])

    def click_secured_button(self):
        self.cDriver.button.click_action_button(elementx=self.accellionGroup['secured_button'])

    def click_remove_security_link_action(self):
        self.cDriver.button.click_action_button(elementx=self.accellionSecure_dialog['removeSecure_link'])

    """Edit"""
    def enter_to_address(self, value):
        self.cDriver.edit.type_send_keys(elementx=self.newEmailWindow['To_button'], value=value)

    def enter_subject(self, value):
        self.cDriver.edit.type_send_keys(elementx=self.newEmailWindow['Subject_text'], value=value)

    def click_area_on_focus(self):
        self.cDriver.edit.clickable_action_Points(elementx=self.newEmailWindow['Body_Edit'])

    def enter_data_on_body(self, txtvalue):
        self.click_area_on_focus()
        self.cDriver.edit.type_send_keys_autogui(txtvalue=txtvalue)

    """MenuItem"""
    def click_new_items_button(self):
        self.cDriver.menuitem.click_action_button(elementx=self.outLookHome['Newitems_button'], wintitle=self.window_title)

    def click_eMessage_menuitem(self):
        self.cDriver.menuitem.click_action_button(elementx=self.newItemsWindow['emailMessage_menuitem'])

    def click_attach_menuitem(self):
        self.cDriver.menuitem.click_action_button(elementx=self.accellionGroup['attach_menuitem'])

    def click_attach_file_menuitem(self):
        self.cDriver.menuitem.click_action_button(elementx=self.accellionGroup['attachfile_menuitem'])

    def click_attach_folder_menuitem(self):
        self.cDriver.menuitem.click_action_button(elementx=self.accellionGroup['attachfolder_menuitem'])

    """Group"""
    def get_acc_group_items(self):
        return self.cDriver.group.get_group_childrens(elementx=self.accellionGroup['Accellion'])

    """Pane"""
    def get_pane_details_secure(self):
        return self.cDriver.pane.get_current_pane_children_details(elementx=self.accellionSecure_dialog['SecuredDialog'])

    def get_pane_details_secure_removed(self):
        return self.cDriver.pane.get_current_pane_children_details(elementx=self.accellionSecure_dialog['SecuredRemoved'])

    """Text"""
    def get_text(self, value):
        return self.cDriver.text.getText(value)