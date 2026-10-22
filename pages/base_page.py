from selenium.webdriver.support.ui import Select


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def select_by_value(self, locator, value):
        Select(self.find_element(locator)).select_by_value(value)

    def get_text(self, locator):
        return self.find_element(locator).text