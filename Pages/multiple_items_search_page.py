from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MultipleItemsSearch(BasePage):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON2 = (By.ID, 'nav-search-submit-button')

    def search_item(self, item):
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys(item)

    def click_search_button2(self):
        self.chrome.find_element(*self.SEARCH_BUTTON2).click()