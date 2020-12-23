import unittest,time,os
import threading
from 线性设计.Public.public_Class import Public_class
from 线性设计.Public.login import login
from 线性设计.Public.public_Tool import Pub
class Test_case(Public_class):
    def test_login(self):
        '''登陆成功案例'''
        taeget=Pub.get_conf()
        username=taeget.get('default','username')
        password=taeget.get('default','password')
        login(self.driver,username,password)
        name=self.driver.find_element_by_xpath('//*[@class="ri-name"]').text
        self.assertEqual(name,'柴光飞','账号登陆失败')
    def test_login_fail(self):
        pass

