from playwright.sync_api import sync_playwright
import os

def test_babel():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Read index.html
        with open("index.html", "r") as f:
            content = f.read()
        script = content.split('<script type="text/babel">')[1].split('</script>')[0]

        with open("test_babel.html", "w") as f:
            f.write(f"""<!DOCTYPE html>
<html>
<head>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
</head>
<body>
<div id="output">Running...</div>
<script>
window.onerror = function(message, source, lineno, colno, error) {{
    document.getElementById("output").innerText = message + " at line " + lineno;
}};
</script>
<script type="text/javascript">
const code = `{script.replace('`', '\\`').replace('$', '\\$')}`;
try {{
  Babel.transform(code, {{ presets: ['react'] }});
  document.getElementById("output").innerText = "Syntax OK";
}} catch(e) {{
  document.getElementById("output").innerText = e.message;
}}
</script>
</body>
</html>""")

        file_url = f"file://{os.path.abspath('test_babel.html')}"
        page.goto(file_url)
        page.wait_for_timeout(2000)
        print(page.locator("#output").inner_text())
        browser.close()

if __name__ == "__main__":
    test_babel()
