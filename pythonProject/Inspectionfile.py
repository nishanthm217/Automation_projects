from selenium  import webdriver
from selenium.webdriver.common.by import By
import time
#We want to identify the right locator and want to pass that element.
#Our goal is to identify the elements
# By using ID, Xpath, CSSselector, classname,  name, LinkText we want to identify the correct elements
driver = webdriver.Chrome()
driver.get("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(2)
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("12345689")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "ud-btn-brand").click()
time.sleep(2)
message=driver.find_element(By.XPATH,"//div[@data-purpose='safely-set-inner-html:auth:error']").text
print(message)

assert "something went wrong" in message
