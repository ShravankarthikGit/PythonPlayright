from playwright.sync_api import Page, expect
from .base_page import BasePage


class LoginPage(BasePage):
    # login modal selectors
    def __init__(self, page: Page):
        super().__init__(page)
        self.modal = self.page.locator("#logInModal")
        self.username_input = self.page.locator("#loginusername")
        self.password_input = self.page.locator("#loginpassword")
        # The modal's Log in button can be matched by text within modal footer
        self.submit_button = self.modal.locator(".modal-footer button:has-text('Log in')")

    def wait_for_modal(self, timeout: int = 5000):
        self.modal.wait_for(state="visible", timeout=timeout)

    def login(self, username: str, password: str):
        # Ensure modal is open
        self.wait_for_modal()
        self.username_input.fill(username)
        self.password_input.fill(password)
        # click the login button
        self.submit_button.click()
        # after clicking, wait a short while for UI update
        self.page.wait_for_timeout(1000)

