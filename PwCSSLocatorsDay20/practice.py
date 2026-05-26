from playwright.sync_api import Page, expect


# 1) Launch application
# 	https://demowebshop.tricentis.com/
# 2) Verify logo presence/visibility
# 3) click on computers, capture all values under computers
# 4) Print name of the first product
# 5) Print name of the last product
# 6) Print name of the nth product


def test_verify_js_locators(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    expect(page.get_by_alt_text("Tricentis Demo Web Shop")).to_be_visible()
    page.wait_for_timeout(5000)

    # click on the computers menu option
    page.locator(".block-category-navigation").get_by_role("link", name="Computers", exact=True).click()
    page.wait_for_timeout(5000)

    # This will give actual list of all web elements
    computer_elements = page.locator("ul[class='sublist'] li a").all()
    for i in range(len(computer_elements)):
        print(computer_elements[i].inner_text().strip())

    first_product_name = computer_elements[0].inner_text().strip()
    print(first_product_name)

    last_product_name = computer_elements[-1].inner_text().strip()
    print(last_product_name)

    n=1
    nth_product_name = computer_elements[n].inner_text().strip()
    print(nth_product_name)
