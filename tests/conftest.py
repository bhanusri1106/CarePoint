import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from config.config import BASE_URL


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


@pytest.fixture
def driver(request):

    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError("Browser must be chrome or edge")

    driver.get(BASE_URL)

    WebDriverWait(driver, 10).until(
        lambda d: d.find_element("id", "forms-country")
    )

    yield driver

    driver.quit()