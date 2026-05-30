import re

import pytest
from playwright.sync_api import Page, expect


def test_assignment_flight_booking(page:Page):
    page.goto("https://blazedemo.com/")

    departure_city = page.locator("select[name='fromPort']")
    destination_city = page.locator("select[name='toPort']")
    departure_city.select_option(value = "Boston")
    destination_city.select_option(value = "London")

    page.get_by_role("button").click()
    rows = page.locator("table.table tbody tr")

    flight_count = rows.count()
    print(f"Flight count: {flight_count}")
    flight_price = []
    for row in rows.all():
        # I am looking for values that start with dollar in the column
        price = row.locator("td").filter(has_text=re.compile(r"^\$")).inner_text().strip()
        flight_price.append(price)
        print(f"Flight price: {flight_price}")
        flight_price.sort()

    print("Lowest flight price:", flight_price[0])
    for row in rows.all():
        price = row.locator("td").filter(has_text=re.compile(r"^\$")).inner_text().strip()
        if (price == flight_price[0]):
            row.locator("td").filter(has_text="Choose This Flight").click()
            break

    page.get_by_placeholder("First Last").fill("John")
    page.get_by_role("textbox", name="Address").fill("1403 American Beauty Ln")
    page.get_by_role("textbox", name="City").fill("Columbus")
    page.get_by_role("textbox", name="State").fill("OH")
    page.get_by_role("textbox", name="Zip Code").fill("43240")
    page.locator("#cardType").select_option(value = "American Express")
    page.get_by_label("Credit Card Number").fill("6789067345231267")
    page.locator("#creditCardYear").fill("2024")
    page.locator("#nameOnCard").fill("John Canedy")
    page.get_by_role("button").click()

    expect(page.get_by_role("heading")).to_contain_text("Thank you for your purchase today!")

    print("All tests passed!")





    page.wait_for_timeout(5000)







