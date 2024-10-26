from selenium.webdriver.common.by import By

class Test_homePage:
    shop = (By.LINK_TEXT, "Shop")

    def __init__(self,driver):
        self.driver = driver

    def test_shopItems(self):
        return self.driver.find_element(*Test_homePage.shop)

