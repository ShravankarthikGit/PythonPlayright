from playwright.sync_api import sync_playwright, expect, Page
import os
from pathlib import Path
from urllib.parse import urlparse

def test_download_file(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    # get path for the file
    absolute_path = Path.cwd() / "test_upload_download"
    print(absolute_path)

    # Approach 1: register an event using a separate function
    # def handle_download(download):
    #     download.save_as(absolute_path / "testfile.txt")
    # page.on("download",handle_download)
    #

    # Approach 2 using lambda expression
    page.on("download",lambda download: download.save_as(absolute_path / "testfile.txt"))

    page.locator("#inputText").fill("welcome")
    page.locator("#generateTxt").click()  # this will generate a link to download file
    page.locator("#txtDownloadLink").click() # this will download the file
    page.wait_for_timeout(5000)

    if os.path.exists("downloads/testfile.txt"):
        print("File exists")
    else:
        print("File not exist")

