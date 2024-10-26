from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
time.sleep(3)
driver.find_element(By.LINK_TEXT,'Shop').click()
time.sleep(2)
products_Get = driver.find_elements(By.XPATH,'//div[@class="card h-100"]')

for product_select in products_Get:
    ProductName = product_select.find_element(By.XPATH,'div/h4/a').text
    if (ProductName =="iphone X") or (ProductName == "Blackberry"):
        time.sleep(2)
        product_select.find_element(By.XPATH,'div/button').click()

driver.find_element(By.XPATH,'//a[@class="nav-link btn btn-primary"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//button[@class="btn btn-success"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//input[@id="country"]').send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//div[@class="suggestions"]')))
get_countries = driver.find_elements(By.XPATH,'//div[@class="suggestions"]')
driver.find_element(By.LINK_TEXT,'India').click()
time.sleep(2)
driver.find_element(By.XPATH,'//a[@style="cursor: pointer;color: #1d1dfb; text-decoration: underline;"]').click()
driver.find_element(By.XPATH,'//button[@class="btn btn-info"]').click()
time.sleep(2)

driver.find_element(By.XPATH,'//input[@class="btn btn-success btn-lg"]').click()
time.sleep(4)
successText = driver.find_element(By.XPATH,'//div[@class="alert alert-success alert-dismissible"]').text
assert "Success! Thank you!" in successText
print(successText)
