from selenium.webdriver.common.by import By
from browser import Browser

class DashboardPageLocator(object):
    # Home Page Locators
    
    HEADER_TEXT = (By.XPATH, "//h1")
    DOCUMENTS_LINK = (By.ID, "browseCategoryLink1")
    WELCOME_DROP_DOWN_BUTTON = (By.ID, "welcome-drop-down")
    LOGOUT_LINK_BUTTON = (By.ID, "logoutLink")


class DashboardPage(Browser):
    # Home Page Actions
    
    def get_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def find_header(self):
        return self.get_element(*DashboardPageLocator.HEADER_TEXT).text
    
    def click_element(self, *locator):
        return self.driver.find_element(*locator).click()
    
    def navigate_to_category(self):
        return self.click_element(*DashboardPageLocator.DOCUMENTS_LINK)
    
    def logout(self):
        self.click_element(*DashboardPageLocator.WELCOME_DROP_DOWN_BUTTON)
        self.click_element(*DashboardPageLocator.LOGOUT_LINK_BUTTON)
    
    def find_welcome_buttom(self):
        return self.get_element(*DashboardPageLocator.WELCOME_DROP_DOWN_BUTTON)

