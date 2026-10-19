import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.registration_page import RegistrationPage


def test_valid_registration():

    driver = webdriver.Chrome()

    driver.get("https://www.qapractice.com/practice-forms")

    WebDriverWait(driver, 10).until(
        lambda d: d.find_element("id", "forms-country")
    )

    registration_page = RegistrationPage(driver)

    # Country
    registration_page.select_country("India")

    # Title
    registration_page.select_title("Ms.")

    # First Name
    registration_page.enter_first_name("Myra")

    # Last Name
    registration_page.enter_last_name("Murata")

    # Date of Birth
    registration_page.enter_dob("2000-05-12")

    # Date of Joining
    registration_page.enter_doj("01/05/2026")

    # Email
    registration_page.enter_email("myra@example.com")

    # Phone Code
    registration_page.select_phone_code("+91")

    # Phone Number
    registration_page.enter_phone_number("9876543210")

    # Preferred Communication
    registration_page.select_email_communication()

    # Submit
    registration_page.click_submit()

    time.sleep(2)

    driver.quit()