from behave import *



@then("Home page: The page title should be displayed")
def step_impl(context):
    assert context.title_page_object.is_page_title_displayed(), "Page title is not displayed"