from playwright.sync_api import Page, expect


# 1) Launch application
# 	https://demowebshop.tricentis.com/
# 2) Verify logo presence/visibility
# 3) Capture all the computer related products and verify the count . Count should be 4
# 4) Print name of the first product
# 5) Print name of the last product
# 6) Print name of the nth product
# 7) Print titles of all the all products  (Tip: all_text_contents())
# 8) get the fist. last and nth link from the footer section


def test_verify_js_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect(page.get_by_alt_text("Tricentis Demo Web Shop")).to_be_visible()
    page.wait_for_timeout(5000)