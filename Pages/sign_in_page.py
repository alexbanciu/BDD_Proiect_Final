import self as self
from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep


class SignInPage(Browser):
    SIGN_IN_BUTTON = (By.ID, "nav-link-accountList-nav-line-1")
    EMAIL_SEND = (By.ID, "ap_email")
    PASSWORD_SEND = (By.ID, "ap_password")
    CONTINUE_BUTTON = (By.ID, "continue")

    def go_to_sign_in(self):
        self.chrome.find_element(*self.SIGN_IN_BUTTON).click()

    def send_email(self, email):
        self.chrome.find_element(*self.EMAIL_SEND).send_keys(email)

    def click_send_email(self):
        self.chrome.find_element(*self.CONTINUE_BUTTON).click()

    def click_send_password(self, password):
        self.chrome.find_element(*self.PASSWORD_SEND).send_keys(password)

    def clear_password(self):
        self.chrome.find_element(*self.PASSWORD_SEND).clear()

    def return_to_page(self):
        self.chrome.get('https://www.amazon.com/')
        sleep(3)