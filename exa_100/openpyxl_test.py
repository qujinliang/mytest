import openpyxl
# 读取excel文档

wb = openpyxl.load_workbook('openpyxl.xlsx')
sheet = wb['Sheet1']
playload = {"fpdm":str(sheet['A2'].value)}
print(playload)


