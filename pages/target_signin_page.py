from selenium.webdriver.common.by import By
from pages.base_page import Page


class TargetSigninPage(Page):
    SIGN_INTO_ACCOUNT_MSG = (By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")

    def verify_sign_into_account_msg(self):
        self.wait_element_visible(*self.SIGN_INTO_ACCOUNT_MSG)
        self.verify_text("Sign into your Target account", *self.SIGN_INTO_ACCOUNT_MSG)