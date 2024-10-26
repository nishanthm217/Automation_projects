from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(1)
countries = driver.find_elements(By.CSS_SELECTOR,'li[class="ui-menu-item"] a')
print(len(countries))

for country in countries:
    if country.text =="India":
        country.click()
        break

time.sleep(3)
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") =="India"
