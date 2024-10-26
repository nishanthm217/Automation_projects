from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

from baseclass import Test_baseClass
from pageObjRevising.FinalCheckOutPage import Test_FinalCheckOut
from pageObjRevising.checkOutPage import Test_CheckOutPage
from pageObjRevising.homepage import Test_homePage
from pageObjRevising.productPage import Test_productPage


class Test_executable(Test_baseClass):
    def test_mainMethod(self):
        homepageclick = Test_homePage(self.driver)
        homepageclick.shopItems().click()

        productPageGet = Test_productPage(self.driver)
        products_Get = productPageGet.test_productSelect()

        for product_select in products_Get:
            ProductName = product_select.find_element(By.XPATH, 'div/h4/a').text
            if (ProductName == "iphone X") or (ProductName == "Blackberry"):
                time.sleep(2)
                product_select.find_element(By.XPATH, 'div/button').click()

        productCartSend = Test_CheckOutPage(self.driver)
        productCartSend.test_cartReturn().click()


        # self.driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()
        finalCheckSend = Test_CheckOutPage(self.driver)
        finalCheckSend.test_finalCheckClick().click()

        # self.driver.find_element(By.XPATH, '//input[@id="country"]').send_keys("ind")
        Send_keys_send = Test_FinalCheckOut(self.driver)
        Send_keys_send.FinalCheckOut()

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//div[@class="suggestions"]')))

        #self.driver.find_elements(By.XPATH, '//div[@class="suggestions"]')
        finalDropdownsend = Test_FinalCheckOut(self.driver)
        finalDropdownsend.preFinalDropdown()

        #self.driver.find_element(By.LINK_TEXT, 'India').click()
        clickFinalInd = Test_FinalCheckOut(self.driver)
        clickFinalInd.clickDropInd()

        #self.driver.find_element(By.XPATH, '//a[@style="cursor: pointer;color: #1d1dfb; text-decoration: underline;"]').click()
        clickTickBOX = Test_FinalCheckOut(self.driver)
        clickTickBOX.fclickTickBox()

        #self.driver.find_element(By.XPATH, '//button[@class="btn btn-info"]').click()
        closefpop = Test_FinalCheckOut(self.driver)
        closefpop.test_closePop()


        #self.driver.find_element(By.XPATH, '//input[@class="btn btn-success btn-lg"]').click()
        finalClickF = Test_FinalCheckOut(self.driver)
        finalClickF.test_clickSubmit()

        fsuccessText = Test_FinalCheckOut(self.driver)
        successText = fsuccessText.test_getSuccessMsg()
        #self.driver.find_element(By.XPATH, '//div[@class="alert alert-success alert-dismissible"]').text
        assert "Success! Thank you!" in successText
        print(successText)

