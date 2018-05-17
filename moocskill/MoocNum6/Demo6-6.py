import xlwt,xlrd

'''
读取excel，并新增一行，然后写入到新的excel文档
'''

rbook = xlrd.open_workbook('report-2018-03-09.xls',encoding_override='utf8')
rsheet = rbook.sheet_by_index(0)

nc = rsheet.ncols
print(nc)
rsheet.put_cell(0,nc,xlrd.XL_CELL_TEXT,'新增',None)

for row in range(1,rsheet.nrows):
    t = rsheet.row_values(row,3,4)
    print(t)
    rsheet.put_cell(row,nc,xlrd.XL_CELL_TEXT,t,None)


wbook = xlwt.Workbook()
wsheet = wbook.add_sheet(rsheet.name)
style = xlwt.easyxf('align: vertical center, horizontal center')

for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r,c,rsheet.cell_value(r,c),style)

wbook.save('output.xls')