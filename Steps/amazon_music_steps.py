from behave import *


@when('Home page: I click on All button from top menu')
def step_impl(context):
    context.amazon_music_object.click_all_button()


@when('Home page: I click on Amazon Music')
def step_impl(context):
    context.amazon_music_object.click_amazon_music_button()


@when('Home page: I choose Free Streaming Music from the menu')
def step_impl(context):
    context.amazon_music_object.click_free_streaming_music_button()


@when('Amazon music page: I click on listen now button')
def step_impl(context):
    context.amazon_music_object.click_listen_now_button()


@when('Amazon streaming music: I should be redirected to Amazon streaming music page')
def step_impl(context):
    context.amazon_music_object.verify_redirected_link()


@then('Home page: I should return to the home page')
def step_impl(context):
    context.amazon_music_object.return_to_homepage()