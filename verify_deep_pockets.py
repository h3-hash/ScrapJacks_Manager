from playwright.sync_api import sync_playwright
import os

def test_deep_pockets():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        file_url = f"file://{os.path.abspath('index.html')}"
        page.goto(file_url)
        page.add_style_tag(content="* { font-family: sans-serif !important; }")

        # Select Roster tab explicitly
        # Actually it starts on Roster.

        # Change first character's knack to Deep Pocket
        page.locator("select").filter(has_text="Space Ballet").first.select_option(label="Deep Pocket")

        # Let's see the text in Play Mode to trigger quiet pull.
        page.click("button:has-text('Play Mode')")

        page.fill("input[placeholder='1d8']", "3")
        page.click("button:has-text('Quiet Pull')")

        # In Play Mode, the quiet pull active panel appears.
        # "QUIET PULL ACTIVE"
        # Click "Success" button to resolve the quiet pull.
        page.click("button:has-text('Success')")

        # Now go back to Roster
        page.click("button:has-text('Roster')")

        page.wait_for_timeout(500)

        # Assign "Utility Choice" to the first character
        locker_item = page.locator(".bg-slate-800", has_text="Utility Choice")
        locker_item.locator("select").select_option(index=1)

        page.wait_for_timeout(500)

        page.select_option("select#choiceSelection", label="Med-Kit")
        page.click("button:has-text('Confirm Assignment')")

        page.wait_for_timeout(500)

        page.screenshot(path="verification_deep_pockets.png")

        browser.close()

if __name__ == "__main__":
    test_deep_pockets()
