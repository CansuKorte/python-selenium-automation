from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='IdFor88889037']")

    def verify_search_results_correct(self, expected_result):
        self.verify_partial_text(expected_result, *self.SEARCH_RESULTS_HEADER)

        # actual_text = self.find_element(*self.SEARCH_RESULTS_HEADER).text
        # assert expected_result in actual_text, f'Expected word {expected_result} not in {actual_text}'

    def verify_search_results_page_url(self, expected_part_url):
        self.verify_partial_url(expected_part_url)

        # url = self.driver.current_url
        # assert expected_part_url in url, f'Expected word {expected_part_url} not in {url}'

    def click_add_to_cart(self):
        self.wait_element_clickable_click(*self.ADD_TO_CART_BUTTON)
