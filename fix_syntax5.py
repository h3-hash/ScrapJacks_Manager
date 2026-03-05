import re

with open('index.html', 'r') as f:
    text = f.read()

# Fix the JSX parsing error on line 5021: "<4" should be encoded as "&lt;4"
text = text.replace("(<4)", "(&lt;4)")

with open('index.html', 'w') as f:
    f.write(text)
