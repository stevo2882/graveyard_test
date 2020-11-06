from selenium.common.exceptions import NoSuchElementException, WebDriverException, JavascriptException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from page_objects.custom_wait_conditions import webelement_to_be_clickable


class GraveyardPage:
    WELCOME_TEXT = (By.CSS_SELECTOR, ".jumbotron h1")
    BRAND_LINK = (By.CSS_SELECTOR, ".navbar-brand")
    GRAVEYARD_NAME = (By.CLASS_NAME, "caption-full")
    ADD_GRAVEYARD_BUTTON = (By.LINK_TEXT, "Add A New Graveyard")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".btn.btn-xs.btn-danger")
    URL = 'https://yelpgraveyard.herokuapp.com/graveyards'

    def __init__(self, driver):
        self.driver = driver
        self.is_loaded()

    def load(self):
        self.driver.get(self.URL)

    def is_loaded(self):
        """"""
        try:
            if self.driver.execute_script("return document.readyState") == "complete":
                return True
            else:
                return False
        except (WebDriverException, JavascriptException):
            return False

    def get_graveyard_name(self):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.GRAVEYARD_NAME)).text

    def click_delete(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.DELETE_BUTTON)).submit()


