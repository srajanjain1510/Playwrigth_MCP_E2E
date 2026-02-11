from playwright.sync_api import sync_playwright
from sohohousehomepagelocators import WELLNESS_MENU_LINK, WELLNESS_SUBMENU_LINKS

def test_fetch_wellness_submenu_links():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.sohohouse.com/")
        # Click on the 'Wellness' top menu link
        page.click(WELLNESS_MENU_LINK)

        # Wait for submenu to appear (adjust selector as needed)
        page.wait_for_selector(WELLNESS_SUBMENU_LINKS)

        # Fetch all submenu link names under 'Wellness'
        submenu_links = page.query_selector_all(WELLNESS_SUBMENU_LINKS)
        submenu_names = [link.inner_text() for link in submenu_links]

        print("Submenu links under 'Wellness':")
        for name in submenu_names:
            print(name)

        browser.close()
