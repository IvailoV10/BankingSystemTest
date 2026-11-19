from selenium import webdriver
import pytest
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://parabank.parasoft.com/parabank/index.html')

    yield driver

    driver.quit()
