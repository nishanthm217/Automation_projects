import pytest
@pytest.fixture
def test_giving(request):
    from selenium import webdriver
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
