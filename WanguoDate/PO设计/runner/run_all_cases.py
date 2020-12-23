from PO设计.Common.config_untils import local_config
import os
import unittest
from PO设计.Common import HTMLTestReportCN

current=os.path.dirname(__file__)
case_path=os.path.join(current,'..',local_config.case_path)
report_path=os.path.join(current,'..',local_config.report_path)
print(case_path)
print(report_path)

class RunAllCase():
    def __init__(self):
        self.test_case_path=case_path
        self.report_path=report_path
        self.titlt='自动化测试报告'
        self.descrition='gds-test'

    def run(self):
        discover=unittest.defaultTestLoader.discover(start_dir=self.test_case_path,
                                                     pattern='*alter_test.py',
                                                     top_level_dir=self.test_case_path)
        all_suite=unittest.TestSuite()
        all_suite.addTest(discover)


        report_dir=HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.titlt)
        report_path =HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp=open(report_path,'wb')

        runner=HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                               title=self.titlt,
                                               description=self.descrition,
                                               tester='axin')

        runner.run(all_suite)
        fp.close()

if __name__ == '__main__':
    RunAllCase().run()