import allure

from test_ui.base_page import BasePage
from test_ui.locators import Locators


@allure.suite('Login Page')
class DynamicLoadingPage(BasePage):
    locators = Locators()

    @allure.step('Click example 1.')
    def click_example_1(self):
        self.element_is_present_and_clickable(self.locators.EXAMPLE_1).click()

    @allure.step('Click start button.')
    def click_start_button(self):
        self.element_is_present_and_clickable(self.locators.BUTTON_START).click()

    @allure.step('Get expected text.')
    def get_expected_text(self):
        return self.element_is_visible(self.locators.EXPECTED_TEXT).text

    @allure.step('Click example 2.')
    def click_example_2(self):
        self.element_is_present_and_clickable(self.locators.EXAMPLE_2).click()
