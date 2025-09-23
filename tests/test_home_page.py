# tests/test_home_page.py

import pytest
from playwright.sync_api import sync_playwright
from locators.home_page_locators import get_wellness_menu_locator, get_wellness_submenu_locator

def test_wellness_menu_submenu():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.sohohouse.com/en-us/")
        page.wait_for_load_state('networkidle')

        # Click on the "Wellness" top menu link
        wellness_menu = get_wellness_menu_locator(page)
        wellness_menu.click()

        # Capture the submenu of the Wellness menu
        submenu = get_wellness_submenu_locator(page)
        assert submenu.is_visible(), "Wellness submenu should be visible after clicking Wellness menu."
        print("Submenu text:", submenu.inner_text())

        browser.close()
