from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
browser_sorted_fruits = []
driver.find_element(By.XPATH,'//span[text()="Veg/fruit name"]').click()
Optained_fruits = driver.find_elements(By.XPATH,'//tr/td[1]')

for element in Optained_fruits:
    browser_sorted_fruits.append(element.text)
    print(element.text)

original_sorted = browser_sorted_fruits.copy()
browser_sorted_fruits.sort()

assert original_sorted == browser_sorted_fruits
