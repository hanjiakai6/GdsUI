import xlrd,os
from PO设计.Common.config_untils import local_config
from PO设计.Common.log_untils import logger
class ExcelUnitils():
    def __init__(self,excel_path,sheet_name=None):
        self.excel_path=excel_path
        self.sheet_name=sheet_name
        self.sheet_date=self.__get_sheet_date()

    def __get_sheet_date(self):
        workbook=xlrd.open_workbook(self.excel_path)
        if self.sheet_name==None:
            sheet=workbook.sheet_by_index(0)
        else:
            sheet=workbook.sheet_by_name(self.sheet_name)
        return sheet

    @property
    def get_row_count(self):
        row_count=self.sheet_date.nrows
        return row_count

    @property
    def get_col_count(self):
        col_count=self.sheet_date.ncols
        return col_count

    def get_sheet_date_by_list(self):
        all_test_date=[]
        for rownum in range(self.get_row_count):
            row_excel_date=[]
            for colnum in range(self.get_col_count):
                row_excel_date.append(self.sheet_date.cell_value(rownum,colnum))
            all_test_date.append(row_excel_date)
        return all_test_date

if __name__ == '__main__':
    curren_path=os.path.dirname(__file__)
    excel_path=os.path.join(curren_path, '../Test_date/test_date.xlsx')
    ex=ExcelUnitils(excel_path,'Sheet1')
    li=ex.get_sheet_date_by_list()
    print(li)

