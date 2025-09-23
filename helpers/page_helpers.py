# helpers/page_helpers.py
from playwright.sync_api import Page

def login(page: Page, username: str, password: str):
    page.fill('input#username', username)
    page.fill('input#password', password)
    page.click('button#login')
    page.wait_for_selector('img.profile-icon')