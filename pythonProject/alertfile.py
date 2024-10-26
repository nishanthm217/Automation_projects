from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
name = "Syed"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,'#name').send_keys(name)
time.sleep(2)
driver.find_element(By.ID,"alertbtn").click()
alert  =  driver.switch_to.alert
alertText = alert.text
assert name in alertText
time.sleep(2)
if(name in alertText):
    alert.accept()
    #alert.dismiss()
print(alertText)
time.sleep(2)




time.sleep(3)