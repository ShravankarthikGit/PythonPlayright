import pytest
from playwright.sync_api import Page, expect

def test_flipkart(page:Page):
    page.goto("https://www.flipkart.com/")

    # As the locator comes up with 2 values i am using first to click on first find
    # page.get_by_placeholder("Search for Products, Brands and More").first.click()
    # page.locator("input:visible").click()

    close_button = page.get_by_role("button", name="✕")
    close_button.wait_for(state='visible', timeout=5000)
    if close_button.count() > 0:
        close_button.click()
    # Search for 'smart'
    page.locator("input:visible").fill("smart")
    # page.keyboard.press("Enter")

    # Wait for suggestions to appear
    page.wait_for_timeout(5000)

    items_displayed = page.locator("ul > li")
    count  = items_displayed.count()
    print("no of suggestions: ", count)

    expect(items_displayed).to_have_count(count)

    # print 5th value
    fifth_value = items_displayed.nth(4).text_content().strip()
    if fifth_value != 0:
        print(f"fifth value is: {fifth_value}")

    for i in items_displayed.all():
        print(i.text_content().strip())

    for i in items_displayed.all():
        option = i.text_content().strip()
        if option == "smart phones":
            i.click()


    page.wait_for_timeout(10000)


