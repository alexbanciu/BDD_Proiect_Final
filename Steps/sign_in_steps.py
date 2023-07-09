from behave import *


@when("Home page: I click on the Sign In button")
def step_impl(context):
    context.sign_in_object.go_to_sign_in()


@when("Sign In page: I send email and password")
def step_impl(context):
    context.sign_in_object.send_email('alexandruioanbanciu@gmail.com')
    context.sign_in_object.click_send_email()
    context.sign_in_object.click_send_password('1234567')
    context.sign_in_object.clear_password()


@then("I should get back to amazon homepage")
def step_impl(context):
    context.sign_in_object.return_to_page()