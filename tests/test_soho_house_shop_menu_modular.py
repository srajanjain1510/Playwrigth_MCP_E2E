from playwright.sync_api import sync_playwright, expect
from locators.soho_house_locators import SohoHouseLocators

def test_soho_house_shop_menu():
    """
    Test case for JIRA ticket SCRUM-1:
    1. Open Chrome browser
    2. Navigate to "https://www.sohohouse.com/"
    3. Click on the "Shop" menu link
    4. Validate there are no 400 errors in network logs
    5. Close the browser
    """
    with sync_playwright() as p:
        # 1. Launch Chrome browser
        browser = p.chromium.launch(channel="chrome", headless=False)
        
        # Create a context with network request tracking
        context = browser.new_context()
        page = context.new_page()
        
        # Store network requests to check for errors later
        requests = []
        
        # Listen for all network requests
        page.on("request", lambda request: requests.append(request))
        page.on("response", lambda response: requests.append(response))
        
        try:
            # 2. Navigate to the URL
            page.goto("https://www.sohohouse.com/")
            
            # 3. Click on the "Shop" menu link
            page.locator(SohoHouseLocators.SHOP_MENU_BUTTON).click()
            
            # 4. Validate there are no 400 errors in network logs
            error_responses = []
            for request in requests:
                if hasattr(request, "status") and 400 <= request.status < 500:
                    error_responses.append({
                        "url": request.url,
                        "status": request.status
                    })
            
            # Assert that there are no 400 errors
            assert len(error_responses) == 0, f"Found 400 errors: {error_responses}"
            
        finally:
            # 5. Close the browser
            browser.close()

if __name__ == "__main__":
    test_soho_house_shop_menu()
