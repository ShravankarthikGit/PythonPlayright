from playwright.sync_api import Page, expect
from ai.home_page import HomePage
from ai.login_page import LoginPage
import os
from datetime import datetime


def test_login_logout(page: Page):
    """
    Test login and logout flow on demoblaze using POM.
    Steps:
    1. Open homepage
    2. Click 'Log in'
    3. Enter username and password and submit
    4. Verify 'Log out' link visible and welcome text shown
    5. Click 'Log out'
    6. Verify 'Log in' link visible again
    """

    username = "pavanol"
    password = "test@123"

    home = HomePage(page)
    login = LoginPage(page)

    # helper for screenshots on failure
    def _screenshot(name: str):
        out_dir = os.path.join(os.getcwd(), "test-artifacts")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, f"{datetime.utcnow().strftime('%Y%m%dT%H%M%S')}_{name}.png")
        try:
            page.screenshot(path=path, full_page=True)
            print(f"Saved screenshot: {path}")
        except Exception as e:
            print(f"Failed to take screenshot: {e}")

    try:
        # 1. Open site
        home.open()

        # 2. Click Log in link
        home.click_login()

        # 3. Enter credentials and login
        login.login(username, password)

        # 4. Verify that Log out is visible
        expect(home.logout_link).to_be_visible(timeout=5000)

        # Verify welcome text contains username
        expect(home.welcome_text).to_contain_text(username, timeout=5000)

        # 5. Click Log out
        home.click_logout()

        # 6. Verify Log in is visible again
        expect(home.login_link).to_be_visible(timeout=5000)

        print("✓ Login-logout flow validated successfully")
    except Exception as exc:
        _screenshot("failure")
        # print a short page content fragment to help debugging
        try:
            print(page.content()[:2000])
        except Exception:
            pass
        raise


