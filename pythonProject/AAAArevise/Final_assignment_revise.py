from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//a[text()="Shop"]').click()
products_get = driver.find_elements(By.XPATH,'//div[@class="card h-100"]')
time.sleep(1)
for product_choose in products_get:
    product_nameG = product_choose.find_element(By.XPATH,'div/h4/a').text
    time.sleep(1)
    if (product_nameG == "iphone X") or (product_nameG=="Samsung Note 8") or (product_nameG=="Nokia Edge"):
        product_choose.find_element(By.XPATH,'div[2]/button').click()
        time.sleep(1)

driver.find_element(By.XPATH,'//a[@class="nav-link btn btn-primary"]').click()
driver.find_element(By.XPATH,'//button[@class="btn btn-success"]').click()
driver.find_element(By.XPATH,'//input[@id="country"]').send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//div[@class="suggestions"]')))
driver.find_element(By.LINK_TEXT,'India').click()
driver.find_element(By.XPATH,'//label[@for="checkbox2"]').click()
driver.find_element(By.XPATH,'//input[@class="btn btn-success btn-lg"]').click()
successMessage = driver.find_element(By.XPATH,'//div[@class="alert alert-success alert-dismissible"]').text
print(successMessage)
time.sleep(2)