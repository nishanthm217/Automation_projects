from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise")
driver.maximize_window()
driver.implicitly_wait(7)
driver.find_element(By.LINK_TEXT,'Free Access to InterviewQues/ResumeAssistance/Material').click()
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])
get_text = driver.find_element(By.XPATH,'//div[@class="col-md-8"]/p[2]').text
extracted_string = get_text.split("at")[1].split(" ")[1]
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.XPATH,'//input[@id="username"]').send_keys(extracted_string)
driver.find_element(By.XPATH,'//input[@id="password"]').send_keys(extracted_string)
#driver.find_element(By.XPATH,'//label[2]//span[2]').click()
#driver.find_element(By.XPATH,'//div[@class="modal-footer justify-content-center"]/button[2]').click()
time.sleep(2)
dropdown_values = Select(driver.find_element(By.XPATH,'//select[@class="form-control"]'))
dropdown_values.select_by_visible_text("Student")
time.sleep(2)

driver.find_element(By.XPATH,'//input[@id="terms"]').click()
driver.find_element(By.XPATH, '//input[@id="signInBtn"]').click()

time.sleep(7)