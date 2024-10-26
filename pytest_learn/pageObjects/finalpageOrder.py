from selenium.webdriver.common.by import By

class Test_finalPageOrder:

    def __init__(self,driver):
        self.driver = driver

    keySend = (By.XPATH,'//input[@id="country"]')
    #self.driver.find_element(By.XPATH,'//input[@id="country"]').send_keys("ind")

    dropdownChoose = (By.XPATH,'//div[@class="suggestions"]')
    #self.driver.find_elements(By.XPATH,'//div[@class="suggestions"]')

    linkTestChoose = (By.LINK_TEXT,'India')
    #self.driver.find_element(By.LINK_TEXT,'India').click()

    termBoxClick = (By.XPATH,'//a[@style="cursor: pointer;color: #1d1dfb; text-decoration: underline;"]')
    #self.driver.find_element(By.XPATH,'//a[@style="cursor: pointer;color: #1d1dfb; text-decoration: underline;"]').click()

    checkBoxClick = (By.XPATH,'//button[@class="btn btn-info"]')
    #self.driver.find_element(By.XPATH,'//button[@class="btn btn-info"]').click()

    finalSubmitButton = (By.XPATH,'//input[@class="btn btn-success btn-lg"]')
    #self.driver.find_element(By.XPATH,'//input[@class="btn btn-success btn-lg"]').click()

    resultFetch = (By.XPATH,'//div[@class="alert alert-success alert-dismissible"]')
    #self.driver.find_element(By.XPATH,'//div[@class="alert alert-success alert-dismissible"]').text

    def test_keysSendInd(self):
        return self.driver.find_element(*Test_finalPageOrder.keySend)

    def test_dropdownChoose(self):
        return self.driver.find_elements(*Test_finalPageOrder.dropdownChoose)

    def test_linkTextChoose(self):
        return self.driver.find_element(*Test_finalPageOrder.linkTestChoose)

    def test_termBoxClick(self):
        return self.driver.find_element(*Test_finalPageOrder.termBoxClick)

    def test_checkBoxClick(self):
        return self.driver.find_element(*Test_finalPageOrder.checkBoxClick)

    def test_finalSubmitButton(self):
        return self.driver.find_element(*Test_finalPageOrder.finalSubmitButton)

    def test_resultFetch(self):
        return self.driver.find_element(*Test_finalPageOrder.resultFetch)
