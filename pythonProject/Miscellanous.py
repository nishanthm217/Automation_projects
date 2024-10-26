from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

chrome_Options = webdriver.ChromeOptions()
chrome_Options.add_argument("headless")
chrome_Options.add_argument("--ignore-certificate-errors")
driver=webdriver.Chrome(options=chrome_Options)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") #Scrolling to bottom
driver.get_screenshot_as_file("screen.png") #Taking screenshot
time.sleep(4)