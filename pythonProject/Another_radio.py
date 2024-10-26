from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radios = driver.find_elements(By.CSS_SELECTOR,'.radioButton')
radios[1].click()
assert radios[1].is_selected()

time.sleep(2)

#Clicking the hide boxes
driver.find_element(By.ID,'hide-textbox').click()
assert not driver.find_element(By.ID,'displayed-text').is_displayed()

time.sleep(2)