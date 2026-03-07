import re

with open('index.html', 'r') as f:
    text = f.read()

# Is `actionRollPrompt` undefined when rendering because it's caught in some outer scope closure?
# The state is defined at the very top of `App` component!
match = re.search(r'const \[actionRollPrompt, setActionRollPrompt\] = useState\(null\);', text)
print("State found:", match is not None)

# If it's correctly defined and triggering the function updates it, why wouldn't the UI update?
# Maybe the script clicked a different "Roll" button? There are manual roll buttons (e.g. "Site Roll", "Hazard Roll") in the phase overrides!
# Ah! In the Playwright script:
# roll_btn = page.locator("div.bg-slate-800.border-slate-700 >> button:has-text('Roll')").first
# Did that click the dice roll? Let's check the Playwright test failure. It says:
# "Timeout 30000ms exceeded." waiting for "Select Action" to be visible.

# Let's write a playwright script that strictly finds the button:
