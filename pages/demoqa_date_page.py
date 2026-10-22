from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class DemoQADatePage(BasePage):

    date_input = (By.ID, "datePickerMonthYearInput")

    def enter_date(self, date):
        element = self.find_element(self.date_input)
        element.click()
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(date)