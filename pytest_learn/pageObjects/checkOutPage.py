from selenium.webdriver.common.by import By


class Test_CheckOutPage:

    def __init__(self,driver):
        self.driver = driver

    cardTitle = (By.XPATH, '//div[@class="card h-100"]')
    # self.driver.find_elements(By.XPATH,'//div[@class="card h-100"]')

    primaryButton = (By.XPATH,'//a[@class="nav-link btn btn-primary"]')
    # self.driver.find_element(By.XPATH,'//a[@class="nav-link btn btn-primary"]')

    successButton = (By.XPATH, '//button[@class="btn btn-success"]')
    # self.driver.find_element(By.XPATH,'//button[@class="btn btn-success"]').click()


    def test_cardTitle(self):
        return self.driver.find_elements(*Test_CheckOutPage.cardTitle)

    def test_primaryButton(self):
        return self.driver.find_element(*Test_CheckOutPage.primaryButton)

    def test_successButton(self):
        return self.driver.find_element(*Test_CheckOutPage.successButton)