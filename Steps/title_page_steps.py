from behave import *



@then('Home page: The page title "{title_page}" should be displayed')
def step_impl(context, title_page):
    context.title_page_object.is_page_title_displayed(title_page)