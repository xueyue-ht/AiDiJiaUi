from excle_utils import ExcleUtils
excle=ExcleUtils('test.xlsx','合并测试')
col=excle.sheet.row_values(0)
excle_data_list=[]
# dict[col[0]]=excle.get_cellvalue(1,0)
for rows in range(1,excle.get_row_count()):
    dict = {}
    for length in range(excle.get_col_count()):
        dict[col[length]] = excle.get_cellvalue(rows, length)
    excle_data_list.append(dict)
print(excle_data_list)
