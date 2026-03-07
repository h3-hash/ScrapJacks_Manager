import re
with open('index.html', 'r') as f:
    text = f.read()

# Let's fix the bug in my ACTION_TYPES injection. I might have replaced WEAPONS_MELEE weirdly.
# Wait, I did:
# const ACTION_TYPES = { ... };
# text = text.replace("const WEAPONS_MELEE", action_types + "\n        const WEAPONS_MELEE")
# And then I added a bunch of literal JS template string. Let's see if ACTION_TYPES is in there.
print("ACTION_TYPES found:", "const ACTION_TYPES =" in text)
