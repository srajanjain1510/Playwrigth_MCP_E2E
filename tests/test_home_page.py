# tests/test_home_page.py
import pytest
from playwright.sync_api import sync_playwright
from locators.home_page_locators import HomePageLocators

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_search_box_visible(page):
    page.goto("https://example.com")
    assert page.is_visible(HomePageLocators.SEARCH_BOX)

def test_login_link(page):
    page.goto("https://example.com")
    assert page.is_visible(HomePageLocators.LOGIN_LINK)
    page.click(HomePageLocators.LOGIN_LINK)
    assert page.url == "https://example.com/login"
