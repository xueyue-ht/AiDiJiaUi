import xlrd
import os
import logging
from datetime import datetime
from xlrd import xldate_as_tuple
'''
python读取excel中单元格的内容返回的5种类型
0 --empty：空
1 --string：字符串
2 --number：数字
3 --date：日期
4 --boolean：布尔
5 --error
'''
class Cell():
    table=None
    def __init__(self,filename,sheets_name):
        excel_path = os.path.join(os.getcwd(), filename)
        excel_file = xlrd.open_workbook(excel_path)
        self.table=excel_file.sheet_by_name(sheets_name)
    # filename,sheets_index,colname,number
    # def gettable(self,filename,sheets_name):
    #     # 打开Excel文件
    #     excel_path = os.path.join(os.getcwd(), filename)  # Excel文件路径
    #     excel_file = xlrd.open_workbook(excel_path)
    #     # table = excel_file.sheet_by_index(1)                  # 通过索引打开
    #     # table = excel_file.sheet_by_name('mode')              # 通过名字打开
    #     table = excel_file.sheet_by_name(sheets_name)  # 通过索引打开
    #     return table

    def getColumnIndex(self, columnName):
        columnIndex=0
        for i in range(self.table.ncols):
            if(self.table.cell_value(0, i) == columnName):
                columnIndex = i
                break
        return columnIndex

    def getcell(self,number,columnIndex):
        cell=self.table.cell_value(number,columnIndex)
        Cell.cell_format(self.table,number,columnIndex)
        return cell

    def cell_format(self,number,columnIndex):
        cell_value=None
        ctype = self.table.cell_type(number,columnIndex)
        if ctype == 2 and cell % 1 == 0:  # 是否是数字类型
            cell_value = int(self.table.cell_value(number,columnIndex))
        elif ctype == 3:  # 是否是日期
            date = datetime(*xldate_as_tuple(self.table.cell_value(number,columnIndex), 0))
            cell_value = date.strftime('%Y/%m/%d %H:%M:%S')
        elif ctype == 4:  # 是否是布尔类型
            cell_value = True if cell == 1 else False
        return  cell_value

    def getallcells(self):
        all_content = []
        for i in range(self.table.nrows):
            row_content = []
            for j in range(self.table.ncols):
                ctype = self.table.cell_type(i, j)          # 获取单元格返回的数据类型
                logging.info(ctype)
                cell_value = self.table.cell_value(i, j)         # 获取单元格内容
                logging.info(cell_value)
                if ctype == 2 and cell_value % 1 == 0:      # 是否是数字类型
                    cell_value = int(cell_value)
                elif ctype == 3:                            # 是否是日期
                    date = datetime(*xldate_as_tuple(cell_value, 0))
                    cell_value = date.strftime('%Y/%m/%d %H:%M:%S')
                elif ctype == 4:                            # 是否是布尔类型
                    cell_value = True if cell_value == 1 else False
                row_content.append(cell_value)
            all_content.append(row_content)
        return all_content
    def getcellvalue(self,number,colname):
        colindex = Cell.getColumnIndex(self.table, colname)
        cell = Cell.getcell(self.table, number, colindex)
        return cell