from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
derived_list =[]
expected_list = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']

driver.find_element(By.XPATH,'//form/input[@class="search-keyword"]').send_keys("ber")
product_names = driver.find_elements(By.XPATH,'//div[@class="products"]/div/h4')
for product_name in product_names:
    print(product_name)
time.sleep(3)
