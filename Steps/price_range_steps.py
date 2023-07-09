from behave import when, then


@when('I search for "{item}"')
def step_search_item(context, item):
    context.price_range_object.search_item(item)


@when('I apply a filter for a price range of ${min_price} to ${max_price}')
def step_apply_price_filter(context, min_price, max_price):
    context.min_price = float(min_price)
    context.max_price = float(max_price)
    context.price_range_object.apply_price_filter()


@then('If the filter was applied I should be able to see the icon to close that price filter')
def step_impl(context):
    context.price_range_object.click_close_icon()