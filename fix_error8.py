import re

with open('index.html', 'r') as f:
    text = f.read()

# Let's inspect triggerActionRoll to make sure it's bound.
start = text.find("const triggerActionRoll")
print(text[start:start+100])
