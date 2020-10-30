from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from page_objects.graveyards_page import GraveyardsPage
from page_objects.landing_page import LandingPage


class LoginPage:
    URL = 'https://yelpgraveyard.herokuapp.com/login'
    LOGIN_FORM = (By.CSS_SELECTOR, ".form-group")
    USER_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "btn")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def close(self):
        self.driver.quit()

    def is_loaded(self):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.LOGIN_FORM))

    def login_user(self, user, password):
        self.is_loaded()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.USER_FIELD)).send_keys(user)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(password)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.LOGIN_BUTTON)).click()
        return GraveyardsPage(self.driver)
