Feature: Testing python.org website
  Scenario: Checking the welcome message in python
    Given I open the url
    When I found the welcome message
    Then It should be true or else false