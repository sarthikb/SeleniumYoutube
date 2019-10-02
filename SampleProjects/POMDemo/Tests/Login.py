import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import HtmlTestRunner
from SampleProjects.POMDemo.Pages.LogonPage import LogonPage
from SampleProjects.POMDemo.Pages.homePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get('https://opensource-demo.orangehrmlive.com')
        Login = LogonPage(driver)
        Login.enter_username("Admin")
        Login.enter_password("admin123")
        Login.click_login()

        homePage = HomePage(driver)
        homePage.clickWelcome()
        homePage.clickLogout()

        driver.get('https://opensource-demo.orangehrmlive.com')
        #self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        #self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        #self.driver.find_element_by_id('btnLogin').click()
        #time.sleep(2)
        #self.driver.find_element_by_id('welcome').click()
        #self.driver.find_element_by_link_text('Logout').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()



if __name__ == '__main__' :
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Sarthik B/PycharmProjects/SeleniumYoutube/Reports'))








