import xlrd,xlwt,os
from configparser import ConfigParser
class Public_tool():
    def file_path(self,path):
        current_path=os.path.dirname(__file__)
        file_path=os.path.join(current_path,path)
        return file_path

    def rade_excel(self,file_path,sheet):
        workbook=xlrd.open_workbook(file_path)
        worksheet=workbook.sheet_by_name(sheet)
        col=worksheet.ncols
        row=worksheet.nrows
        all_date=[]
        for i in range(1,row):
            w={}
            for z in range(col):
                w[worksheet.cell_value(0,z)]=worksheet.cell_value(i,z)
            all_date.append(w)
        return all_date

    def roller(self,driver,element):
        driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_conf(self):
        taeget = ConfigParser()
        current_path = os.path.dirname(__file__)
        conf_path = os.path.join(current_path, '../Conf/local_config.ini')
        taeget.read(conf_path, encoding='utf-8')
        return taeget
Pub=Public_tool()