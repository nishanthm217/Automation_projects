from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver
@given("open a url")
def url_open(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.guru99.com/test/newtours/")
    context.driver.maximize_window()

@then("check the website name for validation")
def web_validation(context):
    varTitle  = context.driver.title
    assert "Login: Mercury Tours" == varTitle


@when("I enter '{username}', '{password}' and click submit")
def sending_keys(context,username, password):
    context.driver.find_element(By.XPATH,"//input[@name='userName']").send_keys(username)
    context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)
    context.driver.find_element(By.XPATH,"//input[@name='submit']").click()

@then("check for validation with both positive and negative")
def another_validation(context):
    try:
        text = context.driver.find_element(By.XPATH,'//h3[text()="Login Successfully"]').text
    except:
        context.driver.close()
        assert False, "Test Cases Failed"

    if text =="Login Successfully":
        context.driver.close()
        assert True, "Test Cases Passed"




@when("I enter the username and password for the file")
def table_setup(context):
    for i in context.table:
        context.driver.find_element(By.XPATH,"//input[@name='userName']").send_keys(i['userName'])
        context.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(i['passWord'])
        context.driver.find_element(By.XPATH,"//input[@name='submit']").click()



