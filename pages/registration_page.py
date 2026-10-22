from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegistrationPage(BasePage):

    # Locators
    country = (By.ID, "forms-country")
    title = (By.ID, "forms-title")
    first_name = (By.ID, "forms-first-name")
    last_name = (By.ID, "forms-last-name")
    dob = (By.ID, "forms-dob")
    doj = (By.ID, "forms-doj")
    email = (By.ID, "forms-email")
    phone_code = (By.ID, "forms-phone-code")
    phone_number = (By.ID, "forms-phone-number")

    communication_email = (
        By.CSS_SELECTOR,
        "[data-testid='forms-comm-email']"
    )

    submit_button = (By.ID, "forms-submit")

    def select_country(self, country):
        self.select_by_value(self.country, country)

    def select_title(self, title):
        self.select_by_value(self.title, title)

    def enter_first_name(self, first_name):
        self.enter_text(self.first_name, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.last_name, last_name)

    def enter_dob(self, dob):
        self.enter_text(self.dob, dob)

    def enter_doj(self, doj):
        self.enter_text(self.doj, doj)

    def enter_email(self, email):
        self.enter_text(self.email, email)

    def select_phone_code(self, phone_code):
        self.select_by_value(self.phone_code, phone_code)

    def enter_phone_number(self, phone_number):
        self.enter_text(self.phone_number, phone_number)

    def select_email_communication(self):
        element = self.find_element(self.communication_email)
        self.driver.execute_script(
            "arguments[0].click();", element
        )

    def click_submit(self):
        element = self.find_element(self.submit_button)
        self.driver.execute_script(
            "arguments[0].click();", element
        )