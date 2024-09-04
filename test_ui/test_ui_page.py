import time

import allure

from test_ui.dynamic_loading_page import DynamicLoadingPage
from test_ui.links import TestDataLinks
from test_ui.login_page import LoginPage


@allure.epic("UI.")
class TestLoginPage:

    @allure.title('test_positive_login')
    def test_positive_login(self, driver):
        page = LoginPage(driver, TestDataLinks.login_page)
        page.open()
        page.input_login('tomsmith')
        page.input_password('SuperSecretPassword!')
        page.click_login_button()
        login_alert_text = page.get_alert_text()
        assert login_alert_text == 'You logged into a secure area!', 'Incorrect alert message.'
        page.click_logout_button()
        logout_alert_text = page.get_alert_text()
        assert logout_alert_text == 'You logged out of the secure area!', 'Incorrect alert message.'

    @allure.title('test_negative_login')
    def test_negative_login(self, driver):
        page = LoginPage(driver, TestDataLinks.login_page)
        page.input_login('lambotik')
        page.input_password('lambotik')
        page.click_login_button()
        login_alert_text = page.get_alert_text()
        assert login_alert_text == 'Your username is invalid!', 'Incorrect alert message.'


class TestDynamicPage:

    @allure.title('test_dynamic_page_example_1')
    def test_dynamic_page_example_1(self, driver):
        page = DynamicLoadingPage(driver, TestDataLinks.dynamic_loading_page)
        page.open()
        page.click_example_1()
        page.click_start_button()
        expected_text = page.get_expected_text()
        assert expected_text == 'Hello World!', 'Incorrect text.'

    @allure.title('test_dynamic_page_example_2')
    def test_dynamic_page_example_2(self, driver):
        page = DynamicLoadingPage(driver, TestDataLinks.dynamic_loading_page)
        page.open()
        page.click_example_2()
        page.click_start_button()
        expected_text = page.get_expected_text()
        assert expected_text == 'Hello World!', 'Incorrect text.'
