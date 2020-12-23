from 线性设计.TestCase import demo_Baidu
import unittest,os,time
from HTMLTestRunner import HTMLTestRunner
from 线性设计.Public.public_Tool import Pub
class Test_suite():
    def get_allcase(self):
        now_path=os.path.join(os.path.dirname(os.path.abspath(__file__)))
        case_path=os.path.join(now_path,'../TestCase')
        print(case_path)
        discover=unittest.TestLoader().discover(case_path,
                                              pattern='suite*.py',
                                              top_level_dir=None)
        suite=unittest.TestSuite()
        suite.addTest(discover)
        return suite
if __name__ == '__main__':
    suite=Test_suite().get_allcase()
    # unittest.main(defaultTest='suite')
    # suite=unittest.TestSuite()
    # from 线性设计.TestCase import suite_Case_01
    # suite.addTest(suite_Case_01.Test_case('test_login'))
    # # unittest.main(defaultTest='suite')
    nowtime = time.strftime('%Y-%m-%d %H-%M-%S')
    file_path=Pub.file_path('../report/test_report_{}.html'.format(nowtime))
    print(file_path)
    file=open(file_path,'wb')
    runner=HTMLTestRunner(stream=file,
                          title='Gds_report',
                          description='report_runner')
    runner.run(suite)
