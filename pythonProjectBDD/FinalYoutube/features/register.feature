Feature: Registration functionality

  Scenario: Registering with all fields
    Given I got navigated to the registration page
    When I enter all the fields in the register page
    And I click register buttonnnn
    Then New registration should happen

  Scenario: Registering with the mandatory fields
    Given I got navigated to the registration page
    When I enter the mandatory fields in the register page
    And I click register buttonnnn
    Then New registration should happen


  Scenario: Registering with the used email ID
    Given I got navigated to the registration page
    When I enter the already used email ID
    And I click register buttonnnn
    Then It would show error message


  Scenario: Registering without giving email ID
    Given I got navigated to the registration page
    When I enter nothing in the email_ID
    And I click register buttonnnn
    Then It would show not a valid mail message