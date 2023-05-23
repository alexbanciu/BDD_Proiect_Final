from Pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class SignUpPage(BasePage):
    SIGN_UP_BUTTON = (By.XPATH, '//*[@id="nav-signin-tooltip"]/div/a')
    FULL_NAME_INPUT = (By.ID, "ap_customer_name")
    EMAIL_INPUT = (By.ID, "ap_email")
    PASSWORD_INPUT = (By.ID, "ap_password")
    PASSWORD_CHECK_INPUT = (By.ID, "ap_password_check")
    VERIFY_EMAIL_BUTTON = (By.ID, "continue")

    def go_to_sign_up(self):
        self.chrome.find_element(*self.SIGN_UP_BUTTON).click()

    def insert_full_name(self, name):
        self.chrome.find_element(*self.FULL_NAME_INPUT).send_keys(name)

    def insert_email(self, email):
        self.chrome.find_element(*self.EMAIL_INPUT).send_keys(email)

    def insert_password(self, password):
        self.chrome.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def insert_password_check(self, check):
        self.chrome.find_element(*self.PASSWORD_CHECK_INPUT).send_keys(check)

    def verify_email_button(self):
        self.chrome.find_element(*self.VERIFY_EMAIL_BUTTON).click()

    def check_error_message(self):
        expected = "Passwords must match"
        actual = self.chrome.find_element(By.XPATH, '//*[@id="auth-password-mismatch-alert"]/div/div').text
        assert expected == actual