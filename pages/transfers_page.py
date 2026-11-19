from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TransferPage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

        # Locators
        self.TRANSFER_FUNDS_LINK = (By.LINK_TEXT, "Transfer Funds")
        self.AMOUNT_INPUT = (By.ID, "amount")
        self.TRANSFER_BUTTON = (By.XPATH, "//input[@value='Transfer']")
        self.SUCCESS_MESSAGE = (By.XPATH, "//h1[text()='Transfer Complete!']")

        # Anchor check to ensure we are on the transfer page
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.TRANSFER_FUNDS_LINK)
        )

    def navigate_to_transfer(self):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.TRANSFER_FUNDS_LINK)
        ).click()

    def transfer_funds(self, amount):
        # Wait for the amount input field to be visible
        amount_field = WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.AMOUNT_INPUT)
        )
        amount_field.clear()
        amount_field.send_keys(amount)

        # Click the transfer button
        WebDriverWait(self.dotenv if hasattr(self, 'dotenv') else self.driver, self.timeout).until(
            EC.element_to_be_clickable(self.TRANSFER_BUTTON)
        ).click()

    def get_success_message(self):
        # Wait for the success header to appear after the transfer POST request completes
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text