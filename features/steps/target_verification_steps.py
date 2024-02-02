from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Steps for the first scenario


@given('Open Target.com')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(2)


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(2)


@then('Verify "Your cart is empty" message is displayed')
def verify_cart_empty(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"
    print("Test case passed")
    sleep(3)


# Steps for the second scenario
# (Since there is one step for 'open target' above, I didn't put it here again)


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH,"//a[@data-test='@web/AccountLink']").click()
    sleep(2)


@when('From right side navigation menu, click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(2)


@then('Verify "Sign into your Target account" message is shown')
def verify_signin_msg(context):
    expected_text = "Sign into your Target account"
    actual_text = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign into your Target account')]").text
    assert expected_text in actual_text, f"Expected {expected_text} but got {actual_text}"
    print("Test passed")
    sleep(3)
