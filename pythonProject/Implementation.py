from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

@pytest.mark.usefixtures("test_calling")
class Test_implementationClass():
    self.driver.find_element(By.LINK_TEXT, 'Shop').click()
    total_phones = driver.find_elements(By.XPATH, '//div[@class="card h-100"]')

    for phone in total_phones:
        phoneName = phone.find_element(By.XPATH, 'div/h4/a').text
        if phoneName == "Blackberry":
            time.sleep(2)
            phone.find_element(By.XPATH, "div/button").click()

    driver.find_element(By.XPATH, '//a[@class="nav-link btn btn-primary"]').click()
    driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()
    driver.find_element(By.XPATH, '//input[@id="country"]').send_keys("Ind")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located((By.XPATH, '//div[@class="suggestions"]')))
    gotCountries = driver.find_elements(By.XPATH, '//div[@class="suggestions"]')
    for country in gotCountries:
        countryName = country.find_element(By.XPATH, 'ul/li/a').text
        print(countryName)
        if countryName == "India":
            country.find_element(By.XPATH, 'ul/li/a').click()

    driver.find_element(By.XPATH, '//label[@for="checkbox2"]').click()
    driver.find_element(By.XPATH, '//input[@class="btn btn-success btn-lg"]').click()
    successmsg = driver.find_element(By.XPATH, '//div[@class="alert alert-success alert-dismissible"]').text
    print(successmsg)
    time.sleep(2)