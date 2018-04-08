import openpyxl
# 读取excel文档

wb = openpyxl.load_workbook('openpyxl.xlsx')
sheet = wb['Sheet1']
playload = {"fpdm":str(sheet['A2'].value), "fphm":str(sheet['B2'].value), "fplx":str(sheet['C2'].value),
            "fpje":(lambda x:"" if str(sheet['D2'].value) == 'None' else "")}
print(playload)


