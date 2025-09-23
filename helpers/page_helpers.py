# helpers/page_helpers.py
from playwright.sync_api import Page

def search_for(page: Page, query: str):
    page.fill("#search-box", query)
    page.click("#search-btn")
