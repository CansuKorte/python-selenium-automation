Feature: Target tests for window handling

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target.com
    When  Click Sign In
    And   From right side navigation menu, click Sign In
    Then  Verify "Sign into your Target account" message is shown
  # Target sign in page link redirects to Target main page, so needed to use the same steps above
    When Store original windows
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window
    And Switch back to original window