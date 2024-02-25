from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.XPATH, "//div[@data-test='boxEmptyMsg']")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    EMPTY_CART_MSG = 'Your cart is empty'  # not a locator!
    # if we have a lot of texts for verification, we can store them here in variables - not very common tho.

# ------------------------------------------------------------------------------------------------------------------
    # MY VERSION
    # def verify_cart_empty_msg(self, expected_msg):
    #     actual_text = self.find_element(*self.CART_EMPTY_MSG).text
    #     assert expected_msg in actual_text, f'Expected msg {expected_msg} not in {actual_text}'

    # Instructor version;
    # def verify_cart_empty_msg(self):
    #     actual_text = self.find_element(*self.CART_EMPTY_MSG).text
    #     assert 'Your cart is empty' == actual_text, f'Expected 'Your cart is empty' but got {actual_text}'
# ------------------------------------------------------------------------------------------------------------------

    # Then she changed it after creating a verify function in base page;

    # def verify_cart_empty_msg(self):
    #     expected_text = 'Your cart is empty'     # --> or pass it to the function below
    #     self.verify_text(expected_text, *self.CART_EMPTY_MSG)
    #     # or self.verify_text(expected_text: 'Your cart is empty', *locator: *self.CART_EMPTY_MSG)

    # If CART EMPTY MSG can't load fast, your test can fail, so we should put wait_element_visible function here;
    def verify_cart_empty_msg(self):
        self.wait_element_visible(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty',  *self.CART_EMPTY_MSG)

    def verify_cart_item_correct(self):
        self.wait_element_visible(*self.CART_ITEM_TITLE)
        self.verify_text('22" Terracotta Ceramic Table Lamp - Nourison',  *self.CART_ITEM_TITLE)
