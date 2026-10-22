Day 1
- Selenium setup
- Created first test
- Created registration test
- Created validation tests
- 6 tests passed

Day 2
- Introduced Page Object Model
- Created RegistrationPage
- Moved locators/actions to page class
- Updated test files
- 6 tests passed

## Day 3 - Test Data, Configuration and Reusable Components

- Created `data/test_data.json` for test data.
- Moved registration data from the test code to JSON.
- Created `config/config.py` for the website URL.
- Updated tests to use `BASE_URL`.
- Created `pages/base_page.py` with reusable Selenium methods.
- Updated `RegistrationPage` to inherit from `BasePage`.
- Created `tests/conftest.py` for the reusable pytest driver fixture.
- Updated registration and validation tests to use the `driver` fixture.
- Ran the complete test suite.
- Result: 6/6 tests passed.

## Day 4 - HTML Test Reporting

- Created the `reports` folder for test reports.
- Generated an HTML test report using `pytest-html`.
- Created `CarePoint_Test_Report.hgit statustml`.
- Ran the complete test suite.
- Result: 6/6 tests passed.
- Added `reports/` to `.gitignore` so generated reports are not tracked by Git.

## Day 5 - Cross-Browser Testing

- Updated `conftest.py` to support browser selection.
- Added `--browser` option to pytest.
- Tested the registration test on Chrome and Edge.
- Ran the complete test suite on both browsers.
- Chrome: 6/6 tests passed.
- Edge: 6/6 tests passed.
## Day 6 - Reusable Base Page Methods

- Improved `BasePage` with reusable Selenium methods.
- Added common methods for finding elements, clicking, entering text, selecting values, and getting text.
- Updated `RegistrationPage` to use these reusable methods.
- Ran the complete test suite after the changes.
- Result: 6/6 tests passed.

### Day 7 - Appointment Booking Flow

- Created `pages/appointment_page.py` for the appointment booking workflow.
- Added reusable methods for entering appointment date and patient details.
- Created `tests/test_appointment.py` for appointment booking.
- Automated date, patient name, and email entry.
- Automated form submission.
- Added an assertion to verify the success message after submission.
- Tested the appointment workflow on Chrome.
- Tested the appointment workflow on Edge.
- Ran the complete test suite on Chrome.
- Result: **7/7 tests passed**.
- The practice website does not provide separate Specialty, Doctor, or Time Slot fields, so the available form fields were used as equivalent interactions.

## Day 8 – DemoQA Date Picker

### Objective
To automate date selection using the DemoQA Date Picker.

### Website
https://demoqa.com/date-picker

### Work Completed
- Created `DemoQADatePage` using the Page Object Model.
- Added a locator for the date input field.
- Added a method to enter the appointment date.
- Created `test_demoqa_date.py`.
- Verified that the entered date is displayed correctly.

### Test Result
DemoQA Date Picker test passed successfully.