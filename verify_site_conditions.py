from playwright.sync_api import sync_playwright
import os

def test_site_conditions():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        file_url = f"file://{os.path.abspath('index.html')}"
        page.goto(file_url)
        page.add_style_tag(content="* { font-family: sans-serif !important; }")

        page.click("text=Play Mode")

        page.fill("input[placeholder='Site Roll']", "4")
        page.locator("button.w-full.font-bold").first.click()

        page.wait_for_timeout(500)

        # At this point, we should be in Sweep phase and Site Condition should be shown.
        # But wait, Condition 4 is Level 2 dependent.
        # It should still show up. Let's see.

        page.screenshot(path="verification_site_conditions.png")

        browser.close()

if __name__ == "__main__":
    test_site_conditions()
