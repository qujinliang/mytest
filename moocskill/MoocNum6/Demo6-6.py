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

# 设置写入内容的样式
style = xlwt.easyxf('align: vertical center, horizontal center')

# 遍历读取表格的行数次, 再遍历读取表格的列数次
# 写入行列坐标位置，内容，和样式
for r in range(rsheet.nrows):
    for c in range(rsheet.ncols):
        wsheet.write(r,c,rsheet.cell_value(r,c),style)

wbook.save('output.xls')