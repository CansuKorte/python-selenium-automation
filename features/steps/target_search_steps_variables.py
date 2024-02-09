from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)


@then('Verify search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_result in actual_text, f'Expected word {expected_result} not in {actual_text}'


@then('Page url has search term {expected_part_url}')
def verify_search_results_url(context, expected_part_url):
    url = context.driver.current_url
    assert expected_part_url in url, f'Expected word {expected_part_url} not in {url}'


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id*='IdFor88889037']").click()


@when('From right side navigation menu, click Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='shippingButton']").click()


@when('From right side navigation menu, click previous icon')
def click_previous_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Previous']").click()


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(2)


@then('Verify added item is in the cart')
def verify_item_in_cart(context):
    assert context.driver.find_element(By.XPATH, "//div[@data-test='cartItem-title']").is_displayed()
