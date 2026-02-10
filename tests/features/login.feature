Feature: Login

  Scenario: Login should work with valid credentials
    Given I open the ParaBank login page
    When I login with valid credentials
    Then I should see the logout link
