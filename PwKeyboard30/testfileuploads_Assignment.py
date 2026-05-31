from playwright.sync_api import Playwright, sync_playwright, expect, Page
from pathlib import Path
import pytest

@pytest.mark.skip()
def test_single_file_upload(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    absolute_path = Path.cwd() / "test_upload_download"

    page.locator("#filesToUpload").set_input_files(absolute_path / "testfile1.pdf")
    expect(page.locator("#fileList li")).to_contain_text("testfile1")

    page.wait_for_timeout(5000)

def test_multiple_file_upload(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    absolute_path = Path.cwd() / "test_upload_download"

    files = [absolute_path / "testfile1.pdf", absolute_path / "testfile2.pdf"]
    page.locator("#filesToUpload").set_input_files(files)
    page.wait_for_timeout(3000)
    expect(page.locator("#fileList li").first).to_contain_text("testfile1")
    expect(page.locator("#fileList li").nth(1)).to_contain_text("testfile2")

    # Remove all selected files (clear input)
    page.locator("#filesToUpload").set_input_files([])
    # Validate cleared state
    expect(page.locator("#fileList li:nth-child(1)")).to_have_text("No Files Selected")

    page.wait_for_timeout(5000)