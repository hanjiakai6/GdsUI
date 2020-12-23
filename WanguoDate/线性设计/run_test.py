import time,os,unittest,HTMLTestRunner
import threading
#报告存放路径
current_path=os.path.dirname(__file__)
report_path=os.path.join(current_path,'report')
#存放用例路径
case_path=os.path.join(current_path,'TestCase')
#加载满足匹配规则的用例
discover=unittest.defaultTestLoader.discover(case_path,
                                             pattern='suite*.py',
                                             top_level_dir=case_path)
nowdate=time.strftime('%Y-%m-%d')
nowtime=time.strftime('%H-%M-%S')
# try:
#     file_path=os.path.join(current_path,'report/report{}'.format(nowdate))
#     os.mkdir(file_path)
# except Exception:
#     pass
html_path=os.path.join(current_path,'report/report{}/test_report_{}.html'.format(nowdate,nowtime))
file=open(html_path,'wb')
main_suite=unittest.TestSuite()
main_suite.addTest(discover)
runner=HTMLTestRunner.HTMLTestRunner(stream=file,
                                     title='Gds_report',
                                     description='report_runner')

runner.run(main_suite)

