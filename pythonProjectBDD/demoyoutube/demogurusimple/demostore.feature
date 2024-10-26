Feature: Username and password validation
  Background:
    Given open a url
  @smoke
  Scenario: Demo guru website username and password login
    When I enter 'nishanth.ezhilan', 'Nishanth@2021' and click submit
    Then check the website name for validation

  @regression
  Scenario Outline:
    When I enter '<username>', '<password>' and click submit
    Then check for validation with both positive and negative
    Examples:
      | username | password |
      | nishanth.ezhilan | Nishanth@2021 |
      | vffdf.ddd | dnfdn |

    @setupName
    Scenario:
    When I enter the userName and passWord for the file
      | userName | passWord |
      | nishanth.ezhilan | Nishanth@2021 |
    Then check the website name for validation