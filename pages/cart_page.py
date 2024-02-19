from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.XPATH, "//div[@data-test='boxEmptyMsg']")

    def verify_cart_empty_msg(self, expected_msg):
        actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        assert expected_msg in actual_text, f'Expected msg {expected_msg} not in {actual_text}'
