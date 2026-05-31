
from playwright.sync_api import Page, expect

def test_draganddrop(page:Page):
    page.goto("https://demo.guru99.com/test/drag_drop.html")

    source_1 = page.locator("#credit2 a")
    target_1 = page.locator("#bank li")
    source_1.drag_to(target_1)
    expect(page.locator("ol[id='bank'] li")).to_contain_text("BANK")

    source_2 = page.locator("#fourth a").first
    target_2 = page.locator("#amt7 li")
    source_2.drag_to(target_2)

    source_3 = page.locator("#credit1 a")
    target_3 = page.locator("#loan li")
    source_3.drag_to(target_3)

    source_4 = page.locator("#fourth a").last
    target_4 = page.locator("#amt8 li")
    source_4.drag_to(target_4)


    page.wait_for_timeout(3000)

