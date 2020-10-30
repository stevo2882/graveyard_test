import pytest

from selenium import webdriver

from page_objects.graveyards_page import GraveyardsPage
from page_objects.landing_page import LandingPage
from page_objects.login_page import LoginPage


def test_create_graveyard():
    """Test that landing page loads and button redirects you to graveyards page."""
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.load()
    graveyards_page = login_page.login_user("test_user", "test_pass")
    create_graveyard_page = graveyards_page.click_add_new_graveyard_button()
    create_graveyard_page.create_graveyard("test_graveyard", "https://images.unsplash.com/photo-1559916711-50f8f6fa74df?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2089&q=80", "test description")

    assert graveyards_page.is_loaded() is True
