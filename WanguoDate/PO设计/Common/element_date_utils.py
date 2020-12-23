import os,xlrd
curren_path=os.path.dirname(__file__)
excel_path=os.path.join(curren_path,'../Element_info_date/element_infos.xlsx')
#excel表数据读取
class ElementDateUtils():
    def __init__(self,modult_name,excel_path=excel_path):
        self.excel_path=excel_path
        self.workbook=xlrd.open_workbook(self.excel_path)
        self.worksheet=self.workbook.sheet_by_name(modult_name)
        self.row_cont=self.worksheet.nrows

    def get_element_info(self,page_name):
        '''
        读取表中数据
        :param page_name: 页面名，对应表中的页面名称
        :return:字典类型{a:{a1:1,a2:2}，b:{b1:1,b2:2}}
        '''
        element_infos = {}
        for i in range(1,self.row_cont):
            if self.worksheet.cell_value(i,2)==page_name:
                element_info = {}
                element_info['element_name'] = self.worksheet.cell_value(i, 1)
                element_info['locator_type'] = self.worksheet.cell_value(i, 3)
                element_info['locator_value'] = self.worksheet.cell_value(i, 4)
                element_info['timeout'] = self.worksheet.cell_value(i, 5)
                element_infos[self.worksheet.cell_value(i, 0)] = element_info
        return element_infos

if __name__ == '__main__':
    e=ElementDateUtils('login')
    a=e.get_element_info('login_page')
    print(a)
