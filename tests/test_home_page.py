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
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_home_page_search(page):
    page.goto("https://example.com")
    page.fill(HomePageLocators.SEARCH_BOX, "Playwright")
    page.click(HomePageLocators.SEARCH_BUTTON)
    assert "search" in page.url

def test_wellness_menu_submenus(page):
    page.goto("https://www.sohohouse.com/en-us/")
    page.click(HomePageLocators.WELLNESS_MENU)
    page.wait_for_selector(HomePageLocators.WELLNESS_SUBMENUS, timeout=5000)
    submenu_elements = page.query_selector_all(HomePageLocators.WELLNESS_SUBMENUS)
    submenu_names = [el.inner_text().strip() for el in submenu_elements]
    print("Wellness Submenus:", submenu_names)
