import pytest
from playwright.sync_api import sync_playwright, expect, Page


def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # 3 ways to select option from the dropdown
    #page.locator("#country").select_option("India")  # by label
    page.locator("#country").select_option(label="India")  # by label

    selected_value = page.locator("#country").input_value() # capture selected option
    print("Selected Value:", selected_value)
    assert selected_value == "india" # using pytest assert to validate the value selected.
    page.pause()
    page.locator("#country").select_option("germany") # this is not a good practice
    page.locator("#country").select_option(value="germany")  # by value
    page.wait_for_timeout(5000)

    page.locator("#country").select_option(index=2)   # by index  # index starts from 0
    # check number of options in dropdown
    dropdown_options=page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)

    options_text=[text.strip() for text in dropdown_options.all_text_contents()]
    print(options_text)

    # print countries using loop
    for option in options_text:
        print(option)


    page.wait_for_timeout(5000)

