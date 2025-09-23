# helpers/page_helpers.py

def login(page, username, password):
    page.goto("https://example.com/login")
    page.fill("#username", username)
    page.fill("#password", password)
    page.click("#submitLogin")
