Feature: Search tests for target.com

  Scenario: User can search for a product on target
    Given Open Target main page
    When Search for coffee
    Then Verify search results for coffee are shown
    Then Page url has search term coffee

  Scenario: User can search for a product on target
    Given Open Target main page
    When Search for coffee mug
    Then Verify search results for coffee mug are shown
    Then Page url has search term coffee+mug


  Scenario Outline: User can search for a product on target
    Given Open Target main page
    When Search for <product>
    Then Verify search results for <expected_result> are shown
    Then Page url has search term <expected_part_url>
    Examples:
    |product      |expected_result   |expected_part_url  |
    |coffee       |coffee            |coffee             |
    |coffee mug   |coffee mug        |coffee+mug         |
