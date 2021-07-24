from selenium import webdriver
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Testcase:
    def setup(self):
        # option=webdriver.ChromeOptions
        # option.debugger_address='127.0.0.1:9888'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)


    def testcase1(self):
        # 访问爱迪家pro管理后台
        self.driver.get("http://192.168.60.234:8081/idea-home/")
        # 提交用户线索
        # 输入账户名密码
        self.driver.find_element_by_xpath('//input[@id="userName"]').send_keys(15116129152)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(15116129152)
        self.driver.find_element_by_xpath('//button[@lay-filter="login"]').send_keys(Keys.ENTER)
        # el=self.driver.find_element_by_xpath('//button[@lay-filter="login"]')
        # self.driver.execute_script('arguments[0].click;',el)
        sleep(5)
        # 点击客户管理添加线索
        # self.driver.find_element_by_xpath('//cite[text()="客户管理"]').send_keys(Keys.ENTER)
        # self.driver.find_element_by_xpath('//cite[text()="客户线索"]').send_keys(Keys.ENTER)
        self.driver.find_element_by_link_text('客户管理').click()
        self.driver.find_element_by_link_text('客户线索').click()
        # 新增客户线索，填写对应资料
        # 跳转到对应的iframe,给予sleep，加载页面元素完成

        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="div_frames"]/div[2]/iframe'))
        self.driver.find_element_by_xpath('//a[text()="新增客户线索"]').click()
        # driver.find_element_by_xpath('//a[text()="新增客户线索"]').click()
        # 切换frame
        self.driver.switch_to.frame("layui-layer-iframe100001")
        # 创建select下拉实例化，并选取对应值
        # 选择所属公司
        s1 = Select(self.driver.find_element_by_id('groupBranchId'))
        s1.select_by_value("125")
        # 填写用户姓名
        self.driver.find_element_by_xpath('//input[@placeholder="客户姓名"]').send_keys('黄涛测试1')
        # 填写地址
        self.driver.find_element_by_xpath('//input[@placeholder="如：A区1栋1单元101号"]').send_keys('长沙岳麓区')
        # 填写电话号码
        self.driver.find_element_by_xpath('//input[@name="mobile"]').send_keys('17900000007')
        # 期房现房选择,使用兄弟节点进行定位
        # driver.find_element_by_xpath('//input[@name="mobile"]').send_keys('17700000015')
        # s2=Select(driver.find_element_by_xpath('//select[@id="deliveryType"]'))
        # s2.select_by_value("20")
        self.driver.find_element_by_xpath('//select[@id="deliveryType"]//..//div[1]//div[1]').click()
        self.driver.find_element_by_xpath('//select[@id="deliveryType"]//..//div[1]//dl[1]//dd[2]').click()
        # 预计装修时间
        self.driver.find_element_by_xpath('//select[@id="estimateDecoreteDateType"]//..//div[1]//div[1]').click()
        self.driver.find_element_by_xpath('//select[@id="estimateDecoreteDateType"]//..//div[1]//dl[1]//dd[2]').click()
        # 预计装修金额
        self.driver.find_element_by_xpath('//select[@id="budgetAmountType"]//..//div[1]//div[1]').click()
        self.driver.find_element_by_xpath('//select[@id="budgetAmountType"]//..//div[1]//dl[1]//dd[2]').click()
        # s3=Select(driver.find_element_by_id("budgetAmountType"))
        # s3.select_by_value("100")
        # 房屋面积
        self.driver.find_element_by_xpath('//input[@name="houseArea"]').send_keys('172')
        # 所属门店
        self.driver.find_element_by_xpath('//select[@id="storeId"]//..//div[1]//div[1]').click()
        self.driver.find_element_by_xpath('//select[@id="storeId"]//..//div[1]//dl[1]//dd[2]').click()
        # s4=Select(driver.find_element_by_id("storeId"))
        # s4.select_by_value("127")
        # 预计上门时间
        self.driver.find_element_by_xpath('//input[@name="estimateComeDate"]').click()
        self.driver.find_element_by_xpath('//input[@name="estimateComeDate"]').send_keys("2021-05-24 00:00:00")
        # 客户来源
        self.driver.find_element_by_xpath('//select[@id="sourceId"]//..//div[1]//div[1]').click()
        self.driver.find_element_by_xpath('//select[@id="sourceId"]//..//div[1]//dl[1]//dd[8]').click()
        # s6=Select(driver.find_element_by_id("sourceId"))
        # s6.select_by_value("7")
        # 交房时间
        self.driver.find_element_by_xpath('//input[@name="deliveryDate"]').click()
        self.driver.find_element_by_xpath('//input[@name="deliveryDate"]').send_keys("2021-05-04 00:00:00")
        # 客户上门分类
        self.driver.find_element_by_xpath('//select[@id="designLevel"]//..//div[1]//div[1]').click()
        self.driver.find_element_by_xpath('//select[@id="designLevel"]//..//div[1]//dl[1]//dd[2]').click()
        # s5=Select(driver.find_element_by_id("designLevel"))
        # s5.select_by_value("1")
        # 提交店长
        # driver.find_element_by_xpath('//button[text()="提交店长"]').click()







