from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


@given(u'I got navigated to the home page')
def homepage(context):
    title_expectedF = "Your Store"
    assert context.driver.title == title_expectedF

@when("I enter the valid product name")
def valid_username(context):
    context.driver.find_element(By.XPATH,'//input[@name="search"]').send_keys("HP")

@when("I click search button")
def click_search(context):
    context.driver.find_element(By.XPATH,'//button[@class="btn btn-default btn-lg"]').click()

@then("Valid product should get displayed in the search result")
def valid_product(context):
    assert context.driver.find_element(By.XPATH,'//a[contains(text(),"HP LP3065")]').is_displayed()

#Scenario Two
@when("I enter the invalid product name")
def invalid_product(context):
    context.driver.find_element(By.XPATH,'//input[@name="search"]').send_keys("Audi")

@then("Proper message should be displayed in search results")
def proper_message(context):
    getText  = context.driver.find_element(By.XPATH,'//div[@id="content"]/p[2]').text
    expected_text = "There is no product that matches the search criteria."
    assert getText == expected_text


#Scenario Three
@when("I enter the nothing in the search")
def enter_nothing(context):
    context.driver.find_element(By.XPATH,'//input[@name="search"]').send_keys("")


