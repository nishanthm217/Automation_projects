from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time



@given("I got navigated to the registration page")
def homepage(context):
    context.driver.find_element(By.XPATH,'//span[contains(text(), "My Account")]').click()
    context.driver.find_element(By.LINK_TEXT,'Register').click()

@when("I enter all the fields in the register page")
def enter_register(context):
    context.driver.find_element(By.ID,'input-firstname').send_keys("Hinanddna")
    context.driver.find_element(By.ID,'input-lastname').send_keys("M")
    context.driver.find_element(By.ID,'input-email').send_keys("princea@gmail.com")
    context.driver.find_element(By.ID,'input-telephone').send_keys("9484848484")
    context.driver.find_element(By.ID,'input-password').send_keys("Nishanth@2021")
    context.driver.find_element(By.ID,'input-confirm').send_keys("Nishanth@2021")
    context.driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()

@when("I click register buttonnnn")
def click_register(context):
    context.driver.find_element(By.XPATH,'//div[@class="buttons"]/div/input[2]').click()


@then("New registration should happen")
def new_register(context):
    expected_text = "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH,'//div[@id="content"]/h1').text.__contains__(expected_text)



@when("I enter the mandatory fields in the register page")
def mandatory_field(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys("mddunnaanna")
    context.driver.find_element(By.ID, 'input-lastname').send_keys("M")
    context.driver.find_element(By.ID, 'input-email').send_keys("salaar@gmail.com")
    context.driver.find_element(By.ID, 'input-telephone').send_keys("9484848484")
    context.driver.find_element(By.ID, 'input-password').send_keys("Nishanth@2021")
    context.driver.find_element(By.ID, 'input-confirm').send_keys("Nishanth@2021")
    context.driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()

@when("I enter the already used email ID")
def avail_field(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys("Hinanna")
    context.driver.find_element(By.ID, 'input-lastname').send_keys("M")
    context.driver.find_element(By.ID, 'input-email').send_keys("nishanth.ezhilan222@gmail.com")
    context.driver.find_element(By.ID, 'input-telephone').send_keys("9484848484")
    context.driver.find_element(By.ID, 'input-password').send_keys("Nishanth@2021")
    context.driver.find_element(By.ID, 'input-confirm').send_keys("Nishanth@2021")
    context.driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()

@then("It would show error message")
def error_msg(context):
    exp_textONe = "Warning: E-Mail Address is already registered!"
    context.driver.find_element(By.XPATH,'//div[@class="alert alert-danger alert-dismissible"]').text.__contains__(exp_textONe)



@when("I enter nothing in the email_ID")
def nothing_error(context):
    context.driver.find_element(By.ID, 'input-firstname').send_keys("")
    context.driver.find_element(By.ID, 'input-lastname').send_keys("")
    context.driver.find_element(By.ID, 'input-email').send_keys("")
    context.driver.find_element(By.ID, 'input-telephone').send_keys("")
    context.driver.find_element(By.ID, 'input-password').send_keys("")
    context.driver.find_element(By.ID, 'input-confirm').send_keys("")
    context.driver.find_element(By.XPATH, '//input[@type="checkbox"]').click()

@then("It would show not a valid mail message")
def invalid_email(context):
    context.driver.find_element(By.XPATH,'//div[contains(text(),"E-Mail Address does not appear to be valid!")]').is_displayed()

