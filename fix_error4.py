import re

with open('index.html', 'r') as f:
    text = f.read()

# Make sure actionRollPrompt check doesn't conflict with other prompts blocking it.
# Check what is blocking it
print(text.find("{actionRollPrompt &&"))
