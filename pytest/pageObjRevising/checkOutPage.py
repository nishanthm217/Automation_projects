from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class Test_CheckOutPage:
    def __init__(self,driver):
        self.driver = driver

    cartClick = (By.XPATH, '//a[@class="nav-link btn btn-primary"]')
    #self.driver.find_element(By.XPATH, '//a[@class="nav-link btn btn-primary"]').click()


    finalCheckClick = (By.XPATH, '//button[@class="btn btn-success"]')
    #self.driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()

    def test_cartReturn(self):
        return self.driver.find_element(*Test_CheckOutPage.cartClick)

    def test_finalCheckClick(self):
        return self.driver.find_element(*Test_CheckOutPage.finalCheckClick)