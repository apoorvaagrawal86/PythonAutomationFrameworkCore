from selenium import webdriver
import unittest


class EnvSetup(unittest.TestCase):

    #def __init__(self):
        #self.driver = webdriver.Chrome()

    def setup(self):
        self.driver = webdriver.Chrome('C:\Personal\HTML-CSS\Python\chromedriver.exe')
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
