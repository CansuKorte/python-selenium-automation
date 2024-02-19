from pages.base_page import Page
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)


# instead of individually connecting to every page in our environment,
# we will connect to the actual Application via environment.py file
# app = Application(driver)
# app.search_results_page.open()
# app.main_page.open()
