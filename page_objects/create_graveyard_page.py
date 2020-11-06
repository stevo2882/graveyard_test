from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class CreateGraveyard:
    GRAVEYARD_NAME = (By.NAME, "name")
    GRAVEYARD_IMAGE = (By.NAME, "image")
    GRAVEYARD_DESC = (By.NAME, "description")
    SUBMIT_BUTTON = (By.CLASS_NAME, "btn")
    URL = "https://yelpgraveyard.herokuapp.com/graveyards/new"

    def __init__(self, driver):
        self.driver = driver
        self.is_loaded()

    def is_loaded(self):
        """"""
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.SUBMIT_BUTTON))

    def create_graveyard(self, name, image, desc):
        self.set_graveyard_name(name)
        self.set_graveyard_image(image)
        self.set_graveyard_desc(desc)
        self.set_graveyard_name(name)

    def set_graveyard_name(self, name):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(self.GRAVEYARD_NAME))
        elem = self.driver.find_element(*self.GRAVEYARD_NAME)
        ActionChains(self.driver).move_to_element(elem).click().send_keys(name).perform()

    def set_graveyard_image(self, image):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.GRAVEYARD_IMAGE))
        elem = self.driver.find_element(*self.GRAVEYARD_IMAGE)
        ActionChains(self.driver).move_to_element(elem).click().send_keys(image).perform()

    def set_graveyard_desc(self, desc):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.GRAVEYARD_DESC))
        elem = self.driver.find_element(*self.GRAVEYARD_DESC)
        ActionChains(self.driver).move_to_element(elem).click().send_keys(desc).perform()

    def click_submit(self):
        elem = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.SUBMIT_BUTTON))
        elem.click()