from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

#from page_objects.graveyards_page import GraveyardsPage


class CreateGraveyard:
    GRAVEYARD_NAME = (By.NAME, "name")
    GRAVEYARD_IMAGE = (By.NAME, "image")
    GRAVEYARD_DESC = (By.NAME, "description")
    SUBMIT_BUTTON = (By.CLASS_NAME, "btn")
    URL = "https://yelpgraveyard.herokuapp.com/graveyards/new"

    def __init__(self, driver):
        self.driver = driver

    def create_graveyard(self, name, image, desc):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.GRAVEYARD_NAME)).send_keys(name)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.GRAVEYARD_IMAGE)).send_keys(image)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.GRAVEYARD_DESC)).send_keys(desc)
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(self.SUBMIT_BUTTON)).click()