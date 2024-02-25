from behave import given, when, then


@then('Verify "Sign into your Target account" message is shown')
def verify_signin_msg(context):
    context.app.target_signin_page.verify_sign_into_account_msg()
