import re

with open('index.html', 'r') as f:
    content = f.read()

content = content.replace(
    'setMissionLevel(1);\n                setActiveObjectives([]);',
    'setMissionLevel(1);\n                setRolledSiteConditions([]);\n                setActiveObjectives([]);'
)

with open('index.html', 'w') as f:
    f.write(content)
