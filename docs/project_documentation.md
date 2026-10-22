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