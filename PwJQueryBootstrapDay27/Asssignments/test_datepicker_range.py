import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_date_range_picker(page: Page):
    # Navigate to the site
    page.goto("https://testautomationpractice.blogspot.com/")

    # Fill in the start and end date using YYYY-MM-DD format (required for <input type="date">)
    page.locator("#start-date").fill("2025-10-20")
    page.locator("#end-date").fill("2026-09-05")

    page.wait_for_timeout(10000)