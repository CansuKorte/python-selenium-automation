from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Help page')
def open_target_help(context):
    context.driver.get('https://help.target.com/help')


@then("Verify 'Target Help' text is shown")
def verify_target_help_text(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "[class='custom-h2']").is_displayed()
    sleep(2)


@then("Verify 'search help' text is shown in search engine")
def verify_search_help_text(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "[title='search help']").is_displayed()


@then("Verify there is a search icon to click on")
def verify_search_icon(context):
    assert context.driver.find_element(By.XPATH, "//input[contains(@src, 'search_icon')]").is_displayed()
    sleep(2)


@then('Verify there are {expected_amount} links in the first column')
def verify_column_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class='grid_6']")
    assert len(links) == expected_amount, f"Expected {expected_amount} links but got {len(links)}"
    sleep(2)


@then('Verify there are {expected_num} links in the second column')
def verify_column_links(context, expected_num):
    expected_num = int(expected_num)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='grid_4']")
    assert len(links) == expected_num, f"Expected {expected_num} links but got {len(links)}"
    sleep(2)


@then("Verify the 'Browse all Help pages' text is shown")
def verify_browse_pages_text(context):
    assert context.driver.find_element(By.ID, "divID1").is_displayed()
    sleep(2)


