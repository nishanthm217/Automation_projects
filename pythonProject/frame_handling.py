from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.implicitly_wait(5)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.XPATH,'body p').clear()
driver.find_element(By.XPATH,'//iframe[@id="mce_0_ifr"]').send_keys("I am able to automate the frames")