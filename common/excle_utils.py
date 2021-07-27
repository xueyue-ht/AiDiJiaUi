import xlrd

class ExcleUtils():
    def __init__(self,filepath,sheetname):
        self.filepath=filepath
        self.sheetname=sheetname
        self.sheet=self.get_sheet()
    def get_sheet(self):
        #获取表格对象
        workbook=xlrd.open_workbook(self.filepath)
        sheet=workbook.sheet_by_name(self.sheetname)
        return sheet
    def get_row_count(self):
        row_count=self.sheet.nrows
        return row_count
    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count
    def get_cellvalue(self,row,col):
        mergedcells=self.sheet.merged_cells
        for (rowmin, rowmax, colmin, colmax) in mergedcells:
            if row >= rowmin and row < rowmax:
                if col >= colmin and col < colmax:
                    cellvalue = self.sheet.cell_value(rowmin, colmin)
                    break
                else:
                    cellvalue = self.sheet.cell_value(row, col)
            else:
                cellvalue = self.sheet.cell_value(row, col)
        return  cellvalue
    def get_allcellbvalue(self):
        col = self.sheet.row_values(0)
        excle_data_list = []
        # dict[col[0]]=excle.get_cellvalue(1,0)
        for rows in range(1, self.get_row_count()):
            dict = {}
            for length in range(self.get_col_count()):
                dict[col[length]] = self.get_cellvalue(rows, length)
            excle_data_list.append(dict)
        return excle_data_list
if __name__=='__main__':
    excle=ExcleUtils('test.xlsx','合并测试')
    print(excle.get_allcellbvalue())

