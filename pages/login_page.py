
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    #locators are stored here
        self.USERNAME = (By.NAME, 'username')
        self.PASSWORD = (By.NAME, 'password')
        self.LOGIN = (By.XPATH, '/html/body/div[1]/div[3]/div[1]/div/form/div[3]/input')

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN).click()