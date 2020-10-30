from selenium import webdriver

from page_objects.login_page import LoginPage


def test_user_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login_user("test_user", "test_pass")
    login_page.close()
