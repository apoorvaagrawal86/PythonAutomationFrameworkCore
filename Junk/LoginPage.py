from selenium import webdriver

driver = webdriver.Chrome('C:\Personal\HTML-CSS\Python\Project\chromedriver.exe')


class LandingPage:

    def open_url(self, url):
        driver.get(url)

    def click(self, ids):
        driver.click(ids)

    def click_class_name(self, classnames):
        driver.click(classnames)

    def enter_text(self, text):
        driver.send_keys(text)

    def find_element(self, ids):
        driver.find_element_by_id(ids)

    def find_element_by_class_name(self, classnames):
        driver.find_element_by_class_name(classnames)

