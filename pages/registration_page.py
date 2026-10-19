from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class RegistrationPage:

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

    def __init__(self, driver):
        self.driver = driver

    def select_country(self, country):
        element = self.driver.find_element(*self.country)
        Select(element).select_by_value(country)

    def select_title(self, title):
        element = self.driver.find_element(*self.title)
        Select(element).select_by_value(title)

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)

    def enter_dob(self, dob):
        self.driver.find_element(*self.dob).send_keys(dob)

    def enter_doj(self, doj):
        self.driver.find_element(*self.doj).send_keys(doj)

    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def select_phone_code(self, phone_code):
        element = self.driver.find_element(*self.phone_code)
        Select(element).select_by_value(phone_code)

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number).send_keys(phone_number)

    def select_email_communication(self):
        element = self.driver.find_element(*self.communication_email)
        self.driver.execute_script(
            "arguments[0].click();", element
        )

    def click_submit(self):
        element = self.driver.find_element(*self.submit_button)
        self.driver.execute_script(
            "arguments[0].click();", element
        )