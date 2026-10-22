import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from config.config import BASE_URL


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.get(BASE_URL)

    WebDriverWait(driver, 10).until(
        lambda d: d.find_element("id", "forms-country")
    )

    yield driver

    driver.quit()