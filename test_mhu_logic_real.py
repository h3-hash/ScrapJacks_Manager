from playwright.sync_api import sync_playwright
import os

def test_mhu():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_url = f"file://{os.path.abspath('index.html')}"
        page.goto(file_url)
        page.add_style_tag(content="* { font-family: sans-serif !important; }")

        page.click("text=Play Mode")
        page.select_option("select:has-text('Level 1')", label="Level 3")

        page.fill("input[placeholder='Site Roll']", "7")
        page.locator("button.w-full.font-bold").first.click()
        page.wait_for_timeout(500)

        # Test POI in MHU 1
        page.click("button:has-text('Point of Interest (POI)')")
        page.fill("input[placeholder='Manual Roll (Opt)']", "1")
        page.click("button:has-text('Roll POI')")
        page.wait_for_timeout(500)

        page.locator("button:has-text('[RESOLVE]')").first.click()
        page.wait_for_timeout(500)

        page.locator("div.fixed.inset-0 button").filter(has_text="Success").click()
        page.wait_for_timeout(500)

        logs = page.locator(".font-mono.text-\\[11px\\] > div").all_inner_texts()
        print("Logs MHU 1:")
        for l in logs[:5]:
            print(l)

        # Get to MHU 3
        for i in range(2):
            page.click("text=Prepare to Breach")
            page.click("text=Breach Next MHU")
            page.locator("button.w-full.font-bold").first.click() # Breach to Sweep

        page.click("button:has-text('Point of Interest (POI)')")
        page.wait_for_timeout(500)
        try:
            page.fill("input[placeholder='Manual Roll (Opt)']", "2")
        except:
            pass
        page.click("button:has-text('Roll POI')")
        page.wait_for_timeout(500)

        page.locator("button:has-text('[RESOLVE]')").last.click()
        page.wait_for_timeout(500)
        page.locator("div.fixed.inset-0 button").filter(has_text="Success").click()
        page.wait_for_timeout(500)

        logs = page.locator(".font-mono.text-\\[11px\\] > div").all_inner_texts()
        print("Logs MHU 3:")
        for l in logs[:10]:
            print(l)

        page.screenshot(path="verification_mhu_logic.png")

        browser.close()

if __name__ == "__main__":
    test_mhu()
