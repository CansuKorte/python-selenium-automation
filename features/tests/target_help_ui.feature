
Feature: Verification tests for Target Help page UI

  Scenario: Verify 'Target Help' text is shown
    Given Open Target Help page
    Then Verify 'Target Help' text is shown

  Scenario: Verify 'search help' text is shown in search engine
    Given Open Target Help page
    Then Verify 'search help' text is shown in search engine

  Scenario: Verify there is a search icon to click on
    Given Open Target Help page
    Then Verify there is a search icon to click on

  Scenario: Verify there are 7 links in the first column
    Given Open Target Help page
    Then Verify there are 7 links in the first column

  Scenario: Verify there are 2 links in the second column
    Given Open Target Help page
    Then Verify there are 2 links in the second column
    # (no holiday help box present)

  Scenario: Verify the 'Browse all Help pages' text is shown
    Given Open Target Help page
    Then Verify the 'Browse all Help pages' text is shown
