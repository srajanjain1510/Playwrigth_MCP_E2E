# helpers/browser_helper.py
from playwright.sync_api import sync_playwright

def launch_browser(headless=True):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=headless)
    return browser, p

def close_browser(browser, playwright):
    browser.close()
    playwright.stop()