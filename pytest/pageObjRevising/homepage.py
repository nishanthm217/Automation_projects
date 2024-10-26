import pytest
from selenium.webdriver.common.by import By


class Test_homePage:

    def __init__(self,driver):
        self.driver = driver

    shop = (By.LINK_TEXT, 'Shop')
    #self.driver.find_element(By.LINK_TEXT, 'Shop').click()

    def shopItems(self):
        return self.driver.find_element(*Test_homePage.shop)
