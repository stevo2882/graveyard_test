import pytest

from selenium import webdriver
from page_objects.landing_page import LandingPage


def test_landing_page():
    """Test that landing page loads and button redirects you to graveyards page."""
    driver = webdriver.Chrome()
    landing_page = LandingPage(driver)
    landing_page.load()
    graveyards_page = landing_page.click_view_all_graveyards()
    assert graveyards_page.is_loaded() is True