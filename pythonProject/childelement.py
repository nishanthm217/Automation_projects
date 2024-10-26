from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(4)
driver.find_element(By.LINK_TEXT,"Click Here").click()
#Using window handles to get capture the windows
windowsOpened = driver.window_handles
time.sleep(2)
driver.switch_to.window(windowsOpened[1])
get_text = driver.find_element(By.TAG_NAME,'h3').text
print(get_text)
driver.close()
time.sleep(2)
driver.switch_to.window(windowsOpened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,'h3').text


