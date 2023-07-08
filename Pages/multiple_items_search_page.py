from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MultipleItemsSearch(BasePage):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON2 = (By.ID, 'nav-search-submit-button')
    LAPTOP_RESULTS = (By.XPATH, '//span[text()='"laptop"']')
    HEADPHONES_RESULTS = (By.XPATH, '//span[text()='"headphones"']')
    SMARTPHONES_RESULTS =(By.XPATH, '//span[text()='"smartphone"']')

    def search_item(self, item):
        self.chrome.find_element(*self.SEARCH_INPUT).send_keys(item)

    def click_search_button2(self):
        self.chrome.find_element(*self.SEARCH_BUTTON2).click()

    def verify_search_results(self, items):
        for item in items:
            locator = None
            if item == "laptop":
                locator = self.LAPTOP_RESULTS
            elif item == "headphones":
                locator = self.HEADPHONES_RESULTS
            elif item == "smartphone":
                locator = self.SMARTPHONES_RESULTS
            else:
                raise ValueError(f"Unsupported item: {item}")

            WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(locator))
            assert self.chrome.find_element(*locator).is_displayed(), f"Search result not found for item: {item}"