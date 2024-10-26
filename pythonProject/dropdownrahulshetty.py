from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
#dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
time.sleep(2)
dropdown.select_by_index(1)
time.sleep(2)
dropdown.select_by_visible_text("Male")










time.sleep(4)