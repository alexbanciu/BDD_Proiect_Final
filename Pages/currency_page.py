from selenium.webdriver.common.by import By
from browser import Browser
from selenium.webdriver.support.ui import Select


class CurrencyPage(Browser):
    CURRENCY_DROPDOWN = (By.XPATH, '//*[@id="icp-nav-flyout"]/span/span[2]/span[1]')
    CURRENCY_OPTION = (By.XPATH, '//*[@id="icp-currency-dropdown-selected-item-prompt"]/span/span')
    SELECTED_CURRENCY = (By.XPATH, "//span[text()=' - Euro']")

    def click_currency_dropdown(self):
        self.chrome.find_element(*self.CURRENCY_DROPDOWN).click()

    def select_currency(self):
        self.chrome.find_element(*self.CURRENCY_OPTION).click()

    def get_selected_currency(self):
        return self.chrome.find_element(*self.SELECTED_CURRENCY).text

    def assert_currency_is_euro(self):
        selected_currency = self.get_selected_currency()
        assert selected_currency == " - Euro"