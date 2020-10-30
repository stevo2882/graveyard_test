from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from page_objects.create_graveyard_page import CreateGraveyard
from page_objects.landing_page import LandingPage
#from page_objects.login_page import LoginPage


class GraveyardsPage:
    WELCOME_TEXT = (By.CSS_SELECTOR, ".jumbotron h1")
    BRAND_LINK = (By.CSS_SELECTOR, ".navbar-brand")
    LOGIN_BUTTON = (By.LINK_TEXT, "Login")
    ADD_GRAVEYARD_BUTTON = (By.LINK_TEXT, "Add A New Graveyard")
    URL = 'https://yelpgraveyard.herokuapp.com/graveyards'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def is_loaded(self):
        try:
            return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.WELCOME_TEXT)).is_displayed()
        except NoSuchElementException:
            return False

    def click_brand_link(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.BRAND_LINK)).click()
        return LandingPage(self.driver)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.LOGIN_BUTTON)).click()
        #return LoginPage(self.driver)

    def click_add_new_graveyard_button(self):
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.ADD_GRAVEYARD_BUTTON)).click()
        return CreateGraveyard(self.driver)

