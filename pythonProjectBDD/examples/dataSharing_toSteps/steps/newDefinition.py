from behave import given, when, then
@given("I couldn't find the matched order number")
def new_check_data(context):
    print("I'm inside the database checking for the refund")
    print("The order number refunded is: {}".format(context.order_num))

@when("I click the refund it shouldn't be accepted")
def new_find_data(context):
    print("I check whether the request is available or not")
    print("The order number request initiated is: {}".format(context.order_num))

@then("It shouldn't be transferred to the customer")
def new_final_request_data(context):
    print("I'm at the final phase of initiating transaction")
    print("The transaction refunded to the order num is: {}".format(context.order_num))