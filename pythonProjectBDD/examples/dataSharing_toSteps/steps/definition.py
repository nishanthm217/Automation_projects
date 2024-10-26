from behave import given, when, then
@given("I can initiate the payment refund request through the database")
def check_data(context):
    print("I'm inside the database checking for the refund")
    context.order_num = "333090"
    print("The order number refunded is: {}".format(context.order_num))

@when("I click the refund it should be accepted")
def find_data(context):
    print("I check whether the request is available or not")
    print("The order number request initiated is: {}".format(context.order_num))

@then("It should be transferred to the customer")
def final_request_data(context):
    print("I'm at the final phase of initiating transaction")
    print("The transaction refunded to the order num is: {}".format(context.order_num))