from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, "username").send_keys("nishanth@gmail.com")
driver.find_element(By.ID, "password").send_keys("Nishanth@1001")
#Creating tagname here --> //tagname[@attribute='value']
#driver.find_element(By.XPATH, '//svg[@role="presentation"]').click()
driver.find_element(By.ID, "loginBtn").click()
message = driver.find_element(By.CLASS_NAME,"Heading-sc-1aecbgk-0").text
print(message)
time.sleep(10)
