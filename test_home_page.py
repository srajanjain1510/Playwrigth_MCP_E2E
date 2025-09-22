# test_home_page.py

from playwright.sync_api import sync_playwright
from home_page_locators import ABOUT_NAV_LINK

def test_about_link_no_400_error():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Step 1: Navigate to the Soho House home page
        page.goto("https://www.sohohouse.com/")

        # Step 2: Click on the 'About' navigation link
        page.click(ABOUT_NAV_LINK)

        # Step 3: Verify there is no 400 error in the network requests
        # Wait for navigation to complete
        page.wait_for_load_state("networkidle")

        # Listen to all requests and check for 400s
        errors = []
        for req in page.context.requests:
            if req.response and req.response.status == 400:
                errors.append(req.url)
        assert not errors, f"400 error(s) found in network requests: {errors}"

        browser.close()
