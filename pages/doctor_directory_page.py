
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class DoctorDirectoryPage(BasePage):

    department_filter = (By.ID, "deptFilter")
    first_doctor = (By.ID, "docName0")
    schedule_doctor_name = (By.ID, "scheduleDocName")

    def select_department(self, department):
        dropdown = self.driver.find_element(*self.department_filter)
        Select(dropdown).select_by_value(department)

    def get_first_doctor(self):
        return self.get_text(self.first_doctor)

    def click_first_doctor(self):
        self.click(self.first_doctor)

    def get_schedule_doctor_name(self):
        return self.get_text(self.schedule_doctor_name)