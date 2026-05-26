# Pre-requisite for Asynchrouns execution
# install  pytest-asyncio
# command:   pip install pytest-asyncio

from playwright.async_api import async_playwright, expect as async_expect
from playwright.sync_api import sync_playwright, expect as sync_expect
import pytest

@pytest.mark.asyncio
async def test_verifyPageUrl_async():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  #  headed mode
        mypage = await browser.new_page()
        await mypage.goto("https://demowebshop.tricentis.com/")
        myurl = mypage.url
        await async_expect(mypage).to_have_url(myurl)
        await browser.close()


def test_verifyPageUrl_sync():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headed mode
        mypage = browser.new_page()
        mypage.goto("https://demowebshop.tricentis.com/")  # passing url
        myurl=mypage.url
        print("Url of the application:", myurl)
        sync_expect(mypage).to_have_url(myurl)
        browser.close()
