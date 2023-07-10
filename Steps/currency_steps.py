from behave import *


@when("Home page: I click on the currency dropdown")
def step_impl(context):
    context.currency_page_object.click_currency_dropdown()


@when('Home page: I select the currency as Euro')
def step_impl(context):
    context.currency_page_object.select_currency()


@then("Home page: The currency should be changed to EUR")
def step_impl(context):
    context.currency_page_object.get_selected_currency()