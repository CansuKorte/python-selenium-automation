# Created by cansuhas at 2/1/24
Feature: Target.com search tests
  # Enter feature description here

  Scenario: User can search for a product on target
    # Enter steps here
    # All pre-conditions and things before the actual interaction with the page go under 'GIVEN'
    Given Open Target main page
    # All actions we do; search, click, populate a text etc go under 'WHEN'
    When Search for coffee
    # All verifications go under 'THEN'
    Then Verify search results for coffee are shown


  # Make sure Scenario names are unique:
  Scenario: User can search for a mug on target
    Given Open Target main page
    When Search for mug
    Then Search results for mug are shown