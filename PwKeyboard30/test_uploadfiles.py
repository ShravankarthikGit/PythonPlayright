from playwright.sync_api import expect, Page
import pytest
from pathlib import Path

@pytest.mark.skip
def test_upload_singlefile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # get path for the file
    absolute_path = Path.cwd() / "test_upload_download"
    print(absolute_path)

    #uploading single file
    page.locator("#singleFileInput").set_input_files(absolute_path / "testfile1.pdf")
    page.locator("button:has-text('Upload Single File')").click()

    #validation
    expect(page.locator("#singleFileStatus")).to_contain_text("testfile1.pdf")
    print("File upload successful......")
    page.wait_for_timeout(5000)

# @pytest.mark.skip
def test_upload_multiplefiles(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # get path for the file
    absolute_path = Path.cwd() / "test_upload_download"
    print(absolute_path)

    #uploading multiple files
    files=[ absolute_path / "testfile1.pdf", absolute_path / "testfile2.pdf"]
    page.locator("#multipleFilesInput").set_input_files(files)
    page.locator("button:has-text('Upload Multiple Files')").click()

    #validation
    msg_loc=page.locator("#multipleFilesStatus")

    expect(msg_loc).to_contain_text("testfile1.pdf")
    expect(msg_loc).to_contain_text("testfile2.pdf")

    page.wait_for_timeout(5000)

    print("Multiple files are uploaded successfully.......")