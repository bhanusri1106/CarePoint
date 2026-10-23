
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class MediConnectAppointmentPage(BasePage):

    department = (By.ID, "department")
    doctor = (By.ID, "doctorSelect")
    appointment_date = (By.ID, "appointmentDate")
    time_slot = (By.ID, "slot0900")
    patient_uhid = (By.ID, "patientUhid")
    book_appointment = (By.ID, "bookAppointmentBtn")
    booked_title = (By.ID, "bookedTitle")

    def select_department(self, department_name):
        dropdown = self.driver.find_element(*self.department)
        Select(dropdown).select_by_visible_text(department_name)

    def select_doctor(self, doctor_name):
        dropdown = self.driver.find_element(*self.doctor)
        Select(dropdown).select_by_visible_text(
            doctor_name + " (MBBS, DM Cardiology)"
        )

    def enter_date(self, date):
        date_input = self.driver.find_element(*self.appointment_date)

        self.driver.execute_script(
            """
            const input = arguments[0];
            const value = arguments[1];

            const setter = Object.getOwnPropertyDescriptor(
                HTMLInputElement.prototype,
                'value'
            ).set;

            setter.call(input, value);

            input.dispatchEvent(new Event('input', { bubbles: true }));
            input.dispatchEvent(new Event('change', { bubbles: true }));
            input.blur();
            """,
            date_input,
            date
        )

    def select_time_slot(self):
        self.driver.find_element(*self.time_slot).click()

    def enter_patient_uhid(self, uhid):
        self.driver.find_element(*self.patient_uhid).send_keys(uhid)

    def is_book_button_enabled(self):
        return self.driver.find_element(*self.book_appointment).is_enabled()

    def click_book_appointment(self):
        self.driver.find_element(*self.book_appointment).click()

    def get_booked_title(self):
        return self.driver.find_element(*self.booked_title).text