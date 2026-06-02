from playwright.sync_api import sync_playwright, expect, Page, Playwright


# Browser--> context---> page/s

def test_browser_context(playwright:Playwright):
    # chromium=playwright.chromium
    # browser=chromium.launch()

    # Browser will open a browser session
    browser=playwright.chromium.launch(headless=False)  # created browser

    # Context will open a new window
    context = browser.new_context() # created context
    context2 = browser.new_context()  # created context

    page1 = context.new_page()  # created page1
    page2 = context.new_page()  # created page2
    page3 = context2.new_page()  # created page 3 on context 2

    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(3000)
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    page2.goto("https://www.selenium.dev/")
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title("Selenium")

    page3.goto("https://davidwalsh.name/demo/multiple-file-upload.php")
    page2.wait_for_timeout(3000)

    # ── SWITCH FOCUS BACK TO PAGE 1 ──
    # Note: In playwright we dont need bring_to_front() just to operate on pages. You can interact with any open tab or
    # window completely in the background without bringing it to the visual foreground.
    # You only must use page.bring_to_front() if your test workflow includes:Taking Screenshots:
    # If you try to run page2.screenshot() while page1 is visually active, the screenshot will often come out blank,
    # corrupted, or show the wrong page content.
    # Physical Mouse Interactions: Actions like page2.hover() or complex
    # raw coordinate movements using page.mouse require the operating system to place physical visual focus on that page container.
    print("Page 1 URL is:", page1.url)
    page1.get_by_role("link", name="Docs").click()  # Interacts with Playwright page again
    page1.wait_for_timeout(2000)

    # ── SWITCH TO TAB 2 INSIDE CONTEXT 1 ──
    page2.bring_to_front()
    print("Now on Tab 2 URL:", page2.url)
    page2.get_by_role("link", name="Downloads").click()
    page2.wait_for_timeout(2000)


    # ── SWITCH FOCUS TO PAGE 3 of context 2 (In the other context window) ──
    page3.bring_to_front()
    # You can instantly interact with it because Playwright keeps track of the variable
    print("Page 3 URL is:", page3.url)
    page3.wait_for_timeout(2000)

    browser.close()

