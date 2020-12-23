import unittest
from selenium import webdriver
import time,os
from 线性设计.Log.logging import logger
from 线性设计.Public.public_Tool import Pub

chrome_driver_path=Pub.file_path('../webdriver/chromedriver.exe')

class Public_class(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get('https://petest.gds-services.com/portal/#/portal/r_todo')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        time.sleep(3)
        self.driver.quit()



