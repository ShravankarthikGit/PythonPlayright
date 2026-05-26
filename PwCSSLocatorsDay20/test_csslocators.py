'''
tag id          tag#id
tag class       tag.class
tag attribute   tag[attribute=value]
tag class attribute     tag.class[attribute=value]

Note: tag name is optional
'''


import pytest
from playwright.sync_api import Page, expect

def test_verify_css_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    # #tag id
    # page.locator("input#small-searchterms").fill("T-Shirts")
    # #  without tag name
    # page.locator("#small-searchterms").fill("T-Shirts")
    # page.wait_for_timeout(5000)
    # page.locator("#small-searchterms").clear()
    #
    # #tag class
    # page.locator("input.search-box-text.ui-autocomplete-input").fill("T-Shirts")
    # #  without tag name
    # page.locator(".search-box-text").fill("T-Shirts")
    # page.wait_for_timeout(5000)
    #
    # #tag attribute
    # page.locator("input[name=q]").fill("T-Shirts")
    # # without tag name
    # page.locator("[name=q]").fill("T-Shirts")
    # page.wait_for_timeout(5000)

    # tag class attribute
    page.locator("input.search-box-text[value='Search store']").fill("T-Shirts")
    #  without tag name
    page.locator(".search-box-text[value='Search store']").fill("T-Shirts")
    page.wait_for_timeout(5000)


