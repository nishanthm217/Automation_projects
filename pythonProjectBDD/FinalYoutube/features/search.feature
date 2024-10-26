Feature: Search Functionality
  Scenario: Search for a valid product
    Given I got navigated to the home page
    When I enter the valid product name
    And I click search button
    Then Valid product should get displayed in the search result

  Scenario: Search for a invalid product
    Given I got navigated to the home page
    When I enter the invalid product name
    And I click search button
    Then Proper message should be displayed in search results

  Scenario: Search without entering product in the search
    Given I got navigated to the home page
    When I enter the nothing in the search
    And I click search button
    Then Proper message should be displayed in search results