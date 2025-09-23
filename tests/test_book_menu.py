# tests/test_book_menu.py

import pytest
from playwright.sync_api import sync_playwright
from locators.home_page_locators import BOOK_MENU_LINK, BOOK_SUBMENU_ITEMS

URL = "https://www.sohohouse.com/en-us/"

def test_book_menu_submenus():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(URL)
        page.click(BOOK_MENU_LINK)
        submenu_elements = page.query_selector_all(BOOK_SUBMENU_ITEMS)
        submenu_names = [el.inner_text().strip() for el in submenu_elements]
        print("Book submenu names:", submenu_names)
        browser.close()
