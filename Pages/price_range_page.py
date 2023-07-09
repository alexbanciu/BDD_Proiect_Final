from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PriceRangeFilter(BasePage):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    PRICE_FILTER_OPTION = (By.XPATH, "//span[contains(text(),'$50 to $100')]")
    CLOSE_ICON = (By.XPATH, '//*[@id="topRefinements/-1"]/ul/span/a/i')

    def search_item(self, item):
        search_input = self.chrome.find_element(*self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(item)
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def apply_price_filter(self):
        self.chrome.find_element(*self.PRICE_FILTER_OPTION).click()

    def click_close_icon(self):
        close_icon_element = self.chrome.find_elements(*self.CLOSE_ICON)
        if len(close_icon_element) > 0:
            close_icon_element[0].click()