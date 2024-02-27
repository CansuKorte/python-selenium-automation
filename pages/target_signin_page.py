from selenium.webdriver.common.by import By
from pages.base_page import Page


class TargetSigninPage(Page):
    SIGN_INTO_ACCOUNT_MSG = (By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")
    TERMS_CONDITIONS_HEADER = (By.CSS_SELECTOR, "[aria-label*='terms & conditions']")

    def verify_sign_into_account_msg(self):
        self.wait_element_visible(*self.SIGN_INTO_ACCOUNT_MSG)
        self.verify_text("Sign into your Target account", *self.SIGN_INTO_ACCOUNT_MSG)

    def click_terms_conditions_link(self):
        self.wait_element_clickable_click(*self.TERMS_CONDITIONS_HEADER)

    def verify_terms_conditions_page_opened(self):
        self.verify_partial_url("https://www.target.com/c/terms-conditions/")