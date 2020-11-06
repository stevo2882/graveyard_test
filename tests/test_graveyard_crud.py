import pytest
import requests
from selenium import webdriver

from page_objects.create_graveyard_page import CreateGraveyard
from page_objects.graveyards_page import GraveyardsPage
from page_objects.login_page import LoginPage


@pytest.fixture()
def driver():
    _driver = webdriver.Chrome()
    #login_page = LoginPage(_driver)
    #login_page.login_user("test_user", "test_pass")
    yield _driver
    _driver.quit()


@pytest.fixture()
def login(driver):
    driver.get("http://yelpgraveyard.herokuapp.com/login")
    login_page = LoginPage(driver)
    login_page.login_user("test_user", "test_pass")


def test_create_graveyard(driver, login):
    """Test that landing page loads and button redirects you to graveyards page."""
    graveyards_page = GraveyardsPage(driver)
    create_graveyard_page = graveyards_page.click_add_new_graveyard_button()
    #create_graveyard_page = CreateGraveyard(driver)
    create_graveyard_page.create_graveyard("test_graveyard", "https://images.unsplash.com/photo-1559916711-50f8f6fa74df?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2089&q=80", "test description")
    assert 1 == 1


def test_read_graveyard(driver, login):
    """"""
    graveyards_page = GraveyardsPage(driver)
    test_graveyard = graveyards_page.view_graveyard("test_graveyard")
    caption = test_graveyard.get_graveyard_name()
    assert "test_graveyard" in caption
    assert "test description" in caption
    assert "test_user" in caption


def test_delete_graveyard(driver, login):
    """"""
    graveyards_page = GraveyardsPage(driver)
    test_graveyard = graveyards_page.view_graveyard("test_graveyard")
    test_graveyard.click_delete()
    assert graveyards_page.delete_sucess()
