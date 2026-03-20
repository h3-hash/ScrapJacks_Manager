from playwright.sync_api import sync_playwright
import os

def test_spawns():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        file_url = f"file://{os.path.abspath('index.html')}"
        page.goto(file_url)
        page.add_style_tag(content="* { font-family: sans-serif !important; }")

        page.click("text=Play Mode")

        page.fill("input[placeholder='Site Roll']", "2")
        page.click("button:has-text('Breach and advance to Sweep')")
        page.wait_for_timeout(500)

        page.fill("input[placeholder='Hitch Roll']", "6")
        page.click("button:has-text('Advance to Hitch')")
        page.wait_for_timeout(1000)

        logs = page.locator(".font-mono.text-\\[11px\\] > div").all_inner_texts()
        print("Logs:")
        print(logs)

        err_msg = page.locator("text=A Application Error Occurred")
        if err_msg.is_visible():
            print("App crashed! Error details:")
            print(page.locator("pre").inner_text())

        browser.close()

if __name__ == "__main__":
    test_spawns()
