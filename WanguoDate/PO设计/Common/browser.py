import os
from selenium import webdriver
from PO设计.Common.config_untils import local_config
from selenium.webdriver.chrome.options import Options

#driver二次封装 支持chrome firefox edge三种浏览器
current_path=os.path.dirname(__file__)
dri_path=os.path.join(current_path,'..',local_config.get_driver_path)
driver_name=local_config.driver_name
class Browser():
    def __init__(self,driver_path=dri_path):
        self.__driver_path=driver_path
        self.__driver_name=driver_name

    def get_driver(self):
        if self.__driver_name=='chrome':
            return Browser().__get_chrome_driver()
        elif self.__driver_name=='firefox':
            return Browser().__get_firefox_driver()
        elif self.__driver_name=='edge':
            return Browser().__get_edge_driver()

    def __get_chrome_driver(self):
        # chrome_options = Options()
        # chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        # chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        # chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
        # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示

        chrome_driver_path=os.path.join(self.__driver_path,'chromedriver.exe')
        driver=webdriver.Chrome(executable_path=chrome_driver_path)
        return driver

    def __get_firefox_driver(self):
        firefox_driver_path=os.path.join(self.__driver_path,'geckodriver.exe')
        driver=webdriver.Firefox(executable_path=firefox_driver_path)
        return driver

    def __get_edge_driver(self):
        edge_driver_path=os.path.join(self.__driver_path,'msedgedriver.exe')
        driver=webdriver.Edge(executable_path=edge_driver_path)
        return driver

    #分布式 远程浏览器驱动  多台电脑分布式并发执行，不同浏览器跑同一套脚本
    def get_remote_driver(self): #selenium支持分布式执行grid
        pass

if __name__ == '__main__':
    driver=Browser().get_driver()
    driver.get('https://www.baidu.com')