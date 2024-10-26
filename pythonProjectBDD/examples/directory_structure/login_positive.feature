Feature: Logging in with valid credentials

Scenario: User login successfully
  Given I create a new user
  When I type email
  When I type password
  When I click on 'Login'
  Then I should see the text welcome
