import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
import time


class SampleTeseCase(unittest.TestCase):

    def setUp(self):
        # open Firefox browser
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome()  

        # maximize the window size
        self.driver.maximize_window()
        # delete the cookies
        self.driver.delete_all_cookies()
        # navigate to the url
        self.driver.get('http://localhost:3000/')

    def test_BMI(self):
        # Insert inputs
        self.weight = self.driver.find_element(
            By.XPATH, '//*[@id="weight"]')
        
        self.weight.clear()
        self.weight.send_keys(100)

        self.height = self.driver.find_element(
            By.XPATH, '//*[@id="height"]')
        
        self.height.clear()
        self.height.send_keys(200)

        # find button and click
        self.submitBtn = self.driver.find_element(
            By.XPATH, '//*[@id="bmi-btn"]')
        self.submitBtn.click()

        # find claculated BMI
        time.sleep(2)
        self.bmi = self.driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div/div[4]/div[2]/div[1]/div/div/span').text.split(':')[1]

        self.assertTrue('25.00' in self.bmi)

    def tearDown(self):
        self.driver.close()
        # print('exit')


if __name__ == "__main__":
    unittest.main()
