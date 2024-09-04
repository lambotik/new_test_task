from selenium.webdriver.common.by import By


class Locators:
    # Login Page
    INPUT_USER_NAME = (By.XPATH, '//input[@id="username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@id="password"]')
    BUTTON_LOGIN = (By.XPATH, '//button[@class="radius"]')
    ALERT_MESSAGE = (By.XPATH, '//div[@id="flash"]')
    BUTTON_LOGOUT = (By.XPATH, '//a[@class="button secondary radius"]')

    # Dynamic loading page
    EXAMPLE_1 = (By.XPATH, '//a[@href="/dynamic_loading/1"]')
    BUTTON_START = (By.XPATH, '//div[@id="start"]/button')
    EXPECTED_TEXT = (By.XPATH, '//div[@id="finish"]/h4')
    EXAMPLE_2 = (By.XPATH, '//a[@href="/dynamic_loading/2"]')
