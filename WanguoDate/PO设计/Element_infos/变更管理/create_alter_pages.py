from selenium.webdriver.common.by import By
from selenium import webdriver
from PO设计.Common.log_untils import logger
from PO设计.Common.base_page import BasePage
import os,time
from PO设计.Common.element_date_utils import ElementDateUtils
from PO设计.Common.browser import Browser

class CreateAlterPages(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        #页面控件属性
        elements=ElementDateUtils('变更管理').get_element_info('create_alter_pages')
        self.alter_name_inputbox=elements['alter_name']
        self.data_center_select_click=elements['data_center_select']
        self.create_alter_frame = elements['create_alter_frame']



    #页面操作方法
    def switch_to_frame_create_alter(self):
        self.switch_to_frame_by_element(self.create_alter_frame)

    def input_alter_name(self,alter_name):
        self.input(self.alter_name_inputbox,alter_name)
        logger.info('输入变更名称：'+str(alter_name))
