import time
from playwright.sync_api import BrowserContext


def test_multiple_tabs(context: BrowserContext):
    # Open Tab 1 using the provided browser context
    page1 = context.new_page()
    page1.goto("https://testautomationpractice.blogspot.com/")

    # Open Tab 2 within the same browser context
    page2 = context.new_page()
    page2.goto("https://playwright.dev")

    # Bring Tab 1 back to the front
    page1.bring_to_front()

    # Optional: Add a brief sleep if you want to visually confirm the switch
    # before Pytest instantly closes the browser
    time.sleep(2)
