# Created by cansuhas at 2/2/24

Feature: Verification scenarios for Target.com

  Scenario: User can see empty cart message
    Given Open Target.com
    When  Click on Cart icon
    Then  Verify Your cart is empty message is displayed


  Scenario: Logged out user can access Sign In
    Given Open Target.com
    When  Click Sign In
    And   From right side navigation menu, click Sign In
    Then  Verify "Sign into your Target account" message is shown