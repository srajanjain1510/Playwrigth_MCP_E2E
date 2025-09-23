# tests/test_home_page.py

from playwright.sync_api import Page
from locators.home_page_locators import HomePageLocators

def test_search_box_visible(page: Page):
    page.goto("https://example.com")
    assert page.is_visible(HomePageLocators.SEARCH_BOX)

def test_login_link(page: Page):
    page.goto("https://example.com")
    assert page.is_visible(HomePageLocators.LOGIN_LINK)
