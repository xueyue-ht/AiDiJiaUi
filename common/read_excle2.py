from excle_utils import ExcleUtils
excle=ExcleUtils('../data/test.xlsx', '合并测试')
col=excle.sheet.row_values(0)
excle_data_list=[]
# dict[col[0]]=excle.get_cellvalue(1,0)
for rows in range(1,excle.get_row_count()):
    dict = {}
    for length in range(excle.get_col_count()):
        dict[col[length]] = excle.get_cellvalue(rows, length)
    excle_data_list.append(dict)
# print(excle_data_list)
testdata={}
for data in excle_data_list:
    testdata.setdefault(data['名称'],[]).append(data)
# print(testdata)
for key,value in testdata.items():
    dict={}
    dict['名称']=key
    dict['步骤']=value
    print(dict)
