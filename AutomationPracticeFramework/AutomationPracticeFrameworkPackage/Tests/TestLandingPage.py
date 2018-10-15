from AutomationPracticeFrameworkPackage.EnvironmentSetup.EnvSetup import EnvSetup
from AutomationPracticeFrameworkPackage.Pages.LandingPage import LandingPage

#from AutomationPracticeFrameworkPackage.EnvironmentSetup.EnvSetup import EnvSetup
#from AutomationPracticeFrameworkPackage.Pages.LandingPage import LandingPage
import unittest


class AutomationPracticeLandingPage(EnvSetup):
    def test_home_page(self):

        driver = self.driver
        self.driver.get('http://www.automationpractice.com')

    #test_home_page()
    lp = LandingPage(driver)
    lp.click_sign_in()

if __name__ == '__main__':
        unittest.main()



