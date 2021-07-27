from selenium import webdriver
from Page.getelement import GetElement
class Login():
    @staticmethod
    def login(driver:webdriver.Chrome,username,password):
        # 访问爱迪家pro管理后台
        # 输入账户名密码
        GetElement.by_xpath(driver,'//input[@id="userName"]').send_keys(username)
        GetElement.by_xpath(driver,'//*[@id="password"]').send_keys(password)
        GetElement.by_xpath(driver,'//button[@lay-filter="login"]').click()
    def register(self,driver:webdriver.Chrome,linkname):
        GetElement.by_linkname(linkname).click()