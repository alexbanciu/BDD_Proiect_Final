from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class AmazonMusic(BasePage):
    ALL_BUTTON = (By.XPATH, "//i[@class='hm-icon nav-sprite']")
    AMAZON_MUSIC_BUTTON = (By.XPATH, "//div[normalize-space()='Amazon Music']")
    FREE_STREAMING_MUSIC_BUTTON = (By.XPATH, "//a[normalize-space()='Free Streaming Music']")
    LISTEN_NOW_BUTTON = (By.XPATH, '//*[@id="15"]/span/span/a/span')

    def click_all_button(self):
        self.chrome.find_element(*self.ALL_BUTTON).click()

    def click_amazon_music_button(self):
        self.chrome.find_element(*self.AMAZON_MUSIC_BUTTON).click()

    def click_free_streaming_music_button(self):
        self.chrome.find_element(*self.FREE_STREAMING_MUSIC_BUTTON).click()

    def click_listen_now_button(self):
        self.chrome.find_element(*self.LISTEN_NOW_BUTTON).click()

    def verify_redirected_link(self):
        current_url = self.chrome.current_url
        expected_url = "https://music.amazon.com/?ref=dm_lnd_nw_listn_e909a690_nav_em__dm_nav_nw_0_2_2_3"

        if expected_url != current_url:
            print("User is redirected to the expected Amazon Streaming Music page")
        else:
            raise AssertionError(f"Expected redirection to '{expected_url}', but got '{current_url}'")

    def return_to_homepage(self):
        self.chrome.get('https://www.amazon.com/')
        sleep(3)