Feature: Parsing parameters to steps
  Scenario: method 1 of passing step parameters
    Given I have a new "DVD" in my cart
    And I have a new "BOOK" in my cart

    When I click on "NEXT"
    And I click on "FINISH"

    Then I should see "success"
    And I should see "SUCCESSFULL"