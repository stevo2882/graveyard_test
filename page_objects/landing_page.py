from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#from page_objects.graveyards_page import GraveyardsPage


class LandingPage:
    VIEW_GRAVEYARDS = (By.LINK_TEXT, "View All Graveyards")
    URL = 'https://yelpgraveyard.herokuapp.com/'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def is_loaded(self):
        try:
            return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.VIEW_GRAVEYARDS)).is_displayed()
        except NoSuchElementException:
            return False

    def click_view_all_graveyards(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.VIEW_GRAVEYARDS)).click()
        return GraveyardsPage(self.driver)

    def back(self):
        self.driver.back()
