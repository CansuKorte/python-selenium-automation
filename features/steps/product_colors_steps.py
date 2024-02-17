from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given('Open Target product {product_id} page')
def open_page(context, product_id):
    context.driver.get('https://www.target.com/p/A-81540287')
    sleep(6)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Deep Olive', 'White']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # ['Color\nBlack']
        selected_color = selected_color.split('\n')[1]  # Black
        actual_colors.append(selected_color)
    print(actual_colors)

    assert actual_colors == expected_colors, f' Expected {expected_colors} but got {actual_colors}'


