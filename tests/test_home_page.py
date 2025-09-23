# tests/test_home_page.py

# tests/test_home_page.py

from playwright.sync_api import sync_playwright
from locators.home_page_locators import SHOP_MENU_LINK

def test_navigate_to_shop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.sohohouse.com/en-us/")
        page.click(SHOP_MENU_LINK)
        browser.close()

if __name__ == "__main__":
    test_navigate_to_shop()
