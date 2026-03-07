import re

with open('index.html', 'r') as f:
    text = f.read()

# I see what happened. I used setActionRollPrompt but actionRollPrompt wasn't properly initialized!
# Let me look for where I injected actionRollPrompt.
print(text.find('const [actionRollPrompt, setActionRollPrompt]'))
