# tests/test_soho_house_shop_menu.py

from playwright.sync_api import sync_playwright
import time
from locators.home_page_locators import SHOP_BUTTON, SOHO_HOME_LINK, COWSHED_LINK, SOHO_SKIN_LINK

def test_soho_house_shop_menu():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.sohohouse.com/")
        print("Successfully navigated to Soho House website")

        # Step 3: Click on the top menu navigation link - 'Shop'
        shop_button = page.get_by_role(SHOP_BUTTON["role"], name=SHOP_BUTTON["name"])
        shop_button.click()
        print("Clicked on Shop menu link")

        network_requests = []

        def handle_request(request):
            if request.response:
                network_requests.append({
                    "url": request.url,
                    "method": request.method,
                    "status": request.response.status
                })

        page.on("requestfinished", handle_request)
        time.sleep(2)

        has_400_errors = False
        for request in network_requests:
            if 400 <= request.get("status", 0) < 500:
                has_400_errors = True
                print(f"Error: Found 400 status code in request to {request['url']}")

        if not has_400_errors:
            print("Validation passed: No 400 errors found after clicking on Shop menu")

        # Step 5: Click on all sub menu links one by one
        soho_home_link = page.get_by_role(SOHO_HOME_LINK["role"], name=SOHO_HOME_LINK["name"])
        soho_home_link.click()
        print("Clicked on Soho Home sub-menu link")
        page.goto("https://www.sohohouse.com/")
        shop_button = page.get_by_role(SHOP_BUTTON["role"], name=SHOP_BUTTON["name"])
        shop_button.click()
        cowshed_link = page.get_by_role(COWSHED_LINK["role"], name=COWSHED_LINK["name"])
        cowshed_link.click()
        print("Clicked on Cowshed sub-menu link")
        page.goto("https://www.sohohouse.com/")
        shop_button = page.get_by_role(SHOP_BUTTON["role"], name=SHOP_BUTTON["name"])
        shop_button.click()
        soho_skin_link = page.get_by_role(SOHO_SKIN_LINK["role"], name=SOHO_SKIN_LINK["name"])
        soho_skin_link.click()
        print("Clicked on Soho Skin sub-menu link")

        browser.close()
        print("Browser closed successfully")
        print("Test completed successfully!")

if __name__ == "__main__":
    test_soho_house_shop_menu()
