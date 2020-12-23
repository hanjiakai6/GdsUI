from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from PO设计.Common.log_untils import logger
from selenium.webdriver.support.ui import WebDriverWait
import time,os
from PO设计.Common.config_untils import local_config
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from PO设计.Common import HTMLTestReportCN

class BasePage():
    def __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Chrome()


    #封装元素识别
    def find_element(self,element_info):
        try:
            local_type_name=element_info['locator_type']
            local_value_info=element_info['locator_value']
            local_timeout=element_info['timeout']
            if local_type_name=='id':
                locator_type=By.ID
            elif local_type_name=='name':
                locator_type=By.NAME
            elif local_type_name=='class':
                locator_type = By.CLASS_NAME
            elif local_type_name=='xpath':
                locator_type = By.XPATH
            elif local_type_name=='css':
                locator_type = By.CSS_SELECTOR
            elif local_type_name=='link':
                locator_type=By.LINK_TEXT
            elif local_type_name=='tag':
                locator_type=By.TAG_NAME
            element=WebDriverWait(self.driver,local_timeout).until(lambda x: x.find_element(locator_type,local_value_info))
            logger.info('[{}]元素识别成功'.format(element_info['element_name']))
        except UnboundLocalError as e:
            logger.error('[{}]元素不能识别，请检查[element]')
        except Exception as e:
            logger.error('[{}]元素不能识别，原因是{}：'.format(element_info['element_name'],e.__str__()))
            self.screentshot_as_file()
        finally:
            if element is UnboundLocalError:
                element=None
        return element



    #元素基本操作方法
    def click(self,element_info):
        element=self.find_element(element_info)
        try:
            element.click()
            logger.info('点击[{}]元素'.format(element_info['element_name']))
        except Exception as e:
            logger.error('点击[{}]元素失败，原因是：'.format(element_info['element_name']),e.__str__())
            self.screentshot_as_file()

    def input(self,element_info,content):
        element=self.find_element(element_info)
        try:
            element.send_keys(content)
            logger.info('输入[{}]元素'.format(element_info['element_name']))
        except Exception as e:
            logger.error('点击[{}]元素失败，原因是：'.format(element_info['element_name']),e)

    def open_url(self,url):
        try:
            self.driver.get(url)
            logger.info('打开浏览器地址：{}'.format(url))
        except Exception as e:
            logger.error('不能打开指定的网址，原因是:{}'.format(e))

    def get_url(self):
        url=self.driver.current_url
        logger.info('获取网页url:{}'.format(url))
        return url

    def get_title(self):
        title=self.driver.title
        logger.info('title为：{}'.format(title))
        return title

    def get_text(self,element_info):
        element=self.find_element(element_info)
        value=element.text
        return value

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('浏览器最大化')

    def impl_wait(self,time=local_config.impl_time):
        self.driver.implicitly_wait(time)
        logger.info('添加隐式等待')

    def wait(self,seconds=local_config.time_out):
        time.sleep(seconds)
        logger.info('等待{}秒'.format(seconds))

    def refresh(self):
        self.driver.refresh()
        logger.info('页面刷新')

    def quite(self):
        self.driver.quit()
        logger.info('关闭浏览器')


    #页面操作封装
    #切框架
    # 示范：element=self.find_element(element_info)  switch_to_frame(element=element)
    # 示范：switch_to_frame(id=framid)
    def switch_to_frame(self,**element_dict):
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        if 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        if 'element' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['element'])

    def switch_to_frame_by_element(self, element_info):
        element = self.find_element(element_info)
        self.driver.switch_to.frame(element)

    #js操作封装
    #封装移除元素的value属性/添加元素的value属性
    def delete_element_attribute(self,element_info,attribute_name):
        element = self.driver.find_element(element_info)
        js='arguments[0].removeAttribute({})'.format(attribute_name)

    def update_element_attribute(self,element_info,attribute_name,attribute_value):
        element = self.driver.find_element(element_info)
        js = 'arguments[0].setAttribute({},{})'.format(attribute_name,attribute_value)
        self.driver.execute_script(js,element)

    #封装滚轴
    def scoll(self,element_info):
        element=self.find_element(element_info)
        print(element)
        self.driver.execute_script("arguments[0].scrolllntoView(false);",element)
        time.sleep(1)

    #鼠标操作
    #  移动鼠标到指定位置
    def move_to_element_by_mouse(self,element_info):
        element=self.driver.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()

    #双击
    def double_click_by_mouse(self,element_info):
        element=self.driver.find_element(element_info)
        ActionChains(self.driver).double_click(element).perform()

    #鼠标右击
    def right_click_element(self,element_info):
        element=self.driver.find_element(element_info)
        ActionChains(self.driver).double_click(element).perform()

    # 键盘操作
    # ctrl+s
    def control_s(self):
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL).perform()

    #弹出框处理
    def switch_to_alter(self,action='accept',time_out=1):
        WebDriverWait(self.driver,10).until(EC.alert_is_present())
        alter=self.driver.switch_to.alert()
        alter_text=alter.text
        if action =='accept':
            alter.accept()
        else:
            alter.dismiss()
        return alter_text

    #切换句柄的封装
    #多页面切换
    #获取当前句柄
    def get_windows_handle(self):
        return self.driver.current_window_handle
    #切句柄
    def switch_to_windows_by_handle(self,window_handle):
        self.driver.switch_to.window(window_handle)

    #根据title切换句柄
    def switch_to_window_by_title(self,title):
        window_handles=self.driver.window_handles
        for windou_handle in window_handles:
            if WebDriverWait(self.driver,local_config.time_out).until(EC.title_contains(title)):
                self.driver.switch_to.window((windou_handle))
                break

    #跟据url切换句柄
    def switch_to_window_by_url(self,url):
        window_handles=self.driver.window_handles
        for window_handle in window_handles:
            if WebDriverWait(self.driver,local_config.time_out).until(EC.url_contains(url)):
                self.driver.switch_to.window(window_handle)
                break

    #错误截图封装
    def screentshot_as_file(self,*screentshot_path):
        if len(screentshot_path)==0:
            screentshot_filepath=local_config.screent_shot_path
        else:
            screentshot_filepath=screentshot_path[0]
        now=time.strftime('%Y_%m_%d_%H_%M_%S')
        current_path=os.path.dirname(__file__)
        screentshot_filepath=os.path.join(current_path,'..',screentshot_filepath,'UItest_{}.png'.format(now))
        print(screentshot_filepath)
        self.driver.save_screenshot(screentshot_filepath)

    def screentshot_to_report(self):
        report_path=os.path.join(os.path.abspath(os.path.dirname(__file__)),'..',local_config.report_path)
        report_dir=HTMLTestReportCN.ReportDirectory(report_path)
        report_dir.get_screenshot(self.driver)
