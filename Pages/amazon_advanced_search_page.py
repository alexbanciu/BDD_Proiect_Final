from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class AdvancedSearchPage(BasePage):
    SELECT_DEPARTMENTS = (By.XPATH, "(//span[text()='Computers & Accessories'])[2]")
    SELECT_PRICE = (By.XPATH, "//span[text()='$100 to $200']")
    SELECT_REVIEW_RATING = (By.XPATH, "(//span[@role='text'])[1]")
    SELECT_DISCOUNT = (By.XPATH, "//span[text()='10% off or more']")
    CLEAR_BUTTON = (By.XPATH, "//li[@data-csa-c-element-id='filter-department-all']//a[1]")

    def select_departments(self):
        self.chrome.find_element(*self.SELECT_DEPARTMENTS).click()

    def select_price(self):
        self.chrome.find_element(*self.SELECT_PRICE).click()

    def select_review_rating(self):
        self.chrome.find_element(*self.SELECT_REVIEW_RATING).click()

    def select_discount(self):
        self.chrome.find_element(*self.SELECT_DISCOUNT).click()

    def select_first_product(self):
        self.chrome.find_element(*self.CLEAR_BUTTON).click()