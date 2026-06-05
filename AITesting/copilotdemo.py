from playwright.sync_api import Page

def test_login(page: Page):
    page.goto("https://playwright.org/")

    # Click on the "Get Started" button
    page.wait_for_selector("#login-form")