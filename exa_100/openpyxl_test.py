import openpyxl
import xlwt,xlrd
# 读取excel文档

wb = openpyxl.load_workbook('openpyxl.xlsx')
sheet = wb['Sheet1']
# print(dir(sheet))
# print(help(sheet))
l = []
for row in sheet.rows:
    for cell in row:
        l.append(cell.value)
    print(l)





playload = {"fpdm":str(sheet.cell(column=1,row=2).value), "fphm":str(sheet['B2'].value), "fplx":str(sheet['C2'].value),
            "fpje":str(sheet['D2'].value)}
print(playload)


