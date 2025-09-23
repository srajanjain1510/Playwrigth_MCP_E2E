# tests/test_bedrooms_menu.py

from playwright.sync_api import sync_playwright
from locators.home_page_locators import BEDROOMS_MENU, BEDROOMS_SUBMENU_ITEMS

def test_bedrooms_submenus():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.sohohouse.com/en-us/")
        page.click(BEDROOMS_MENU)
        page.wait_for_selector(BEDROOMS_SUBMENU_ITEMS)
        submenu_elements = page.query_selector_all(BEDROOMS_SUBMENU_ITEMS)
        submenu_names = [el.inner_text() for el in submenu_elements]
        print("Submenus under 'Bedrooms':", submenu_names)
        browser.close()
