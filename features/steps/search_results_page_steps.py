from behave import given, when, then
from selenium.webdriver.common.by import By

# SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.search_results_page.click_add_to_cart()


@then('Verify search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    context.app.search_results_page.verify_search_results_correct(expected_result)

    # actual_text = context.driver.find_element(*SEARCH_RESULTS_HEADER).text
    # assert expected_result in actual_text, f'Expected word {expected_result} not in {actual_text}'


@then('Page url has search term {expected_part_url}')
def verify_search_results_url(context, expected_part_url):
    context.app.search_results_page.verify_search_results_page_url(expected_part_url)

    # url = context.driver.current_url
    # assert expected_part_url in url, f'Expected word {expected_part_url} not in {url}'
