import re

with open("index.html", "r") as f:
    content = f.read()

pattern = r"// Temporarily add to locker with new ID.*?(const charObj = crew\.find)"
new_text = r"\1"

content = re.sub(pattern, new_text, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)
