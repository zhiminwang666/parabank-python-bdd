Feature: API Auth

  Scenario: Create account API should reject unauthorized request
    Given I call createAccount API without auth
    Then API response status should be 401
