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
        page.click("text=Breach and advance to Sweep")
        page.wait_for_timeout(500)

        page.fill("input[placeholder='Hitch Roll']", "6")
        page.click("text=Advance to Hitch")
        page.wait_for_timeout(1000)

        enemy_cards = page.locator(".bg-slate-900.border-red-900").all()
        print(f"Number of enemy cards spawned: {len(enemy_cards)}")

        if len(enemy_cards) > 0:
            print(enemy_cards[0].inner_text().replace('\n', ' '))
            page.screenshot(path="verification_spawns.png")

        browser.close()

if __name__ == "__main__":
    test_spawns()
