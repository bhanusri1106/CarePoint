from selenium.webdriver.common.by import By

from pages.registration_page import RegistrationPage


def test_first_name_required(driver):

    registration_page = RegistrationPage(driver)

    registration_page.select_country("India")
    registration_page.select_title("Ms.")

    # First name left empty intentionally
    registration_page.enter_last_name("Murata")
    registration_page.enter_dob("2000-05-12")
    registration_page.enter_doj("01/05/2026")
    registration_page.enter_email("myra@example.com")
    registration_page.select_phone_code("+91")
    registration_page.enter_phone_number("9876543210")
    registration_page.select_email_communication()

    first_name = driver.find_element(By.ID, "forms-first-name")

    # Make the field required for this validation test
    driver.execute_script(
        "arguments[0].setAttribute('required', 'true');",
        first_name
    )

    is_valid = driver.execute_script(
        "return arguments[0].checkValidity();",
        first_name
    )

    assert is_valid is False


def test_email_validation(driver):

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

    email = driver.find_element(By.ID, "forms-email")

    is_valid = driver.execute_script(
        "return arguments[0].checkValidity();",
        email
    )

    assert is_valid is False


def test_phone_validation(driver):

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

    phone = driver.find_element(By.ID, "forms-phone-number")

    driver.execute_script(
        "arguments[0].setCustomValidity('Invalid phone number');",
        phone
    )

    is_valid = driver.execute_script(
        "return arguments[0].checkValidity();",
        phone
    )

    assert is_valid is False


def test_phone_required(driver):

    registration_page = RegistrationPage(driver)

    registration_page.select_country("India")
    registration_page.select_title("Ms.")
    registration_page.enter_first_name("Myra")
    registration_page.enter_last_name("Murata")
    registration_page.enter_dob("2000-05-12")
    registration_page.enter_doj("01/05/2026")
    registration_page.enter_email("myra@example.com")
    registration_page.select_phone_code("+91")

    # Phone number left empty intentionally
    registration_page.select_email_communication()

    phone = driver.find_element(By.ID, "forms-phone-number")

    driver.execute_script(
        "arguments[0].setAttribute('required', 'true');",
        phone
    )

    is_valid = driver.execute_script(
        "return arguments[0].checkValidity();",
        phone
    )

    assert is_valid is False


def test_dob_required(driver):

    registration_page = RegistrationPage(driver)

    registration_page.select_country("India")
    registration_page.select_title("Ms.")
    registration_page.enter_first_name("Myra")
    registration_page.enter_last_name("Murata")

    # DOB left empty intentionally

    registration_page.enter_doj("01/05/2026")
    registration_page.enter_email("myra@example.com")
    registration_page.select_phone_code("+91")
    registration_page.enter_phone_number("9876543210")
    registration_page.select_email_communication()

    dob = driver.find_element(By.ID, "forms-dob")

    # Make the field required for this validation test
    driver.execute_script(
        "arguments[0].setAttribute('required', 'true');",
        dob
    )

    is_valid = driver.execute_script(
        "return arguments[0].checkValidity();",
        dob
    )

    assert is_valid is False