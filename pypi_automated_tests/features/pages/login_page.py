from selenium.webdriver.common.by import By
from browser import Browser

class LoginPageLocator(object):
    # Login Page Locators
    
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGIN_ERROR_MESSAGE_FIELD = (By.XPATH, "//*[@id='loginPanel']/div[2]/div[2]")


class LoginPage(Browser):
    # Login Page Actions
    
    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)
    
    def click_element(self, *locator):
        self.driver.find_element(*locator).click()
    
    def navigate(self, address):
        self.driver.get(address)
    
    def get_page_title(self):
        return self.driver.title
    
    def get_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def login(self, username, password):
        self.fill(username, *LoginPageLocator.USERNAME_FIELD)
        self.fill(password, *LoginPageLocator.PASSWORD_FIELD)
        self.click_element(*LoginPageLocator.LOGIN_BUTTON)
    
    def enter_username(self, username):
        self.fill(username, *LoginPageLocator.USERNAME_FIELD)
    
    def enter_password(self, password):
        self.fill(password, *LoginPageLocator.PASSWORD_FIELD)
    
    def submit(self):
        self.click_element(*LoginPageLocator.LOGIN_BUTTON)
    
    def login_error_message(self):
        return self.get_element(*LoginPageLocator.LOGIN_ERROR_MESSAGE_FIELD)

