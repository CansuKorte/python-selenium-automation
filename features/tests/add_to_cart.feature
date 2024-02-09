Feature: Target tests for adding items to cart

  Scenario: User can add items to cart
    Given Open Target main page
    When Search for Terracotta Ceramic Table Lamp
    Then Verify search results for Terracotta Ceramic Table Lamp are shown
    When Click on Add to cart button
    When From right side navigation menu, click Add to cart button
    When From right side navigation menu, click previous icon
    When  Click on Cart icon
    Then  Verify added item is in the cart