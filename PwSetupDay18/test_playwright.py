import pytest
from playwright.sync_api import Page, expect, sync_playwright


def test_verifyPageUrl(page:Page):
    page.goto("https://demowebshop.tricentis.com/")  # passing url
    myurl=page.url
    print("Url of the application:", myurl)
    expect(page).to_have_url(myurl) # expected url


def test_verifyTitle(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    mytitle=page.title()
    print("Title of the page:", mytitle)
    expect(page).to_have_title(mytitle)
