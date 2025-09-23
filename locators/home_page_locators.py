# locators/home_page_locators.py

from playwright.sync_api import Page, Locator

class HomePageLocators:
    WELLNESS_MENU = "a[data-testid='nav-link-wellness']"
    WELLNESS_SUBMENUS = "[data-testid='nav-link-wellness'] + div ul li a"  # Adjust if actual DOM differs
