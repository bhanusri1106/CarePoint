
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.mediconnect_appointment_page import MediConnectAppointmentPage


def test_select_time_slot():
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

    appointment_page.enter_patient_uhid("UHID001")

    assert appointment_page.is_book_button_enabled()

    appointment_page.click_book_appointment()

    assert appointment_page.get_booked_title() == "Booked Appointments"

    driver.quit()
