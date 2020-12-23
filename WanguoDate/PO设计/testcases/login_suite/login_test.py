import unittest
from PO设计.actions.login_action import LoginAction
from PO设计.Common.browser import Browser
from PO设计.Common.base_page import BasePage
from PO设计.Common.config_untils import local_config
from PO设计.Common.log_untils import logger
from PO设计.actions.select_entrance import Select_Entrance
from PO设计.Common.selenium_base_case import SeleniumBaseCase
from PO设计.Element_infos.login_page.login_pages import LoginPages
from PO设计.Common.element_date_utils import ElementDateUtils
from PO设计.Common.test_date_untils import TestDateUntils

class LoginTest(SeleniumBaseCase):
    def setUp(self) -> None:
        super().setUp()
        self.test_class_date=TestDateUntils('login_suite','LoginTest').convert_exceldate_to_testdate()


    def test_login_success(self):
        login_action=LoginAction(self.base_page.driver)
        text1=login_action.login_default_success()
        self.assertEqual(text1,local_config.user_name_text,'登录失败，请检查对应用户姓名是否填写正确')
        logger.info('用户登录校验成功')
        select_action=Select_Entrance(self.base_page.driver)
        select_action.select_entrance()
        self.base_page.wait(3)

    def test_login_fail(self):
        test_function_date=self.test_class_date['test_login_fail']
        self._testMethodDoc=test_function_date['test_name']
        login_page=LoginPages(self.base_page.driver)
        login_page.input_username(test_function_date['test_parameter']['username'])
        login_page.input_password(test_function_date['test_parameter']['password'])

        element_info=ElementDateUtils('login').get_element_info('login_page')['login_button']
        login_page.click(element_info)
        logger.info('[{}]执行成功'.format(self._testMethodDoc))
        self.base_page.wait(5)



if __name__ == '__main__':
    unittest.main()

