import re

with open('index.html', 'r') as f:
    text = f.read()

# Let's insert the state declaration
match = re.search(r'const \[modalConfig, setModalConfig\] = React\.useState\(null\);', text)
if match:
    insert_pos = match.end()
    text = text[:insert_pos] + "\n            const [actionRollPrompt, setActionRollPrompt] = React.useState(null);" + text[insert_pos:]
else:
    print("Could not find modalConfig!")

with open('index.html', 'w') as f:
    f.write(text)
