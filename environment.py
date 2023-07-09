from Pages.amazon_music_page import AmazonMusic
from Pages.amazon_sign_up_page import SignUpPage
from Pages.price_range_page import PriceRangeFilter
from browser import Browser
from Pages.amazon_homepage import HomePage
from Pages.amazon_advanced_search_page import AdvancedSearchPage


def before_all(context):
    context.browser = Browser()
    context.home_page_object = HomePage()
    context.advanced_search_object = AdvancedSearchPage()
    context.sign_up_page_object = SignUpPage()
    context.amazon_music_object = AmazonMusic()
    context.price_range_object = PriceRangeFilter()
    context.homepage_elements_object = PriceRangeFilter()


def after_all(context):
    context.browser.close()