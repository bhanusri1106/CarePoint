from selenium import webdriver

from pages.demoqa_date_page import DemoQADatePage


def test_demoqa_date_picker():

    driver = webdriver.Chrome()

    driver.get("https://demoqa.com/date-picker")

    date_page = DemoQADatePage(driver)

    date_page.enter_date("12/05/2026")

    date_input = driver.find_element(
        "id",
        "datePickerMonthYearInput"
    )

    assert date_input.get_attribute("value") == "12/05/2026"

    driver.quit()