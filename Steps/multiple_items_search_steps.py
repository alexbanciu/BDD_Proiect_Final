from telnetlib import EC

from behave import *
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@when('I search for the following "{items}":')
def step_impl(context, items):
    context.multiple_items_search_object.search_item(items)
    context.multiple_items_search_object.click_search_button2()


@then('I should see search results for each item')
def step_impl(context):