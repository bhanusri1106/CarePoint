from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AppointmentPage(BasePage):

    # Locators
    appointment_date = (By.ID, "forms-doj")
    patient_name = (By.ID, "forms-first-name")
    patient_email = (By.ID, "forms-email")
    confirm_button = (By.ID, "forms-submit")

    def enter_date(self, date):
        self.enter_text(self.appointment_date, date)

    def enter_patient_name(self, name):
        self.enter_text(self.patient_name, name)

    def enter_patient_email(self, email):
        self.enter_text(self.patient_email, email)

    def click_confirm(self):
        element = self.find_element(self.confirm_button)
        self.driver.execute_script(
            "arguments[0].click();", element
        )