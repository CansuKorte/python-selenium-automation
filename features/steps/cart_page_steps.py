from selenium.webdriver.common.by import By
from behave import given, when, then

CART_EMPTY_MSG = (By.XPATH, "//div[@data-test='boxEmptyMsg']")


@then('Verify {expected_msg} message is displayed')
def verify_cart_empty(context, expected_msg):
    context.app.cart_page.verify_cart_empty_msg(expected_msg)

    # actual_text = context.driver.find_element(*CART_EMPTY_MSG").text
    # assert 'Your cart is empty' == actual_text, f"Expected 'Your cart is empty' but got {actual_text}"

