from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Test_productPage:
    def __init__(self,driver):
        self.driver = driver

    #self.driver.find_elements(By.XPATH, '//div[@class="card h-100"]')
    productChoose = (By.XPATH, '//div[@class="card h-100"]')

    def test_productSelect(self):
        return self.driver.find_elements(*Test_productPage.productChoose)
