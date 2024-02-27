from behave import given, when, then


@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('Current window', context.original_window)
    print('All windows:', context.driver.window_handles)


@when('Click on Target terms and conditions link')
def click_terms_conditions_link(context):
    context.app.target_signin_page.click_terms_conditions_link()
    print('All windows:', context.driver.window_handles)


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.target_signin_page.switch_to_new_window()
    print('After switching to a new window:')
    print('All windows:', context.driver.window_handles)
    print('Current window', context.driver.current_window_handle)


@then('Verify Terms and Conditions page is opened')
def verify_terms_conditions_page_opened(context):
    context.app.target_signin_page.verify_terms_conditions_page_opened()


@then('User can close new window')
def close(context):
    context.driver.close()


@then('Switch back to original window')
def switch_to_original_window(context):
    context.app.target_signin_page.switch_to_window_by_id(context.original_window)
    print('After switching back to original:')
    print('Current window', context.driver.current_window_handle)