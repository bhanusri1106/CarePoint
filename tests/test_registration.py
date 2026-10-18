import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_valid_registration():

    driver = webdriver.Chrome()
    driver.get("https://www.qapractice.com/practice-forms")

    # Country
    country = driver.find_element(By.ID, "forms-country")
    Select(country).select_by_value("India")

    # Title
    title = driver.find_element(By.ID, "forms-title")
    Select(title).select_by_value("Ms.")

    # First Name
    driver.find_element(By.ID, "forms-first-name").send_keys("Myra")

    # Last Name
    driver.find_element(By.ID, "forms-last-name").send_keys("Murata")

    # Date of Birth
    driver.find_element(By.ID, "forms-dob").send_keys("2000-05-12")

    # Date of Joining
    driver.find_element(By.ID, "forms-doj").send_keys("01/05/2026")

    # Email
    driver.find_element(By.ID, "forms-email").send_keys("myra@example.com")

    # Phone Code
    phone_code = driver.find_element(By.ID, "forms-phone-code")
    Select(phone_code).select_by_value("+91")

    # Phone Number
    driver.find_element(By.ID, "forms-phone-number").send_keys("9876543210")

    # Preferred Communication
    communication = driver.find_element(
        By.CSS_SELECTOR, "[data-testid='forms-comm-email']"
    )

    driver.execute_script("arguments[0].click();", communication)

    # Submit
    submit = driver.find_element(By.ID, "forms-submit")
    driver.execute_script("arguments[0].click();", submit)

    time.sleep(2)

    # Verify success
    success_message = driver.find_element(By.ID, "forms-success")

    assert success_message.is_displayed()

    driver.quit()