from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep


class CartPage(Browser):
    SEARCH_TEXTBOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    FIRST_RESULT = (By.CSS_SELECTOR,
                    "div#search>div>div>div>span>div>div:nth-of-type(4)>div>div>div>div>div>div>div>div:nth-of-type(2)>div>span>a>div>img")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    CART_ITEM_COUNT = (By.ID, "nav-cart-count")
    GO_TO_CART = (By.XPATH, "//a[@href='/cart?ref_=sw_gtc']")
    DELETE_FROM_CART =(By.XPATH, "//input[@name='submit.delete.fe7c6bc7-b6bd-4951-8ae7-5007f2feb00c']")

    def perform_search(self, cart_item):
        search_box = self.chrome.find_element(*self.SEARCH_TEXTBOX)
        search_box.clear()
        search_box.send_keys(cart_item)
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def select_first_product(self):
        self.chrome.find_element(*self.FIRST_RESULT).click()

    def add_to_cart(self):
        self.chrome.find_element(*self.ADD_TO_CART_BUTTON).click()

    def get_cart_item_count(self):
        cart_item_count_element = self.chrome.find_element(*self.CART_ITEM_COUNT)
        sleep(5)
        return int(cart_item_count_element.text)