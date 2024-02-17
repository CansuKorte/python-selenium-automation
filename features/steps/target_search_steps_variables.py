from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SIDE_NAV_PRODUCT_NAME = (By.XPATH, "//h4[contains(@class, 'styles__StyledHeading')]")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()


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


@when('Store product name')
def store_product_name(context):
    context.wait.until(EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME), message='Side nav did not open')
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    # sleep(3)


@when('From right side navigation menu, click Add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='shippingButton']").click()


@when('From right side navigation menu, click previous icon')
def click_previous_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Previous']").click()


@when('Click on Cart icon')
def click_cart_icon(context):
    cart_icon = (By.XPATH, "//a[@data-test='@web/CartLink']")
    context.wait.until(EC.element_to_be_clickable(cart_icon), message='Cart icon not clickable').click()
    # sleep(3)


# @then('Verify added item is in the cart')
# def verify_item_in_cart(context):
#     assert context.driver.find_element(By.XPATH, "//div[@data-test='cartItem-title']").is_displayed()

# for this last step we can use the stored product name for verification;

@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name == actual_name, f"Expected {context.product_name} but got {actual_name}"

#  Getting a failed assertion at the end of my test, can you tell what is wrong?


