# locators/home_page_locators.py

WELLNESS_MENU = "//nav//a[contains(text(), 'Wellness')]"
WELLNESS_SUBMENUS = "//nav//a[contains(text(), 'Wellness')]/following-sibling::div//a | //nav//a[contains(text(), 'Wellness')]/parent::li//ul//a"

WELLNESS_MENU = "a[data-testid='top-menu-link'][href*='wellness']"
WELLNESS_SUBMENUS = "nav[aria-label='Wellness'] ul li a, nav[aria-label='Wellness'] ul li button"