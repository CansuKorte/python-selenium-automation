from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# -----------------------------------------------------------------------------------------------------------------
# PYTHON SYNTAX WITH AN *
# def func(a, b, c):
#     print(a)
#     print(b)
#     print(c)
#
# func(a=1, b=2, c=3,)  # or we can pass a list of numbers
#
# list_num = [1, 2, 3]
# func(list_num)  # --> gives error cause it needs 3 parameters. if you put * before it, it will take the whole list
# func(*list_num)
# ------------------------------------------------------------------------------------------------------------------
# VARIABLES FOR LOCATORS (so that it's easier to make changes in all codes using the same locators)

SEARCH_FIELD = (By.ID, 'search')
SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")


@given('Open Target.com')
def open_target_main_page(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product()
    sleep(6)

    # context.driver.find_element(*SEARCH_FIELD).send_keys(product) # -> If we use the variable above
    # context.driver.find_element(By.ID, 'search').send_keys(product) -> use when there is no variables
    # context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # context.driver.find_element(*SEARCH_ICON).click()


@when('Click on Cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()

    # context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    # context.driver.find_element(*CART_ICON).click()
    # sleep(2)
