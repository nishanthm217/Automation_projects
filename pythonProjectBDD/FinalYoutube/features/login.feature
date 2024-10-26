Feature: Webpage login functionality

  Scenario: Login with valid username and password
    Given I navigated to the login page
    When I give valid username and password
    And I click the button  login
    Then I should get logged in


  Scenario: Login with invalid username and correct password
    Given I navigated to the login page
    When I give invalid username and correct password
    And I click the button  login
    Then Proper warning message should get displayed

  Scenario: Login with valid username and incorrect password
    Given I navigated to the login page
    When I give valid username and incorrect password
    And I click the button  login
    Then Proper warning message should get displayed

  Scenario: Login with invalid username and incorrect password
    Given I navigated to the login page
    When I give invalid username and incorrect password
    And I click the button  login
    Then Proper warning message should get displayed

  Scenario: Login without typing username and password
    Given I navigated to the login page
    When I give nothing means invalid username and password
    And I click the button  login
    Then Proper warning message should get displayed


