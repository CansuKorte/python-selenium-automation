from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
    SIGNIN_HEADER = (By.XPATH,"//a[@data-test='@web/AccountLink']")

    def search_product(self):
        self.input_text('22" Terracotta Ceramic Table Lamp - Nourison', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

    def click_cart_icon(self):
        self.wait_element_clickable_click(*self.CART_ICON)
        # self.click(*self.CART_ICON)

    # To make your test case more stable, instead of relying on click function you can wait until the element
    # is in the clickable state and then click on it, so you can put wait_element function above

    def click_signin(self):
        self.click(*self.SIGNIN_HEADER)
