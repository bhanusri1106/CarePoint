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