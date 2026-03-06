import re

with open('index.html', 'r') as f:
    content = f.read()

# I also need to make sure applyNewCrew resets it.
content = content.replace(
    'setMissionLevel(1);\n                setAcrDebt(SHIPS[\'Class C - Tug\'].acr);',
    'setMissionLevel(1);\n                setRolledSiteConditions([]);\n                setAcrDebt(SHIPS[\'Class C - Tug\'].acr);'
)

with open('index.html', 'w') as f:
    f.write(content)
