import unittest,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from 线性设计.Public.public_Class import Public_class
from 线性设计.Public.public_Tool import Pub
class BaiDu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()
    def test_Case1(self):
        self.driver.find_element_by_id('kw').send_keys('123')
        time.sleep(2)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        element=self.driver.find_element(By.XPATH,'//*[text()="下一页 >"]')
        Pub.roller(self.driver,element)
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()