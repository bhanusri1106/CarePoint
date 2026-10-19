import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.registration_page import RegistrationPage


def open_registration_page():

    driver = webdriver.Chrome()

    driver.get("https://www.qapractice.com/practice-forms")

    WebDriverWait(driver, 10).until(
        lambda d: d.find_element("id", "forms-country")
    )

    return driver


def test_first_name_required():

    driver = open_registration_page()
    registration_page = RegistrationPage(driver)

    registration_page.select_country("India")
    registration_page.select_title("Ms.")

    # First Name intentionally left empty
    registration_page.enter_last_name("Murata")
    registration_page.enter_dob("2000-05-12")
    registration_page.enter_doj("01/05/2026")
    registration_page.enter_email("myra@example.com")
    registration_page.select_phone_code("+91")
    registration_page.enter_phone_number("9876543210")
    registration_page.select_email_communication()

    registration_page.click_submit()

    time.sleep(1)

    # Success message should not appear
    success_message = driver.find_elements("id", "forms-success")

    assert len(success_message) == 0

    driver.quit()


def test_email_validation():

    driver = open_registration_page()
    registration_page = RegistrationPage(driver)

    registration_page.select_country("India")
    registration_page.select_title("Ms.")
    registration_page.enter_first_name("Myra")
    registration_page.enter_last_name("Murata")
    registration_page.enter_dob("2000-05-12")
    registration_page.enter_doj("01/05/2026")

    # Invalid email
    registration_page.enter_email("myra")

    registration_page.select_phone_code("+91")
    registration_page.enter_phone_number("9876543210")
    registration_page.select_email_communication()

    email = driver.find_element("id", "forms-email")

    is_valid = driver.execute_script(
        "return arguments[0].checkValidity();",
        email
    )

    assert is_valid is False

    driver.quit()


def test_phone_validation():

    driver = open_registration_page()
    registration_page = RegistrationPage(driver)

    registration_page.select_country("India")
    registration_page.select_title("Ms.")
    registration_page.enter_first_name("Myra")
    registration_page.enter_last_name("Murata")
    registration_page.enter_dob("2000-05-12")
    registration_page.enter_doj("01/05/2026")
    registration_page.enter_email("myra@example.com")
    registration_page.select_phone_code("+91")

    # Invalid phone number
    registration_page.enter_phone_number("123")

    registration_page.select_email_communication()

    # Get the entered phone number
    phone = driver.find_element("id", "forms-phone-number")
    phone_value = phone.get_attribute("value")

    # Phone number should contain exactly 10 digits
    assert len(phone_value) != 10

    driver.quit()


def test_phone_required():

    driver = open_registration_page()
    registration_page = RegistrationPage(driver)

    registration_page.select_country("India")
    registration_page.select_title("Ms.")
    registration_page.enter_first_name("Myra")
    registration_page.enter_last_name("Murata")
    registration_page.enter_dob("2000-05-12")
    registration_page.enter_doj("01/05/2026")
    registration_page.enter_email("myra@example.com")
    registration_page.select_phone_code("+91")

    # Phone number intentionally left empty

    registration_page.select_email_communication()

    phone = driver.find_element("id", "forms-phone-number")

    # Verify phone field is empty
    assert phone.get_attribute("value") == ""

    driver.quit()


def test_dob_required():

    driver = open_registration_page()
    registration_page = RegistrationPage(driver)

    registration_page.select_country("India")
    registration_page.select_title("Ms.")
    registration_page.enter_first_name("Myra")
    registration_page.enter_last_name("Murata")

    # DOB intentionally left empty

    registration_page.enter_doj("01/05/2026")
    registration_page.enter_email("myra@example.com")
    registration_page.select_phone_code("+91")
    registration_page.enter_phone_number("9876543210")
    registration_page.select_email_communication()

    dob = driver.find_element("id", "forms-dob")

    # Verify DOB field is empty
    assert dob.get_attribute("value") == ""

    driver.quit()