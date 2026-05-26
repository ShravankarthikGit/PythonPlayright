import time
import re
import pytest
from playwright.sync_api import Page, expect

# 1) page.get_by_alt_text()
# 2) page.get_by_text()
# 3) page.get_by_role()
# 4) page.get_by_label()
# 5) page.get_by_placeholder()
# 6) page.get_by_title()
# 7) page.get_by_test_id()

def test_verify_pwlocators(page:Page):
    apprl = "http://localhost:8080/"

    page.goto(apprl)
    #time.sleep(5) # seconds
    page.wait_for_timeout(5000) # 500 ms = 5 secs

    # 1) page.get_by_alt_text()
    # logo=page.get_by_alt_text("nopCommerce demo store")
    logo = page.get_by_alt_text("Your store name")
    expect(logo).to_be_visible()

    #  2) page.get_by_text()
    expect(page.get_by_text("Welcome to our store")).to_be_visible() # full text
    expect(page.get_by_text("Welcome to")).to_be_visible()  # partial text
    expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible()  # reg expression

    # h2 tag stands for heading
    expect(page.get_by_role("heading", name="Welcome to our store")).to_be_visible()


    # # 3) page.get_by_role()
    page.goto(f"{apprl}register?returnUrl=%2F")
    page.wait_for_timeout(5000)  # 500 ms = 5 secs
    expect(page.get_by_role("heading",name="Register")).to_be_visible()

    # # 4) page.get_by_label() for text box
    page.get_by_label("First name:").fill("John")
    page.get_by_label("Last name:").fill("Kenedy")
    page.get_by_label("Email:").fill("abc@gmail.com")
    page.wait_for_timeout(5000)

    # # 5) page.get_by_placeholder()
    page.get_by_placeholder("Search store").fill("Apple MacBook Pro")
    page.wait_for_timeout(5000)

    # # 6) page.get_by_title()
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page.get_by_title("Home page link")).to_have_text("Home")
    expect(page.get_by_title("HyperText Markup Language")).to_have_text("HTML")
    page.wait_for_timeout(5000)

    # # 7) page.get_by_test_id()
    expect(page.get_by_test_id("profile-name")).to_have_text("John Doe")
    expect(page.get_by_test_id("profile-email")).to_have_text("john.doe@example.com")