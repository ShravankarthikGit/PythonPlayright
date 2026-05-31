from playwright.sync_api import Page, expect


def test_dummy_ticket_booking(page: Page):
    page.goto("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    page.locator("#product_549:visible").click()
    page.locator("#travname").fill("Akash")
    page.locator("#travlastname").fill("rotore")
    # Open the date picker for Date of Birth and select: Year: "2001", Month: "Mar", Date: "2".

    page.locator("[name='dob']").click()
    page.get_by_label("Select month").select_option(value='2')
    page.get_by_label("Select year").select_option(value='2001')
    dates = page.locator(".ui-datepicker-calendar tbody td a")
    for date in dates.all():
        if date.inner_text().strip() == "2":
            date.click()
            break
    page.locator("#sex_1:visible").click()

    # travel details
    page.get_by_label("One Way").click()
    page.locator("[name='fromcity']").fill("Toronto")
    page.locator("#tocity:visible").fill("Mumbai")
    # Open the date picker for departure date and select: Year: "2024", Month: "Nov", Date: "25".
    page.locator("#departon:visible").click()

    page.get_by_label("Select month").select_option(value='10')
    page.get_by_label("Select year").select_option(value='2026')
    dates = page.locator(".ui-datepicker-calendar tbody td a")
    for date in dates.all():
        if date.inner_text().strip() == "25":
            date.click()
            break
    page.locator("#notes").fill("Need visa as soon as possible")

    page.locator('#select2-reasondummy-container').click()
    page.locator('.select2-results li:first-child').click()
    #Open the date picker for appointment date and select: Year: "2026", Month: "Dec", Date: "10".
    page.locator("#appoinmentdate").click()
    page.get_by_label("Select month").select_option(value='11')
    page.get_by_label("Select year").select_option(value='2026')
    dates = page.locator(".ui-datepicker-calendar tbody td a")
    for date in dates.all():
        if date.inner_text().strip() == "10":
            date.click()
            break
    page.get_by_label("Email", exact=True).click()
    page.locator("#billing_email").fill("test@gmail.com")
    page.locator("#select2-billing_country-container").click()
    page.locator("li").filter(has_text="Canada").click()
    page.get_by_placeholder("House number and street name").fill("123 Scott Street")
    page.locator("#billing_city").fill("Niagara Falls")
    page.locator("#select2-billing_state-container:visible").click()
    page.locator("li").filter(has_text="Ontario").click()
    page.locator("#billing_postcode").fill("L2C 6M1")

    # Verify Product details table
    product_name = page.locator('.product-details')
    print("Product Name=====>:", product_name.inner_text())
    expect(product_name).to_contain_text("Dummy")

    product_price = page.locator('.shop_table.woocommerce-checkout-review-order-table .cart_item.opc_cart_item ')
    print("Product Price=====>:",product_price.inner_text())
    expect(product_price).to_contain_text("USD")

    # Place order
    page.locator('#place_order').click()



    page.wait_for_timeout(5000)