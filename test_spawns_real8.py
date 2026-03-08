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
        # Try to click the first button with .w-full.font-bold
        print(page.locator("button.w-full.font-bold").first.inner_text())
        page.locator("button.w-full.font-bold").first.click()
        page.wait_for_timeout(1000)

        logs = page.locator(".font-mono.text-\\[11px\\] > div").all_inner_texts()
        print("Logs:")
        for log in logs:
            print(log)

        print("Active Enemies HTML:")
        print(page.locator(".bg-slate-800.p-4.rounded-xl.border.border-red-900\\/50").inner_html())

        browser.close()

if __name__ == "__main__":
    test_spawns()
