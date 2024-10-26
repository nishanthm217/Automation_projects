from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

@given("I navigated to the login page")
def navigation_page(context):
    context.driver.find_element(By.XPATH,'//span[contains(text(), "My Account")]').click()
    context.driver.find_element(By.LINK_TEXT,'Login').click()

@when("I give valid username and password")
def valid_user_and_valid_pass(context):
    context.driver.find_element(By.ID,'input-email').send_keys("nishanth.ezhilan222@gmail.com")
    context.driver.find_element(By.ID,'input-password').send_keys("Nishanth@2021")

@when("I click the button  login")
def click_login(context):
    context.driver.find_element(By.XPATH,'//input[@type="submit"]').click()

@then("I should get logged in")
def login_success(context):
    context.driver.find_element(By.LINK_TEXT,'Edit your account information').is_displayed()


#Scenario2

@when("I give invalid username and correct password")
def invalid_user_and_pass(context):
    context.driver.find_element(By.ID,'input-email').send_keys("nihdhdhdhd@gmail.com")
    context.driver.find_element(By.ID, 'input-password').send_keys("Nishanth@2021")

@then("Proper warning message should get displayed")
def warning_message(context):
    warning_text = context.driver.find_element(By.XPATH,'//div[@class="alert alert-danger alert-dismissible"]').text
    expected_text  = "Warning: No match for E-Mail Address and/or Password."
    assert warning_text == expected_text

#Scenario3
@when("I give valid username and incorrect password")
def valid_user_and_invalid_pass(context):
    context.driver.find_element(By.ID, 'input-email').send_keys("nishanth.ezhilan222@gmail.com")
    context.driver.find_element(By.ID, 'input-password').send_keys("Nish@4441")

#Scenario4
@when("I give invalid username and incorrect password")
def invalid_user_and_invalid_pass(context):
    context.driver.find_element(By.ID, 'input-email').send_keys("nihdhdhdhd@gmail.comm")
    context.driver.find_element(By.ID, 'input-password').send_keys("Nish@4441")

#Scenario5
@when("I give nothing means invalid username and password")
def nothing_user_and_pass(context):
    context.driver.find_element(By.ID, 'input-email').send_keys("")
    context.driver.find_element(By.ID, 'input-password').send_keys("")



