import pytest
from playwright.sync_api import Page, expect



def test_irctc_date_picker(page: Page):
    page.goto("https://www.irctc.co.in/nget/train-search")
    page.locator("#jDate").click()

    month = "July"
    day = "15"
    year = "2026"

    while True:
        month_locator = page.locator(".ui-datepicker-month").inner_text()
        year_locator = page.locator(".ui-datepicker-year").inner_text()
        if month_locator == month and year_locator == year:
            break
        else:
            next_locator = page.locator(".ui-datepicker-next-icon")
            next_locator.click()

    day_locator = page.locator(".ui-datepicker-calendar td")
    for date in day_locator.all():
        if date.inner_text() == day:
            date.click()
            break

    page.wait_for_timeout(5000)