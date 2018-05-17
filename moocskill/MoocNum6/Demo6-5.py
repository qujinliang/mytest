import xlrd,xlwt

book = xlrd.open_workbook('report-2018-03-09.xls',encoding_override='utf8')
sheet = book.sheet_by_index(0)
row_count = sheet.nrows
col_count = sheet.ncols
print(row_count,col_count)

# 获取一个单元格
cell = sheet.cell(0,0)
print(cell.value)

print(cell.ctype)
print(xlrd.XL_CELL_TEXT)
print(dir(cell.ctype))

# 获取一行
j = 0
while j > row_count:
    row = sheet.row_values(j)
    j +=1
    print(row)

# 获取一列
i = 0
print('一列%s' %sheet.col_values(1))
while i > col_count:
    cells = sheet.col_values(i,1)
    i+=1
    print(cells)


# 添加一个单元格
sheet.put_cell(0,12,2,'hello',None)

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet('sheet1')
wsheet.write(0,0,'hello')

wbook.save('output.xls')