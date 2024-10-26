from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://amazon.in")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//input[@id="twotabsearchtextbox"]').send_keys("Mobile")
driver.find_element(By.XPATH,'//input[@id="nav-search-submit-button"]').click()
Samsung_products = driver.find_elements(By.XPATH,"//span[contains(text(), 'Samsung')]")

for mobile in Samsung_products:
    mobile.find_element(By.XPATH,'')
