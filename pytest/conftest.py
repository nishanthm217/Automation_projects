import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def test_datasendto_baseclass(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(5)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("headless")
    chrome_options.add_argument("--ignore-certificate-errors")
    request.cls.driver = driver
    yield
    driver.close()
