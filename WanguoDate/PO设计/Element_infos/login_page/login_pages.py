from selenium.webdriver.common.by import By
from selenium import webdriver
from PO设计.Common.log_untils import logger
from PO设计.Common.base_page import BasePage
import os,time
from PO设计.Common.element_date_utils import ElementDateUtils
from PO设计.Common.browser import Browser

class LoginPages(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        #页面控件属性
        elements=ElementDateUtils('login').get_element_info('login_page')
        self.username_inputbox=elements['username_inputbox']
        self.password_inputbox=elements['password_inputbox']
        self.login_button=elements['login_button']




    #页面操作方法
    def input_username(self,username):
        self.input(self.username_inputbox,username)
        logger.info('用户名输入框输入：'+str(username))
    def input_password(self,password):
        self.input(self.password_inputbox,password)
        logger.info('密码输入框输入：'+str(password))
    def click_login(self):
        self.click(self.login_button)
        logger.info('点击登录按钮')




if __name__ == '__main__':
    # current=os.path.dirname(__file__)
    # driver_path=os.path.join(current,'../webdriver/chromedriver.exe')
    # driver=webdriver.Chrome(executable_path=driver_path)
    driver=Browser().get_driver()
    login_page=LoginPages(driver)
    login_page.open_url('https://petest.gds-services.com/portal/#/portal/r_todo')
    login_page.set_browser_max()
    login_page.impl_wait(10)
    login_page.input_username('chaiguangfei')
    login_page.input_password('Gds1234567890')
    login_page.click_login()
    time.sleep(5)
    login_page.screentshot_as_file()
    time.sleep(3)
    login_page.quite()