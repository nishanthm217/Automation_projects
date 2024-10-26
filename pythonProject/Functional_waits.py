from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
derived_list =[]
expected_list = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
items=driver.find_elements(By.XPATH,'//div[@class="products"]/div')
items_count = len(items)

for item in items:
    derived_list.append(item.find_element(By.XPATH,'h4').text)
    item.find_element(By.XPATH,'div/button').click()
    time.sleep(0.5)
assert expected_list == derived_list

driver.find_element(By.XPATH,'//a[@class="cart-icon"]/img').click()
driver.find_element(By.XPATH,'//div[@class="cart-preview active"]/div/button').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys("rahulshettyacademy")
time.sleep(1)
driver.find_element(By.XPATH,'//button[@class="promoBtn"]').click()

#Price_validation
prices = driver.find_elements(By.CSS_SELECTOR,'tr td:nth-child(5) p')
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
validate_price = driver.find_element(By.XPATH,'//span[@class="totAmt"]')
assert sum == int(validate_price.text)


#Using explicit_wait for coupon apply
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))
print(driver.find_element(By.CSS_SELECTOR,'.promoInfo').text)


#Comparing the price validation b/w coupon(discounted price) and original prices.
# Discounted price should always be less of original prices
original_price = float(driver.find_element(By.XPATH,'//span[@class="totAmt"]').text)
discounted_price = float(driver.find_element(By.XPATH,'//span[@class="discountAmt"]').text)

assert discounted_price < original_price

