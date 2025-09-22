# test_home_page.py

from playwright.sync_api import sync_playwright
from home_page_locators import HOUSES_NAV_LINK

def test_houses_navigation_no_400_error():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Step 1: Navigate to Soho House home page
        page.goto("https://www.sohohouse.com/")

        # Step 2: Click on 'Houses' navigation link
        page.click(HOUSES_NAV_LINK)

        # Step 3: Verify no network request returns a 400 error after clicking
        # Wait for navigation to complete
        page.wait_for_load_state("networkidle")

        # Get all network requests
        requests = page.context.request.finished

        # Check for 400 errors
        for req in page.context.request.finished:
            if req.response.status == 400:
                print(f"400 error found for URL: {req.url}")
                assert False, f"400 error found for URL: {req.url}"

        # Alternatively, use Playwright's network events
        # for request in page.context.request.finished:
        #     if request.response.status == 400:
        #         assert False, f"400 error found for {request.url}"

        browser.close()

if __name__ == "__main__":
    test_houses_navigation_no_400_error()
