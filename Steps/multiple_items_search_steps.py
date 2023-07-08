from behave import *
from time import sleep


@when('I search for the following "{items}":')
def step_impl(context, items):
    context.multiple_items_search_object.search_item(items)