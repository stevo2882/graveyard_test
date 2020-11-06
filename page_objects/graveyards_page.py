from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from page_objects.create_graveyard_page import CreateGraveyard
from page_objects.graveyard_page import GraveyardPage
from page_objects.landing_page import LandingPage


class GraveyardsPage:
    WELCOME_TEXT = (By.CSS_SELECTOR, ".jumbotron h1")
    BRAND_LINK = (By.CSS_SELECTOR, ".navbar-brand")
    LOGIN_BUTTON = (By.LINK_TEXT, "Login")
    ADD_GRAVEYARD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.btn-large")
    DELETE_BUTTON = (By.CSS_SELECTOR, "#delete-form > button")
    DELETE_SUCCESS = (By.CSS_SELECTOR, ".alert.alert-success")
    URL = 'https://yelpgraveyard.herokuapp.com/graveyards'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def is_loaded(self):
        elem = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.ADD_GRAVEYARD_BUTTON))
        if elem.is_displayed:
            return True

    def click_brand_link(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.BRAND_LINK)).click()
        return LandingPage(self.driver)

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.LOGIN_BUTTON)).click()

    def click_add_new_graveyard_button(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.ADD_GRAVEYARD_BUTTON))
        elem = self.driver.find_element(*self.ADD_GRAVEYARD_BUTTON)
        ActionChains(self.driver).move_to_element(elem).click().perform()
        return CreateGraveyard(self.driver)

    def view_graveyard(self, name):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, name)))
        elem = self.driver.find_element_by_link_text(name)
        ActionChains(self.driver).move_to_element(elem).click().perform()
        #WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.DELETE_BUTTON))
        return GraveyardPage(self.driver)

    def delete_sucess(self):
        elem = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.DELETE_SUCCESS))
        if elem is not None:
            return True

