from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException, JavascriptException


class DeleteGraveyard:
    GRAVEYARD_NAME = (By.NAME, "name")
    GRAVEYARD_IMAGE = (By.NAME, "image")
    GRAVEYARD_DESC = (By.NAME, "description")
    SUBMIT_BUTTON = (By.CLASS_NAME, "btn")
    URL = "https://yelpgraveyard.herokuapp.com/graveyards/new"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.URL)
        self.is_loaded()

    def is_loaded(self):
        """"""
        try:
            if self.driver.execute_script("return document.readyState") == "complete":
                return True
            else:
                return False
        except (WebDriverException, JavascriptException):
            return False

    def create_graveyard(self, name, image, desc):
        elem = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.GRAVEYARD_NAME))
        elem.send_keys(name)
        elem = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.GRAVEYARD_IMAGE))
        elem.send_keys(image)
        elem = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.GRAVEYARD_DESC))
        elem.send_keys(desc)
        elem = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.SUBMIT_BUTTON))
        elem.click()