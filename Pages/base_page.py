from browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Browser):

    def wait_and_click_element(self, selector):
        WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(*selector))
        self.chrome.find_element(*selector).click()