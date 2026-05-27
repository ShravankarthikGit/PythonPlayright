import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_dropdown(page:Page):
    page.goto("https://www.bstackdemo.com/")
    page.wait_for_timeout(5000)

    orderby_dropdown = page.locator("div[class='sort'] select")
    expect(orderby_dropdown).to_be_visible()
    expect(orderby_dropdown).to_be_enabled()

    orderby_dropdown.select_option(value="lowestprice")
    page.wait_for_timeout(5000)

    mydict = {}
    for i in range(1,26):
        price = page.locator(f"div[class='shelf-item'][id = '{i}'] div[class='val'] b").text_content()
        product_name = page.locator(f"div[class='shelf-item'][id = '{i}'] p[class='shelf-item__title']").text_content()
        mydict.update({product_name.strip():price.strip()})

    print(mydict)
    # ascending order. Note: key=lambda is used to ignore key
    sorted_dict = dict(sorted(mydict.items(), key=lambda item: int(item[1])))
    print(sorted_dict)

    # In order to get first and last values we need to convert to list and then fetch values
    sorted_list = list(sorted_dict.items())
    lowest_priced_product, lowest_price = sorted_list[0]
    highest_priced_product, highest_price = sorted_list[-1]
    print(f"Lowest priced product is {lowest_priced_product} with price as {lowest_price}")
    print(f"Highest priced product is {highest_priced_product} with price as {highest_price}")
    page.wait_for_timeout(5000)

