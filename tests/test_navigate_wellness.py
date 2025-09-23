# tests/test_navigate_wellness.py

from playwright.sync_api import sync_playwright
from locators.home_page_locators import WELLNESS_MENU_LINK

def test_navigate_to_wellness():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.sohohouse.com/en-us/")
        page.click(WELLNESS_MENU_LINK)
        # Optionally, add an assertion here to verify navigation
        browser.close()
