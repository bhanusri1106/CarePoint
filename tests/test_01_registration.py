import json

from pages.registration_page import RegistrationPage


with open("data/test_data.json", "r") as file:
    test_data = json.load(file)


def test_valid_registration(driver):

    registration_page = RegistrationPage(driver)

    # Country
    registration_page.select_country(
        test_data["valid_user"]["country"]
    )

    # Title
    registration_page.select_title(
        test_data["valid_user"]["title"]
    )

    # First Name
    registration_page.enter_first_name(
        test_data["valid_user"]["first_name"]
    )

    # Last Name
    registration_page.enter_last_name(
        test_data["valid_user"]["last_name"]
    )

    # Date of Birth
    registration_page.enter_dob(
        test_data["valid_user"]["dob"]
    )

    # Date of Joining
    registration_page.enter_doj(
        test_data["valid_user"]["doj"]
    )

    # Email
    registration_page.enter_email(
        test_data["valid_user"]["email"]
    )

    # Phone Code
    registration_page.select_phone_code(
        test_data["valid_user"]["phone_code"]
    )

    # Phone Number
    registration_page.enter_phone_number(
        test_data["valid_user"]["phone_number"]
    )

    # Preferred Communication
    registration_page.select_email_communication()

    # Submit
    registration_page.click_submit()