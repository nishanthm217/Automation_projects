from behave import given, when, then
import assertion
@given("I create a new user")
def create_new_user(context):
    print("I am creating a new user")
    print("More code would go here")

@when("I type email")
def type_the_email(context):
    print("Typing email in the email field")
    print("Just finished typing the email")

@when("I type password")
def type_the_password(context):
    print("I'm typing the password")
    print("I just typed the password")

@when("I click on 'Login'")
def click_login(context):
    print("Clicked the login")

@then("I should see the text welcome")
def welcome_text(context):
    print("Process finished with the exceptions")

