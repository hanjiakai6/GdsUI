import unittest
from PO设计.actions.login_action import LoginAction
from PO设计.Common.browser import Browser
from PO设计.Common.base_page import BasePage
from PO设计.Common.config_untils import local_config
from PO设计.Common.log_untils import logger
from PO设计.actions.select_entrance import Select_Entrance
from PO设计.Common.selenium_base_case import SeleniumBaseCase
from PO设计.Element_infos.变更管理.create_alter_pages import CreateAlterPages

class CreateAlterTest(SeleniumBaseCase):


    def test_create(self):
        login_action=LoginAction(self.base_page.driver)
        text1=login_action.login_default_success()
        self.assertEqual(text1,local_config.user_name_text,'登录失败，请检查对应用户姓名是否填写正确')
        logger.info('用户登录校验成功')
        select_action=Select_Entrance(self.base_page.driver)
        select_action.select_entrance()
        self.base_page.wait(3)
        create=CreateAlterPages(self.base_page.driver)
        create.switch_to_frame_create_alter()
        create.input_alter_name('1223')
        create.wait(10)

if __name__ == '__main__':
    ca=CreateAlterTest().create()