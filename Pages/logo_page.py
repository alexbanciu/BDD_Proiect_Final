from selenium.webdriver.common.by import By
from browser import Browser



class LogoIsDisplayed(Browser):
    AMAZON_LOGO = (By.CSS_SELECTOR, 'a#nav-logo-sprites')

    def is_logo_displayed(self):
        return self.chrome.find_element(*self.AMAZON_LOGO).is_displayed()

    def verify_amazon_logo_displayed(self):
        if self.is_logo_displayed():
            print("Amazon logo is displayed")
        else:
            assert False, "Amazon logo is not displayed"