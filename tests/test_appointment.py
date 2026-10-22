from selenium.webdriver.common.by import By

from pages.appointment_page import AppointmentPage


def test_appointment_booking(driver):

    appointment_page = AppointmentPage(driver)

    appointment_page.enter_date("01/05/2026")
    appointment_page.enter_patient_name("Myra")
    appointment_page.enter_patient_email("myra@example.com")

    appointment_page.click_confirm()

    success_message = driver.find_element(
        By.XPATH,
        "//*[contains(text(), 'submitted') or contains(text(), 'success')]"
    )

    assert success_message.is_displayed()