#Process of initiating refund to the customer

Feature: Process of initiating the refund
  Scenario: Initiate the refund process it will be successful
    Given I can initiate the payment refund request through the database
    When I click the refund it should be accepted
    Then It should be transferred to the customer

  Scenario: The refund process should be unsuccessful
    Given I couldn't find the matched order number
    When I click the refund it shouldn't be accepted
    Then It shouldn't be transferred to the customer
