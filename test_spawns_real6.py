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

        # Click the button directly using a more robust selector
        # It's the button inside the manual overrides section or just the main phase button
        page.click("button:has-text('Advance to Hitch')")
        page.wait_for_timeout(1000)

        err_msg = page.locator("text=A Application Error Occurred")
        if err_msg.is_visible():
            print("App crashed! Error details:")
            print(page.locator("pre").inner_text())

        enemy_cards = page.locator(".bg-slate-900.border-red-900").all()
        print(f"Number of enemy cards spawned: {len(enemy_cards)}")
        if len(enemy_cards) > 0:
            print("Enemy spawned!")
            print(enemy_cards[0].inner_text().replace('\n', ' '))

        browser.close()

if __name__ == "__main__":
    test_spawns()
