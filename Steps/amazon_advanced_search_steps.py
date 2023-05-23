from behave import *


@when("Today's Deals: I select Computers & Accessories department")
def step_impl(context):
    context.advanced_search_object.select_departments()


@when("Today's Deals: I choose the price")
def step_impl(context):
    context.advanced_search_object.select_price()


@when("Today's Deals: I select average customer review rating")
def step_impl(context):
    context.advanced_search_object.select_review_rating()


@when("Today's Deals: I select the Discount that I want")
def step_impl(context):
    context.advanced_search_object.select_discount()


@then("Today's Deals: I should be able to remove or modify any applied search filters easily")
def step_impl(context):
    context.advanced_search_object.select_first_product()