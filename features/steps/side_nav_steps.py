from behave import given, when, then


@when('From right side navigation menu, click Sign In')
def click_side_nav_signin(context):
    context.app.side_navigation.click_side_nav_signin()


@when('Store product name')
def store_product_name(context):
    context.app.side_navigation.store_product_name()


@when('From right side navigation menu, click Add to cart button')
def click_side_nav_add_to_cart(context):
    context.app.side_navigation.click_side_nav_add_to_cart()


@when('From right side navigation menu, click previous icon')
def click_side_nav_previous_icon(context):
    context.app.side_navigation.click_side_nav_previous_icon()
