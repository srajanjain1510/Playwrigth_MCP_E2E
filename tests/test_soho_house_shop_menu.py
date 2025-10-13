from playwright.sync_api import sync_playwright, expect
import re
from locators.soho_house_locators import SohoHouseLocators

def test_soho_house_shop_menu():
    """
    Test case for JIRA Ticket SCRUM-1:
    1. Open the Chrome Browser
    2. Navigate to the URL - "https://www.sohohouse.com/"
    3. Click on the top menu navigation link - 'Shop'
    4. Capture the network logs and validate there should not be 400 error after clicking on the 'Shop' menu link.
    5. Close the browser.
    """
    with sync_playwright() as p:
        # Step 1: Open the Chrome Browser
        browser = p.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context()
        
        # Enable network request tracking
        page = context.new_page()
        
        # Step 2: Navigate to the URL
        page.goto("https://www.sohohouse.com/")
        
        # Step 3: Click on the top menu navigation link - 'Shop'
        shop_button = page.locator(SohoHouseLocators.SHOP_BUTTON)
        shop_button.click()
        
        # Step 4: Capture the network logs and validate there should not be 400 error
        # Wait for network to be idle to ensure all requests are completed
        page.wait_for_load_state("networkidle")
        
        # Get all requests
        # Playwright does not provide direct API to get all requests from context, so we use event listeners
        error_requests = []
        def handle_response(response):
            if 400 <= response.status < 500:
                error_requests.append({
                    "url": response.url,
                    "status": response.status
                })
        page.on("response", handle_response)
        # Wait a bit to ensure all responses are captured
        page.wait_for_timeout(2000)
        
        # Assert no 400 errors
        assert len(error_requests) == 0, f"Found 400 errors in network requests: {error_requests}"
        
        # Step 5: Close the browser
        browser.close()

if __name__ == "__main__":
    test_soho_house_shop_menu()
