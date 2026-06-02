from playwright.sync_api import Playwright, Page, expect


def test_tabs(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    parent_page = context.new_page()

    # Navigate to the target page
    parent_page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # click on link OrangeHRM, Inc
    parent_page.on("page", lambda page: page.wait_for_load_state())
    parent_page.get_by_text("OrangeHRM, Inc", exact=True).click()
    parent_page.wait_for_timeout(5000)

    all_tabs = context.pages

    parent_page = all_tabs[0]
    print("Page 1 URL is:", parent_page.url)

    child_page = all_tabs[1]
    print("Page 1 URL is:", child_page.url)

    eng_locator = parent_page.get_by_placeholder("Username")
    spa_locator = parent_page.get_by_placeholder("Nombre de usuario")
    final_locator = eng_locator or spa_locator
    final_locator.fill("Admin")

    parent_page.get_by_placeholder("Password").fill("admin123")
    parent_page.on("dialog", lambda dialog: dialog.dismiss())
    parent_page.get_by_role("button").click()

    child_page.locator(".nav-item.nav-item-btn.btn-contact.web-menu").click()
    expect(child_page.locator("h3:has-text('Talk To An Expert')")).to_contain_text("Expert")

    parent_page.wait_for_timeout(5000)

    context.close()
    browser.close()


