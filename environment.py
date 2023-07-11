from Pages.add_to_cart_page import CartPage
from Pages.amazon_music_page import AmazonMusic
from Pages.amazon_sign_up_page import SignUpPage
from Pages.currency_page import CurrencyPage
from Pages.logo_page import LogoIsDisplayed
from Pages.price_range_page import PriceRangeFilter
from Pages.sign_in_page import SignInPage
from Pages.title_page import TitlePage
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
    context.sign_in_object = SignInPage()
    context.add_to_cart_object = CartPage()
    context.currency_page_object = CurrencyPage()
    context.logo_is_displayed = LogoIsDisplayed()
    context.title_page_object = TitlePage()


def after_all(context):
    context.browser.close()