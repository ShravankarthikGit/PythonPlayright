from playwright.sync_api import Page, expect
from .base_page import BasePage


class HomePage(BasePage):
    URL = "https://www.demoblaze.com/index.html"

    def __init__(self, page: Page):
        super().__init__(page)
        # locators
        self.login_link = self.page.locator("#login2")
        self.logout_link = self.page.locator("#logout2")
        self.welcome_text = self.page.locator("#nameofuser")

    def open(self):
        self.goto(self.URL)
        # ensure page loaded
        self.page.wait_for_load_state("domcontentloaded")

    def click_login(self):
        self.login_link.wait_for(state="visible", timeout=5000)
        self.login_link.click()

    def is_logout_visible(self) -> bool:
        try:
            self.logout_link.wait_for(state="visible", timeout=3000)
            return True
        except Exception:
            return False

    def is_login_visible(self) -> bool:
        try:
            self.login_link.wait_for(state="visible", timeout=3000)
            return True
        except Exception:
            return False

    def get_welcome_text(self) -> str:
        try:
            self.welcome_text.wait_for(state="visible", timeout=3000)
            return self.welcome_text.inner_text()
        except Exception:
            return ""

    def click_logout(self):
        self.logout_link.wait_for(state="visible", timeout=5000)
        self.logout_link.click()

