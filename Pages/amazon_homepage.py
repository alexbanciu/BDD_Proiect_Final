from Pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    SEARCH_TEXTBOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    SEARCH_CATEGORIES = (By.ID, 'searchDropdownBox')
    SEARCH_RESULTS = (By.XPATH, '//*[@id="search"]/span/div/h1/div/div[1]/div/div/span[1]')
    ADVANCED_SEARCH_LINK = (By.LINK_TEXT, "Today's Deals")

    def navigate_to_homepage(self):
        self.chrome.get("https://www.amazon.com/")

    def insert_search_value(self, product_name):
        self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys(product_name)

    def choose_category(self, category_name):
        category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
        category_dropdown.select_by_visible_text(category_name)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def check_search_results(self, nr_of_results):
        result = self.chrome.find_element(*self.SEARCH_RESULTS).text.split(" ")[-3].replace(",", "")
        assert int(result) >= int(nr_of_results),\
            f'Error: Results are incorrect. Expected: {nr_of_results}, Actual: {result}'

    def click_todays_deals(self):
        self.chrome.find_element(*self.ADVANCED_SEARCH_LINK).click()