import xlrd
import os

currentpath=os.path.dirname(__file__)
filepath=os.path.join(currentpath, '../data/test.xlsx')
workbook=xlrd.open_workbook(filepath)
table=workbook.sheet_by_name('合并测试')
mergedcells=table.merged_cells
print(mergedcells)
row=1;col=0
for (rowmin,rowmax,colmin,colmax) in mergedcells:
    if row>=rowmin and row<rowmax:
        if col>=colmin and col<colmax:
            cellvalue=table.cell_value(rowmin,colmin)
        else:
            cellvalue = table.cell_value(row, col)
    else:
        cellvalue=table.cell_value(row,col)
print(cellvalue)