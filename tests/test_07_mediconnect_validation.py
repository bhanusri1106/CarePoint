
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.mediconnect_appointment_page import MediConnectAppointmentPage


def test_empty_uhid_validation():
    driver = webdriver.Chrome()

    driver.get("https://www.testerrank.com/hospital/login")

    driver.find_element(By.ID, "email").send_keys(
        "patient@mediconnect.com"
    )
    driver.find_element(By.ID, "password").send_keys(
        "Medi@123"
    )
    driver.find_element(By.ID, "loginBtn").click()

    driver.get("https://www.testerrank.com/hospital/appointments")

    appointment_page = MediConnectAppointmentPage(driver)

    appointment_page.select_department("Cardiology")
    appointment_page.select_doctor("Dr. Vikram Singh")
    appointment_page.enter_date("2026-12-05")
    appointment_page.select_time_slot()

    # UHID is left empty
    assert not appointment_page.is_book_button_enabled()

    driver.quit()
