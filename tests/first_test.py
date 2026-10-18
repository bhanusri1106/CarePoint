import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.qapractice.com/practice-forms")

# Wait for page
WebDriverWait(driver, 10).until(
    lambda d: d.find_element(By.ID, "forms-country")
)

# Country
country = driver.find_element(By.ID, "forms-country")
select_country = Select(country)
select_country.select_by_value("India")
print(select_country.first_selected_option.text)
time.sleep(1)

# Title
title = driver.find_element(By.ID, "forms-title")
select_title = Select(title)
select_title.select_by_value("Ms.")
print(select_title.first_selected_option.text)
time.sleep(1)

# First Name
first_name = driver.find_element(By.ID, "forms-first-name")
first_name.send_keys("Myra")
time.sleep(1)

# Last Name
last_name = driver.find_element(By.ID, "forms-last-name")
last_name.send_keys("Murata")
time.sleep(1)

# Date of Birth
dob = driver.find_element(By.ID, "forms-dob")
dob.send_keys("2000-05-12")
time.sleep(1)

# Date of Joining
doj = driver.find_element(By.ID, "forms-doj")
doj.send_keys("01/05/2026")
time.sleep(1)

# Email
email = driver.find_element(By.ID, "forms-email")
email.send_keys("myra@example.com")
time.sleep(1)

# Phone Country Code
phone_code = driver.find_element(By.ID, "forms-phone-code")
select_phone_code = Select(phone_code)
select_phone_code.select_by_value("+91")
print(select_phone_code.first_selected_option.text)

# Phone Number
phn_no = driver.find_element(By.ID, "forms-phone-number")
phn_no.send_keys("9876543210")
time.sleep(2)

# Preferred Communication
communication = driver.find_element(
    By.CSS_SELECTOR, "[data-testid='forms-comm-email']"
)

driver.execute_script("arguments[0].click();", communication)

print(communication.is_selected())
time.sleep(1)

# Submit
submit = driver.find_element(By.ID, "forms-submit")
print(submit.is_enabled())

driver.execute_script("arguments[0].click();", submit)
time.sleep(2)