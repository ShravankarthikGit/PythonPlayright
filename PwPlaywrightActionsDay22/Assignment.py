# 1. Check visibility and enabled state - Name & Password, then fill the text
# 2. Count number of favorite drinks and select all the favorite drinks and assert each check box is selected
# 3. Check favorite color "Green" radio button by choice
# 4 . Print all the automation tools
from faulthandler import is_enabled

import pytest
from playwright.sync_api import Page, expect

def test_actions(page:Page):
    page.goto("https://practice-automation.com/form-fields/")
    page.wait_for_timeout(5000)
    name_locator = page.locator("#name-input")
    password_locator = page.get_by_label("Password")

    if name_locator.is_enabled() & name_locator.is_visible():
        name_locator.fill("Pillo Killow")
    if password_locator.is_enabled() & name_locator.is_visible():
        password_locator.fill("Password")

    # 2. Count number of favorite drinks and select all the favorite drinks and assert each check box is selected
    favorites = page.locator('[id^="drink"]')
    print(f" total count of favorite drinks: {favorites.count()}")
    for i in favorites.all():
        i.check()
        expect(i).to_be_checked()

    # 3. Check favorite color "Green" radio button by choice
    greenlabel = page.get_by_label("Green", exact=True)
    if greenlabel.is_enabled() & greenlabel.is_visible():
        greenlabel.check()
    page.wait_for_timeout(5000)

    # 4 . Print all the automation tools
    tools = page.locator("form[id='feedbackForm'] ul li")
    for tool in tools.all():
        print(tool.text_content())