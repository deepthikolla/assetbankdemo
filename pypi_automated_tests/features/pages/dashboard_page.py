from selenium.webdriver.common.by import By
from browser import Browser

class DashboardPageLocator(object):
    # Home Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")


class DashboardPage(Browser):
    # Home Page Actions

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_header(self):
        return self.get_element(*DashboardPageLocator.HEADER_TEXT).text
