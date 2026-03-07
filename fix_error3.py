import re

with open('index.html', 'r') as f:
    text = f.read()

# Let's insert the state declaration properly
text = text.replace(
    "const [modalConfig, setModalConfig] = useState(null);",
    "const [modalConfig, setModalConfig] = useState(null);\n            const [actionRollPrompt, setActionRollPrompt] = useState(null);"
)

with open('index.html', 'w') as f:
    f.write(text)
