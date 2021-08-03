from excle_utils import ExcleUtils
import os


class TestdataUtils():
    def __init__(self,filename,sheetname):
        currentpath = os.path.dirname(__file__)
        filepath = os.path.join(currentpath,'..','data',filename )
        self.excle=ExcleUtils(filepath,sheetname)
    def conversion(self):
        '''转化数据格式
        由[{a:b},{a:b}]转为{a:[{},{}],b:[{}]}格式
        '''
        dict1={}
        for data in self.excle.get_allcellvalue():
            dict1.setdefault(data['用例编号'],[]).append(data)
        '''转化数据格式为
        [{a:b,c:[{d:e}]}]
        '''
        datalist=[]
        for key,value in dict1.items():
            dict2 = {}
            dict2['caseid']=key
            dict2['casestep']=value
            datalist.append(dict2)
        return datalist
if __name__=='__main__':
    test=TestdataUtils('接口用例数据.xlsx','接口测试')
    print(test.conversion()[0]['casestep'][0]['请求地址'])
    # print(test.get_allcellvalue())


