from playwright.sync_api import Page, expect

def test_orangeapp(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(30000)
    expect(page.get_by_alt_text("company-branding")).to_be_visible()

    page.get_by_label("Username").fill("Admin")
    page.get_by_label("Password").fill("admin123")

    page.get_by_role("button", name="Login").click()

    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()




