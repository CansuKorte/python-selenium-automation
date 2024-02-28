from pages.base_page import Page
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.main_page import MainPage
from pages.header import Header
from pages.help_page import HelpPage
from pages.search_results_page import SearchResultsPage
from pages.side_navigation import SideNavigation
from pages.target_signin_page import TargetSigninPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.header = Header(driver)
        self.help_page = HelpPage(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.side_navigation = SideNavigation(driver)
        self.target_signin_page = TargetSigninPage(driver)

# Good practice to list pages in alphabetical order

# instead of individually connecting to every page in our environment,
# we will connect to the actual Application via environment.py file
# app = Application(driver)
# app.search_results_page.open()
# app.main_page.open()
