import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    def test_search_in_google(self):
        self.driver.get("https://google.com")
        # time.sleep(5)
        self.driver.find_element_by_name('q').send_keys("search selenium")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name('btnK').click()

    def test_sarthik(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Sarthik")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_name('btnK1').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Sarthik B/PycharmProjects/SeleniumYoutube/Reports'))