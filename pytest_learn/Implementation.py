from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from baseclass import Test_baseclass
from pageObjects.checkOutPage import Test_CheckOutPage
from pageObjects.finalpageOrder import Test_finalPageOrder
from pageObjects.homePage import Test_homePage

class Test_implementation(Test_baseclass):
    def test_executable(self):
        homepage = Test_homePage(self.driver)
        homepage.test_shopItems().click()
        checkOutPage = Test_CheckOutPage(self.driver)
        products_Get = checkOutPage.test_cardTitle()

        for product_select in products_Get:
            ProductName = product_select.find_element(By.XPATH,'div/h4/a').text
            if (ProductName =="iphone X") or (ProductName == "Blackberry"):
                product_select.find_element(By.XPATH,'div/button').click()

        checkOutPage.test_primaryButton().click()
        checkOutPage.test_successButton().click()
        finalPageOrder = Test_finalPageOrder(self.driver)
        finalPageOrder.test_keysSendInd().send_keys("ind")
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//div[@class="suggestions"]')))
        finalPageOrder.test_dropdownChoose()
        finalPageOrder.test_linkTextChoose().click()
        finalPageOrder.test_termBoxClick().click()
        finalPageOrder.test_checkBoxClick().click()

        finalPageOrder.test_finalSubmitButton().click()
        successText = finalPageOrder.test_resultFetch().text
        assert "Success! Thank you!" in successText
        print(successText)
