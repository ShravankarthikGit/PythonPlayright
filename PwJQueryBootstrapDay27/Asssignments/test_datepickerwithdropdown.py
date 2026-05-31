import pytest
from playwright.sync_api import Page, expect


def test_date_picker_with_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    year = "2024"
    month = "7" # August
    day = "15"
    select_date(month,day,year,page)

    expect(page.locator("[name='SelectedDate']")).to_have_value("15/08/2024")
    page.wait_for_timeout(10000)


def select_date(month:str, day:str, year: str, page: Page):
    page.locator("[name='SelectedDate']").click()
    page.get_by_label("Select month").select_option(value=month)
    page.get_by_label("Select year").select_option(value=year)

    dates = page.locator(".ui-datepicker-calendar td a")
    for date in dates.all():
        current_day = date.inner_text().strip()
        if current_day == day:
            date.click()
            break

