from selenium import webdriver
class GetElement():
    @staticmethod
    def by_xpath(driver:webdriver.Chrome,xpath):
        ele=driver.find_element_by_xpath(xpath)
        return ele

    @staticmethod
    def by_id(driver:webdriver.Chrome,id):
        ele=driver.find_element_by_id(id)
        return ele

    @staticmethod
    def by_css(driver:webdriver.Chrome,css):
        ele=driver.find_element_by_css_selector(css)
        return ele

    @staticmethod
    def by_linkname(driver:webdriver.Chrome,linkname):
        ele=driver.find_element_by_link_text(linkname)
        return ele

    @staticmethod
    def by_classname(driver:webdriver.Chrome,classname):
        ele=driver.find_element_by_class_name(classname)
        return ele

    @staticmethod
    def by_tagname(driver:webdriver.Chrome,tagname):
        ele=driver.find_element_by_tag_name(tagname)
        return ele