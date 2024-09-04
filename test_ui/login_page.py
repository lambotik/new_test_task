import allure

from test_ui.base_page import BasePage
from test_ui.locators import Locators


@allure.suite('Login Page')
class LoginPage(BasePage):
    locators = Locators()

    @allure.step('Input username.')
    def input_login(self, user_name):
        self.element_is_visible(self.locators.INPUT_USER_NAME).send_keys(user_name)

    @allure.step('Input password.')
    def input_password(self, password):
        self.element_is_visible(self.locators.INPUT_PASSWORD).send_keys(password)

    @allure.step('Click login button.')
    def click_login_button(self):
        self.element_is_present_and_clickable(self.locators.BUTTON_LOGIN).click()

    @allure.step('Get alert message.')
    def get_alert_text(self):
        alert_text = self.element_is_visible(self.locators.ALERT_MESSAGE).text
        alert_text = alert_text.replace('\n×', '')
        with allure.step(f'Alert message is: {alert_text}'):
            return alert_text

    @allure.step('Click logout button.')
    def click_logout_button(self):
        self.element_is_present_and_clickable(self.locators.BUTTON_LOGOUT).click()
