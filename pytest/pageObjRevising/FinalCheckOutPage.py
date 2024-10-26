from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class Test_FinalCheckOut:
    def __init__(self,driver):
        self.driver = driver

    # self.driver.find_element(By.XPATH, '//input[@id="country"]').send_keys("ind")
    finalPage = (By.XPATH, '//input[@id="country"]')

    #self.driver.find_elements(By.XPATH, '//div[@class="suggestions"]')
    findDropdown = (By.XPATH, '//div[@class="suggestions"]')

    #self.driver.find_element(By.LINK_TEXT, 'India').click()
    clickInd = (By.LINK_TEXT, 'India')

    #self.driver.find_element(By.XPATH, '//a[@style="cursor: pointer;color: #1d1dfb; text-decoration: underline;"]').click()
    clickTickBox = (By.XPATH, '//a[@style="cursor: pointer;color: #1d1dfb; text-decoration: underline;"]')

    #self.driver.find_element(By.XPATH, '//button[@class="btn btn-info"]').click()
    closePop = (By.XPATH, '//button[@class="btn btn-info"]')

    #self.driver.find_element(By.XPATH, '//input[@class="btn btn-success btn-lg"]').click()
    clickSubmit = (By.XPATH, '//input[@class="btn btn-success btn-lg"]')

    #self.driver.find_element(By.XPATH, '//div[@class="alert alert-success alert-dismissible"]').text
    getSuccessMsg = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')

    def FinalCheckOut(self):
        return self.driver.find_element(*Test_FinalCheckOut.finalPage).send_keys("ind")

    def preFinalDropdown(self):
        return self.driver.find_elements(*Test_FinalCheckOut.findDropdown)

    def clickDropInd(self):
        return self.driver.find_element(*Test_FinalCheckOut.clickInd).click()

    def fclickTickBox(self):
        return self.driver.find_element(*Test_FinalCheckOut.clickTickBox).click()

    def test_closePop(self):
        return self.driver.find_element(*Test_FinalCheckOut.closePop).click()

    def test_clickSubmit(self):
        return self.driver.find_element(*Test_FinalCheckOut.clickSubmit).click()

    def test_getSuccessMsg(self):
        return self.driver.find_element(*Test_FinalCheckOut.getSuccessMsg).text