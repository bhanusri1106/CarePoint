
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.doctor_directory_page import DoctorDirectoryPage


def test_cardiology_doctor_filter():
    driver = webdriver.Chrome()

    driver.get("https://www.testerrank.com/hospital/login")

    driver.find_element(By.ID, "email").send_keys("patient@mediconnect.com")
    driver.find_element(By.ID, "password").send_keys("Medi@123")
    driver.find_element(By.ID, "loginBtn").click()

    driver.get("https://www.testerrank.com/hospital/doctors")

    doctor_page = DoctorDirectoryPage(driver)

    doctor_page.select_department("Cardiology")

    doctor_name = doctor_page.get_first_doctor()

    assert doctor_name == "Dr. Vikram Singh"

    doctor_page.click_first_doctor()

    schedule_name = doctor_page.get_schedule_doctor_name()

    assert schedule_name == "Dr. Vikram Singh"

    driver.quit()
