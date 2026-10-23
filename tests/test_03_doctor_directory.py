
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.doctor_directory_page import DoctorDirectoryPage


def test_select_department():
    driver = webdriver.Chrome()

    driver.get("https://www.testerrank.com/hospital/login")

    driver.find_element(By.ID, "email").send_keys("patient@mediconnect.com")
    driver.find_element(By.ID, "password").send_keys("Medi@123")
    driver.find_element(By.ID, "loginBtn").click()

    driver.get("https://www.testerrank.com/hospital/doctors")

    doctor_page = DoctorDirectoryPage(driver)

    doctor_page.select_department("Cardiology")

    dropdown = driver.find_element(By.ID, "deptFilter")
    selected = Select(dropdown).first_selected_option.text

    assert selected == "Cardiology"

    driver.quit()