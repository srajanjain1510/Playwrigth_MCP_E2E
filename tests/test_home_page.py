from playwright.sync_api import sync_playwright
from home_page_locators import SUBMIT_BUTTON, USERNAME_INPUT, SUCCESS_MESSAGE

def test_home_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to the application
        page.goto("https://example.com")

        # Perform actions
        page.click(SUBMIT_BUTTON)
        page.fill(USERNAME_INPUT, "test_user")
        assert page.inner_text(SUCCESS_MESSAGE) == "Welcome!"

        # Close browser
        browser.close()
