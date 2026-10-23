# CarePoint – Project Development Log

## Day 1 – Selenium Setup and Basic Tests

- Set up Selenium WebDriver with Python.
- Created the first Selenium test.
- Created the registration test.
- Created validation tests for required and invalid fields.
- Practiced locating elements using different Selenium locators.
- Ran the test suite.
- Result: **6/6 tests passed.**

## Day 2 – Page Object Model

- Introduced the Page Object Model (POM).
- Created `RegistrationPage`.
- Moved page locators and actions from the test files into the page class.
- Updated the test files to use the page object.
- This made the test code simpler and easier to maintain.
- Result: **6/6 tests passed.**

## Day 3 – Test Data, Configuration and Reusable Components

- Created `data/test_data.json` for test data.
- Moved registration data from the test code to the JSON file.
- Created `config/config.py` for the website URL.
- Updated tests to use `BASE_URL`.
- Created `pages/base_page.py` with reusable Selenium methods.
- Updated `RegistrationPage` to inherit from `BasePage`.
- Created `tests/conftest.py` for the reusable pytest driver fixture.
- Updated registration and validation tests to use the `driver` fixture.
- Ran the complete test suite.
- Result: **6/6 tests passed.**

## Day 4 – HTML Test Reporting

- Installed and used `pytest-html` to generate HTML test reports.
- Generated an HTML test report for the test suite.
- Verified the test results and execution details in the report.
- Added `reports/` to `.gitignore` so generated reports are not tracked by Git.
- Ran the complete test suite.
- Result: **6/6 tests passed.**

## Day 5 – Cross-Browser Testing

- Updated `conftest.py` to support browser selection.
- Added the `--browser` option to pytest.
- Tested the registration test on Chrome and Edge.
- Ran the complete test suite on both browsers.
- Chrome: **6/6 tests passed.**
- Edge: **6/6 tests passed.**

## Day 6 – Reusable Base Page Methods

- Improved `BasePage` with reusable Selenium methods.
- Added common methods for finding elements, clicking, entering text, selecting values, and getting text.
- Updated `RegistrationPage` to use these reusable methods.
- Ran the complete test suite after the changes.
- Result: **6/6 tests passed.**

## Day 7 – Doctor Directory and Doctor Filter

### Objective

To automate doctor-related interactions using Selenium and pytest.

### Work Completed

- Created `pages/doctor_directory_page.py`.
- Automated department selection in the doctor directory.
- Created `tests/test_03_doctor_directory.py`.
- Created `pages/doctor_filter_page.py`.
- Automated filtering of doctors based on department.
- Created `tests/test_04_doctor_filter.py`.
- Used Page Object Model for the doctor-related tests.
- Verified the selected department and filtered doctor results.
- Ran the tests successfully.

### Test Result

Doctor directory and doctor filter tests passed successfully.

## Day 8 – Appointment Booking Flow

### Objective

To automate an appointment booking workflow using Selenium and pytest.

### Work Completed

- Created `pages/appointment_page.py` for the appointment booking workflow.
- Added reusable methods for entering appointment date and patient details.
- Created `tests/test_05_appointment.py`.
- Automated appointment date entry.
- Automated patient details entry.
- Automated form submission.
- Added an assertion to verify the success message after submission.
- Tested the appointment workflow using Chrome.
- Tested the appointment workflow using Edge.
- Ran the complete test suite.
- Result: **9/9 tests passed.**

## Day 9 – MediConnect Appointment Booking

### Objective

To automate a complete hospital appointment booking flow using Selenium and pytest.

### Website

MediConnect hospital appointment website.

### Work Completed

- Created `pages/mediconnect_appointment_page.py`.
- Identified the Department dropdown.
- Automated department selection.
- Automated doctor selection.
- Automated appointment date entry.
- Automated time-slot selection.
- Automated patient UHID entry.
- Verified that the **Book Appointment** button becomes enabled after entering the required details.
- Automated appointment booking.
- Verified the booked appointment section.
- Created `tests/test_06_mediconnect_appointment.py`.
- Ran the test successfully.

### Test Result

MediConnect appointment test passed successfully.

## Day 10 – MediConnect Validation Testing

### Objective

To verify validation behavior on the MediConnect appointment form.

### Work Completed

- Created `tests/test_07_mediconnect_validation.py`.
- Tested the required validation for the Patient UHID field.
- Verified that the appointment form does not allow booking when the required UHID is empty.
- Used Selenium assertions to verify the validation behavior.
- Ran the complete test suite.

### Test Result

MediConnect validation test passed successfully.

## Additional Practice – DemoQA Date Picker

### Objective

To practice automating date selection using a separate date-picker website.

### Website

DemoQA Date Picker

### Work Completed

- Created `DemoQADatePage` using the Page Object Model.
- Added a locator for the date input field.
- Added a method to enter the date.
- Created `tests/test_08_demoqa_date.py`.
- Verified that the selected date is displayed correctly.
- This test was created as additional practice for handling date fields.

### Test Result

DemoQA Date Picker test passed successfully.

## Final Test Suite

The project was finally organized into **12 automated tests** covering registration, form validation, doctor selection, doctor filtering, appointment booking, date selection and MediConnect validation.

The final test execution resulted in:

- **12 tests passed**
- **0 failed**
- **0 skipped**
- **0 errors**
- **100% pass rate**

### Final Test Order

1. `test_01_registration.py` – Registration
2. `test_02_validation.py` – Form validation
3. `test_03_doctor_directory.py` – Doctor directory
4. `test_04_doctor_filter.py` – Doctor filter
5. `test_05_appointment.py` – Appointment booking
6. `test_06_mediconnect_appointment.py` – MediConnect appointment
7. `test_07_mediconnect_validation.py` – MediConnect validation
8. `test_08_demoqa_date.py` – DemoQA date picker

### Websites Used

The project started with one practice website for the initial Selenium, registration and validation tests. Later, additional websites were used to practice different automation scenarios:

1. **Test website** – Registration, form validation, doctor directory, doctor filtering and appointment booking.
2. **MediConnect hospital website** – Department, doctor, date, time-slot, UHID and appointment booking validation.
3. **DemoQA** – Date picker automation practice.

Using multiple websites helped practice different types of Selenium interactions while keeping the same Page Object Model and pytest structure.