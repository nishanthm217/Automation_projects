from logging import exception

from behave import given, when, then

@given("I have a new {item} in my cart")
def i_have_item_in_my_cart(context, item):
    print("The item is {} : ".format(item))

@when("I click {click_button}")
def i_items_button(context, click_button):
    print("Printing the next message: {}".format(click_button))

@then("I should see {text}")
def submit_text_button(context,text):
    print("The message should be displayed is success here: {}".format(text))