# locators/home_page_locators.py

from playwright.sync_api import Page, Locator

def get_wellness_menu_locator(page: Page) -> Locator:
    return page.locator('a:has-text("Wellness")')

def get_wellness_submenu_locator(page: Page) -> Locator:
    # Adjust selector as needed based on actual submenu DOM
    return page.locator('nav[aria-label="Wellness submenu"]')
