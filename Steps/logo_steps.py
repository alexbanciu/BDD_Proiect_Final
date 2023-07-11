from behave import *


@then("Home page: The Amazon logo should be displayed")
def step_impl(context):
    context.logo_is_displayed.verify_amazon_logo_displayed()