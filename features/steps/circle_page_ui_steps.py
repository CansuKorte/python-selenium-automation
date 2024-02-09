from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open the Target Circle page')
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle')
    sleep(2)


@then('Verify there are {expected_amount} benefit boxes on circle page')
def verify_benefit_boxes(context, expected_amount):
    expected_amount = int(expected_amount)
    boxes = context.driver.find_elements(By.CSS_SELECTOR, "[class*='styles__BenefitCard-']")
    assert len(boxes) == expected_amount, f"Expected 5 boxes but got {len(boxes)}"
    sleep(2)

