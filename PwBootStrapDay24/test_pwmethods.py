from playwright.sync_api import Page, expect


def test_comparisonofmethods(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    products = page.locator(".product-title")  # 6 products

    # 1) inner_text() vs text_content()
    # Note that text_content() will return spaces when printed
    # print("Using inner_text()====> ",products.nth(1).inner_text()) # return actual text
    # print("Using inner_text()====> ", products.nth(1).inner_text())
    # print("Using text_content()====> ",products.nth(1).text_content()) # returns content with special chars and spaces

    # count=products.count()
    # for i in range(count):
    #     product_name=products.nth(i).text_content()
    #     # without strip we will see exact difference in the print
    #     # print(product_name.strip())
    #     print(product_name)
    #
    #     product_name = products.nth(i).inner_text()
    #     print(product_name)

    # 2) all_inner_texts() vs all_text_contents()
    # product_names_inner_text = products.all_inner_texts()
    # print(product_names_inner_text)
    # product_names = products.all_text_contents()
    # print(product_names)
    # products_names_trimmed=[text.strip() for text in product_names]
    # print(products_names_trimmed)

    # 3) all() - converts locator to list of locators
    product_locators = products.all()
    print(product_locators[0].inner_text())


    for product_loc in product_locators:
        print(product_loc.inner_text())

    for i in range(len(product_locators)):
        print(product_locators[i].inner_text())
