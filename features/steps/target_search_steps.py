from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Search for coffee')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)


@then('Verify search results for coffee are shown')
def verify_search_results_correct(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert 'coffee' in actual_text, f'Expected word coffee not in {actual_text}'
    print('Test case passed')


@when('Search for mug')
def search_mug(context):
    context.driver.find_element(By.ID, 'search').send_keys('mug')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)


@then('Search results for mug are shown')
def verify_mug_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert 'mug' in actual_text, f'Expected word mug not in {actual_text}'
    print('Test case passed')
