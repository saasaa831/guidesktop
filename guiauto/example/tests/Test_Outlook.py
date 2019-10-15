from unittest import TestCase
import time, traceback, os, logging.config
from pytest import mark
from guiauto.gui.appDriver import BrowserDriver
from guiauto.gui.driverStart import sdownProcess
from guiauto.util.archive import setup_logging
from guiauto.example.pages.pagesall import allPages
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath("../..")
#log_file = open(os.path.join(root_path, 'config', 'config.conf'))
setup_logging(default_path=root_path)
logger = logging.getLogger(__name__)

class BaseTest(TestCase):
    driver = None
    browser = None

    @classmethod
    def setUpClass(cls):
        #UserFunction.set_config(cls)
        cls.browser = 'OUTLOOK.EXE'
        cls.driver = BrowserDriver(cls.browser).driver
        cls.driver.implicitly_wait(10)
        time.sleep(2)
        cls.driver.switch_to.window(cls.driver.window_handles[0])
        cls.parent_handle = cls.driver.current_window_handle
        cls.cDriver = allPages(cls.driver, cls.parent_handle)
        logger.info(cls.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        sdownProcess(cls.browser)


    #@mark.py3dev
    def test_001_try_send_via_outlook_new_email(self):
        logger.info('Testcase-01: Send new email from outlook')
        try:
            self.cDriver.emailWindow.click_new_email_button()
            self.cDriver.emailWindow.enter_to_address(value='ishafee01@gmail.com')
            self.cDriver.emailWindow.enter_subject(value='First_revisioned_subject_001')
            self.cDriver.emailWindow.enter_data_on_body(txtvalue='This is first revisioned body message')
            self.cDriver.emailWindow.click_send_button()
        except Exception as e:
            logger.error(traceback.format_exc())
            raise Exception(str(e))

    #@mark.py3dev
    def test_002_try_send_via_outlook_new_items(self):
        logger.info('Testcase-02: Send email messages from outlook via New Items')
        try:
            self.cDriver.emailWindow.click_new_items_button()
            self.cDriver.emailWindow.click_eMessage_menuitem()
            self.cDriver.emailWindow.enter_to_address('ishafee01@gmail.com')
            self.cDriver.emailWindow.enter_subject('Sub: Second from New items <<>> email message')
            self.cDriver.emailWindow.enter_data_on_body('Second from New items >> email message')
            self.cDriver.emailWindow.click_send_button()
        except Exception as e:
            logger.error(traceback.format_exc())
            raise Exception(str(e))

    #@mark.py3dev
    def test_003_try_send_via_outlook_accellion_group_items(self):
        logger.info('Testcase-03: try validate accellion plugin group controls check secured')
        try:
            self.cDriver.emailWindow.click_new_email_button()
            b4secure = self.cDriver.emailWindow.get_acc_group_items()
            if 'Off' in b4secure:
                self.cDriver.emailWindow.click_off_button()
                afsecure = self.cDriver.emailWindow.get_acc_group_items()
                self.assertIn('Secured', afsecure)
        except Exception as e:
            logger.error(traceback.format_exc())
            raise Exception(str(e))

    #@mark.py3dev
    def test_004_try_send_via_outlook_accellion_group_items(self):
        logger.info('Testcase-04: Try get labels of secured items')
        try:
            b4secure = self.cDriver.emailWindow.get_acc_group_items()
            if 'Secured' in b4secure:
                self.cDriver.emailWindow.click_secured_button()
                afsecure = self.cDriver.emailWindow.get_pane_details_secure()
                # afsecure = panectrl.get_pane_children_details()
                logger.info(afsecure)
        except Exception as e:
            logger.error(traceback.format_exc())
            raise Exception(str(e))

    #@mark.py3dev
    def test_005_try_send_via_outlook_accellion_group_items(self):
        logger.info('Testcase-05: Try Remove Security on controls')
        try:
            afsecure = self.cDriver.emailWindow.get_pane_details_secure_removed()
            if 'Remove Security' in afsecure:
                self.cDriver.emailWindow.click_remove_security_link_text()
                logger.info(afsecure)
        except Exception as e:
            logger.error(traceback.format_exc())
            raise Exception(str(e))

    #@mark.py3dev
    def test_006_try_send_via_outlook_accellion_group_items_attach_file(self):
        logger.info('Testcase-06: Try Attach file to new email')
        try:
            #self.cDriver.emailWindow.click_new_email_button()
            self.cDriver.emailWindow.enter_to_address('ishafee01@gmail.com')
            self.cDriver.emailWindow.enter_subject('With Accellion Group Attach file')
            self.cDriver.emailWindow.click_attach_menuitem()
            self.cDriver.emailWindow.click_attach_file_menuitem()
            valkey = os.path.join(root_path, 'example', 'files', 'KW_TestData1.xlsx')
            logger.info(valkey)
            self.cDriver.ffattachments.file_attachment(valkey)
            self.cDriver.ffattachments.file_attach_open_button()
            txttn = self.cDriver.emailWindow.get_text('KW_TestData1.xlsx')
            logger.info('Texts:' + str(txttn))
            self.cDriver.emailWindow.click_send_button()
            # self.assertEqual('KW_TestData1.xlsx', txttn)
        except Exception as e:
            logger.error(traceback.format_exc())
            raise Exception(str(e))

    #@mark.py3dev
    def test_007_try_send_via_outlook_accellion_group_items_attach_folder(self):
        logger.info('Testcase-07: Try Attach folder to new email')
        try:
            self.cDriver.emailWindow.click_new_email_button()
            self.cDriver.emailWindow.enter_to_address('ishafee01@gmail.com')
            self.cDriver.emailWindow.enter_subject('With Accellion Group Attach folder')
            self.cDriver.emailWindow.click_attach_menuitem()
            self.cDriver.emailWindow.click_attach_folder_menuitem()
            valkey = os.path.join(root_path, 'example', 'files', 'trayfiles')
            #logger.info(valkey)
            self.cDriver.ffattachments.folder_attachment(valkey)
            self.cDriver.ffattachments.folder_attach_select_folder_button()
            txttn = self.cDriver.emailWindow.get_text('trayfiles.zip')
            #logger.info('Folder:'+str(txttn))
            self.cDriver.emailWindow.click_send_button()
            self.assertEqual('trayfiles.zip', txttn)
        except Exception as e:
            logger.error(traceback.format_exc())
            raise Exception(str(e))