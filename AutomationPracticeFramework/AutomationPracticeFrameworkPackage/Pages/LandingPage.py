from AutomationPracticeFrameworkPackage.EnvironmentSetup.EnvSetup import EnvSetup
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By


class LandingPage(object):

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome()
        #self.sign_in = self.driver.find_element_by_class_name('login')

        self.sign_in = driver.find_element(By.CLASS_NAME, 'login')


    def click_sign_in(self):
        self.sign_in.click()

