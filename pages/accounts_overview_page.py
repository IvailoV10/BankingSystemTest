from selenium.webdriver.common.by import By

class AccountsOverviewPage:
    def __init__(self, driver):
        self.driver = driver

        self.TOTAL_BALANCE = (By.CSS_SELECTOR, "#accountTable > tbody:nth-child(2) > tr:nth-child(12) > td:nth-child(2) > b:nth-child(1)")

    def get_total_balance(self):
        user_balance = self.driver.find_element(*self.TOTAL_BALANCE)
        return user_balance.text