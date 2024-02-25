from selenium.webdriver.common.by import By
from pages.base_page import Page


class SideNavigation(Page):
    SIDE_NAV_SIGNIN_HEADER = (By.XPATH, "//a[@data-test='accountNav-signIn']")
    SIDE_NAV_ADD_TO_CART = (By.CSS_SELECTOR, "[data-test='shippingButton']")
    SIDE_NAV_PRODUCT_NAME = (By.XPATH, "//h4[contains(@class, 'styles__StyledHeading')]")
    SIDE_NAV_PREVIOUS_ICON = (By.CSS_SELECTOR, "[aria-label='Previous']")

    def click_side_nav_signin(self):
        self.click(*self.SIDE_NAV_SIGNIN_HEADER)

    def click_side_nav_add_to_cart(self):
        self.click(*self.SIDE_NAV_ADD_TO_CART)

    def store_product_name(self):
        self.wait_element_visible(*self.SIDE_NAV_PRODUCT_NAME)
        self.verify_text('22" Terracotta Ceramic Table Lamp - Nourison', *self.SIDE_NAV_PRODUCT_NAME)

    def click_side_nav_previous_icon(self):
        self.click(*self.SIDE_NAV_PREVIOUS_ICON)