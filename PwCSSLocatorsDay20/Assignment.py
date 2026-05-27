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

    #  using CSS selctor
    # products = page.locator("div.product-grid.home-page-product-grid .product-item a").all()
    # for product in products:
    #     value = product.inner_text().strip()
    #     if "computer" in value:
    #         print(product.inner_text())

    #   Using playwright
    # # 1. Target all product links first
    # all_titles = page.locator("div.product-grid.home-page-product-grid .product-title a")
    # # 2. Apply a Playwright filter method
    # computer_titles = all_titles.filter(has_text="computer").all()
    # # 3. Print the results directly
    # # for title in computer_titles:
    # #     print(title.inner_text().strip())
    #
    # # first product
    # print(computer_titles[1].inner_text() + " is the first product")
    #
    # # last product
    # print(computer_titles[-1].inner_text() + " is the last product")
    #
    # # nth product
    # n = 1
    # print(computer_titles[n].inner_text() + f" is the {n} product")

    # Using CSS contains
    all_titles = page.locator(".product-grid.home-page-product-grid h2>a[href*='computer']")

    # first product
    print(all_titles.first.text_content()+ " is the first product")

    # last product
    print(all_titles.last.text_content() + " is the last product")

    # nth product
    n = 1
    print(all_titles.nth(n).text_content() + f" is the {n} product")

    for title in all_titles.all_text_contents():
        print(title)

    # Products starting with "/build" in href attribute
    building_products = page.locator('h2 > a[href^="/build"]')   # [href^="/build"] mimics XPath starts-with()
    expect(building_products).to_have_count(3)

    # Register link using CSS selector with exact text match
    register_link = page.locator('a[href="/register"]')
    expect(register_link).to_be_visible()

    # Last social media link (Google+) using :last-child
    # ul stands for unordered list, ul is from html
    # li is for list, li is from html  div .follow-us ul li:last-child
    google_plus_link = page.locator('.follow-us ul li:last-child')
    expect(google_plus_link).to_have_text("Google+")

    # Second social media link (Twitter) using :nth-child(2)
    twitter_link = page.locator('.follow-us ul li:nth-child(2)')
    expect(twitter_link).to_have_text("Twitter")






