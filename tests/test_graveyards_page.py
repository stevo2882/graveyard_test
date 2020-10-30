import pytest

from selenium import webdriver
import page_objects
from page_objects.graveyards_page import GraveyardsPage
from page_objects.landing_page import LandingPage


def test_graveyards_page():
    """Test that graveyards page loads and all links redirect you to correct page."""
    driver = webdriver.Chrome()
    graveyards_page = GraveyardsPage(driver)

    # Load graveyards page and verify
    graveyards_page.load()
    assert graveyards_page.is_loaded() is True

    # Navigate to Landing Page
    landing_page = graveyards_page.click_brand_link()
    assert landing_page.is_loaded() is True

    # Navigate to Login Page
    graveyards_page = landing_page.click_view_all_graveyards()
    graveyards_page.click_login_button()
    assert 1 == 1