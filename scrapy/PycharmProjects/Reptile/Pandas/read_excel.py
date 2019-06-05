import xlrd

# f = open('C:/Users/Administrator/Desktop/ex.xlsx', 'r', encoding= 'utf-8')
#
#
#
# print(f.read())

excel_file = xlrd.open_workbook('C:/Users/Administrator/Desktop/test.xlsx')

print(excel_file.sheet_names())

sheet = excel_file.sheet_by_index(0)

print(sheet.name, sheet.nrows, sheet.ncols)

cols = sheet.col_values(1)
rows = sheet.row_values(1)
print(cols, rows)

print(sheet.cell(1, 1).ctype)

for col in cols:
    print(col)