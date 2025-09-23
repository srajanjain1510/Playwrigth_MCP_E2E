# tests/test_home_page.py

import pytest
from playwright.sync_api import sync_playwright
from locators.home_page_locators import HomePageLocators

BASE_URL = "https://www.sohohouse.com/en-us/"

@pytest.mark.e2e
def test_wellness_menu_submenus():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL)
        # Click on the "Wellness" top menu link
        page.click(HomePageLocators.WELLNESS_MENU)
        # Fetch the names of all the submenus under Wellness
        submenu_elements = page.query_selector_all(HomePageLocators.WELLNESS_SUBMENUS)
        submenu_names = [el.inner_text().strip() for el in submenu_elements]
        print("Submenu names under Wellness:", submenu_names)
        browser.close()
