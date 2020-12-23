import os
from PO设计.Common.excel_unitils import ExcelUnitils
from PO设计.Common.config_untils import local_config

curren_path=os.path.dirname(__file__)
excel_path=os.path.join(curren_path, '..',local_config.testdate_path)

class TestDateUntils():
    def __init__(self,test_suite_name,test_class_name):
        self.test_class_name=test_class_name
        self.excel_date=ExcelUnitils(excel_path,test_suite_name).get_sheet_date_by_list()
        self.excel_rows=len(self.excel_date)

    #例：{test_login_success:{test_name:验证能否登陆成功，isnot:是，excepted_result:柴光飞，test_parameter：{username：1，password:2}}}
    def convert_exceldate_to_testdate(self):
        test_date_infos={}
        for i in range(1,self.excel_rows):
            test_date_info={}
            if self.excel_date[i][2].__eq__(self.test_class_name):
                test_date_info['test_name']=self.excel_date[i][1]
                test_date_info['isnot']=self.excel_date[i][3]
                test_date_info['excepted_result']=self.excel_date[i][4]
                test_parameter={}
                for j in range(5,len(self.excel_date[i])):
                    if self.excel_date[i][j].__contains__('=') and len(self.excel_date[i][j])>=2:
                            parameter_info=self.excel_date[i][j].split('=')
                            test_parameter[parameter_info[0]]=parameter_info[1]
                test_date_info['test_parameter']=test_parameter
            test_date_infos[self.excel_date[i][0]]=test_date_info
        return test_date_infos

if __name__ == '__main__':
    infos=TestDateUntils('login_suite','LoginTest').convert_exceldate_to_testdate()
    for i in infos.values():
        print(i)