from selenium import webdriver
from Page.login import Login
from common.read_excle import Cell
from common.getjson import GetJson
class Test_Login():
    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://pro.mophone.net/auth/authentication/login?cid=merryyou2")
        self.table=Cell('测试数据.xls', '首页用例')
    def test_login(self):
        Login.login(self.driver,GetJson.getJson(Cell.getcellvalue(self.table, 1, '参数'),'username'),
                    GetJson.getJson(Cell.getcellvalue(self.table, 1, '参数'),'password'))
        txt=self.driver.find_element_by_xpath('//span[@class="userName"]').text
        assert txt=='孙方娟'
    def test_register(self):
        Login.register(self.driver,'用户注册')
        assert self.driver.title=='用户注册'
    def test1(self):
        print(Cell.getcellvalue(self.table, 1, '参数'))
        cell_dict=json.loads(Cell.getcellvalue(self.table, 1, '参数'))
        print(cell_dict['username'])
    def test2(self):
        pass