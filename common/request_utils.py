import requests
from common.config_utils import ConfigUitls
from common.testdata_utils import TestdataUtils
class Request_Utils():
    def __init__(self):
        config=ConfigUitls()
        self.host=config.HOSTS
        self.testdata=TestdataUtils('接口用例数据.xlsx','接口测试')
    def request(self):
        for i in range(self.testdata.excle.get_row_count()):
            if self.testdata.conversion()[i]['casestep'][0]['请求方法'] == 'get':
                result = self.__get_request()
                return result
            elif self.testdata.conversion()[i]['casestep'][0]['请求方法'] == 'post':
                result = self.__post_request()
                return result
            else:
                return '请求方法不存在'

    def __get_request(self):
        url=self.host+self.testdata.conversion()[0]['casestep'][0]['请求地址']
        params=self.testdata.conversion()[0]['casestep'][0]['请求参数（get）']
        result=requests.get(url,params=params).json()
        return result
    def __post_request(self):
        url = self.host + self.testdata.conversion()[0]['casestep'][0]['请求地址']
        params = self.testdata.conversion()[0]['casestep'][0]['请求参数（get）']
        data=self.testdata.conversion()[0]['casestep'][0]['请求参数（post）']
        result = requests.get(url, params=params,data=data).json()
        return result

if __name__=='__main__':
    req = Request_Utils()
    print(req.request())