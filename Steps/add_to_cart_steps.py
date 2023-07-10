from behave import *

from Pages.add_to_cart_page import CartPage


@when('Main Page: I type "{cart_item}"')
def step_impl(context, cart_item):
    context.add_to_cart_object.perform_search(cart_item)


@then("Search results page: I select the first iphone from the search results")
def step_impl(context):
    context.add_to_cart_object.select_first_product()


@when("Cart page: I click on Add to Cart")
def step_impl(context):
    context.add_to_cart_object.add_to_cart()


@then("Cart page: I should see at least one item in the cart")
def step_impl(context):
    cart_item_count = context.add_to_cart_object.get_cart_item_count()
    assert cart_item_count >= 1, "Expected at least one item in the cart"