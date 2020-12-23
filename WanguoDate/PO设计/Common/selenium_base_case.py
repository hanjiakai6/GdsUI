from PO设计.Common.base_page import BasePage
from PO设计.Common.config_untils import local_config
from PO设计.Common.element_date_utils import ElementDateUtils
from PO设计.Common.log_untils import logger
from PO设计.Common.browser import Browser
import unittest
#初始化方法 结束后方法
class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info('========测试类开始执行========')
        cls.url=local_config.get_url
    def setUp(self) -> None:
        logger.info('--------测试方法开始执行--------')
        self.base_page=BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.impl_wait()
        self.base_page.open_url(self.url)
    def tearDown(self) -> None:
        logger.info('--------测试方法执行结束--------')
        self.base_page.quite()
    @classmethod
    def tearDownClass(cls) -> None:
        logger.info('========测试类执行完毕========')