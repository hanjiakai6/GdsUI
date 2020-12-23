import os,xlrd
curren_path=os.path.dirname(__file__)
excel_path=os.path.join(curren_path,'../Element_info_date/element_infos.xlsx')

workbook=xlrd.open_workbook(excel_path)
worksheet=workbook.sheet_by_name('login_page')
row=worksheet.nrows

element_infos={}

for i in range(1,row):
    element_info={}
    element_info['element_name']=worksheet.cell_value(i,1)
    element_info['locator_type']=worksheet.cell_value(i,2)
    element_info['locator_value']=worksheet.cell_value(i,3)
    element_info['timeout']=worksheet.cell_value(i,4)
    element_infos[worksheet.cell_value(i,0)]=element_info

print(element_infos)