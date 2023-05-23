from behave import *


@when("sign_up: I click on sign up button")
def step_impl(context):
    context.sign_up_page_object.go_to_sign_up()


@when("sign_up: I send my full name")
def step_impl(context):
    context.sign_up_page_object.insert_full_name("Alexandru Banciu")


@when("sign_up: I enter my email")
def step_impl(context):
    context.sign_up_page_object.insert_email("alexandruioanbanciu@gmail.com")


@when("sign_up: I send the password")
def step_impl(context):
    context.sign_up_page_object.insert_password("123456")


@when("sign_up: I re-enter a wrong password")
def step_impl(context):
    context.sign_up_page_object.insert_password_check("12345")


@when("sign_up: I submit my personal info by clicking verify email")
def step_impl(context):
    context.sign_up_page_object.verify_email_button()


@then("sing_up: I should receive the message: Passwords must match")
def step_impl(context):
    context.sign_up_page_object.check_error_message()