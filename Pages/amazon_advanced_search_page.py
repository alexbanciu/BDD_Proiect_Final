from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class AdvancedSearchPage(BasePage):
    SELECT_DEPARTMENTS = (By.XPATH, '//*[@id="grid-main-container"]/div[2]/span[3]/ul/li[14]/label/span')
    SELECT_PRICE = (By.XPATH, '//*[@id="grid-main-container"]/div[2]/span[5]/ul/li[5]/div/a/span')
    SELECT_REVIEW_RATING = (By.XPATH, '//*[@id="grid-main-container"]/div[2]/span[7]/ul/li[1]/div/a/span/span/span')
    SELECT_DISCOUNT = (By.XPATH, '//*[@id="grid-main-container"]/div[2]/span[6]/ul/li[2]/div/a/span')
    CLEAR_BUTTON = (By.XPATH, '//*[@id="grid-main-container"]/div[2]/span[3]/li/a')

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