from common.read_excle import Cell
import xlrd
import os
from datetime import datetime
from xlrd import xldate_as_tuple
import random
class TestCell():
    def test_getcell(self):
        table=Cell.gettable('测试数据.xls', '首页用例')
        colindex=Cell.getColumnIndex(table,'参数')
        cell=Cell.getcell(table,1,colindex)
        print(cell)
    def test1(self):
        excel_path = os.path.join(os.getcwd(), 'OPE费用流水管理.xlsx')  # Excel文件路径
        excel_file = xlrd.open_workbook(excel_path)
        table=excel_file.sheets()[0]
        print("总行数：" + str(table.nrows))
        print("总列数：" + str(table.ncols))
        for i in range(table.ncols):
            if(table.cell_value(0, i) == '参数'):
                columnIndex = i
                break
        print(columnIndex)
        print(table.cell_type(0, 7))

