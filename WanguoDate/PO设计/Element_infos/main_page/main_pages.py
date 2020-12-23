from PO设计.Common.log_untils import logger
from PO设计.Common.base_page import BasePage
import os,time
from PO设计.Common.element_date_utils import ElementDateUtils
from PO设计.Common.browser import Browser

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        element=ElementDateUtils('main').get_element_info('main_page')
        element_system=ElementDateUtils('main').get_element_info('system_main_page')
        element_system['system_name_click']['locator_value']=element_system['system_name_click']['locator_value']%"变更管理"
        element_system['system_event_link']['locator_value']=element_system['system_event_link']['locator_value']%("变更管理","新建变更单")

        self.system_link=element['system_link']
        self.system_name_click=element_system['system_name_click']
        self.system_event_link = element_system['system_event_link']
        self.user_name_text = element['user_name_text']

    def click_system_link(self):
        self.click(self.system_link)

    def click_system_name(self):
        self.click(self.system_name_click)

    def click_system_event(self):
        self.click(self.system_event_link)

if __name__ == '__main__':
    print(MainPage(1).system_name_click)
    print(MainPage(1).system_event_link)