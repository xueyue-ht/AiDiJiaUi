from selenium import webdriver
from common.getelement import GetElement
class CustomerManagement():
    @staticmethod
    def addclue(driver:webdriver.Chrome,):
        driver.find_element_by_link_text('客户管理').click()
        driver.find_element_by_link_text('客户线索').click()