# tests/test_home_page.py

from playwright.sync_api import sync_playwright
from locators.home_page_locators import WELLNESS_MENU, WELLNESS_SUBMENUS

def test_wellness_menu_submenus():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.sohohouse.com/en-us/")
        page.click(WELLNESS_MENU)
        page.wait_for_selector(WELLNESS_SUBMENUS, timeout=5000)
        submenu_elements = page.query_selector_all(WELLNESS_SUBMENUS)
        submenu_names = [el.inner_text().strip() for el in submenu_elements]
        print("Wellness Submenus:", submenu_names)
        browser.close()

if __name__ == "__main__":
    test_wellness_menu_submenus()
