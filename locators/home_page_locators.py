# locators/home_page_locators.py

class HomePageLocators:
    SEARCH_BOX = "input[name='q']"
    SEARCH_BUTTON = "button[type='submit']"
    WELLNESS_MENU = "a[data-testid='top-menu-link'][href*='wellness']"
    WELLNESS_SUBMENUS = "nav[aria-label='Wellness'] ul li a, nav[aria-label='Wellness'] ul li button"