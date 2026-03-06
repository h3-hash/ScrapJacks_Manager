import re

with open('index.html', 'r') as f:
    content = f.read()

# I also need to make sure undoAction handles it if it is included in turnHistory?
# We didn't add it to turnHistory... let's add it.
content = content.replace(
    'playLog: [...playLog],',
    'playLog: [...playLog],\n                    rolledSiteConditions: [...rolledSiteConditions],'
)

content = content.replace(
    'setPlayLog([`[Turn ${turnHistory.turn} - ${turnHistory.phase}] Undo: Reverted last action.`, ...turnHistory.playLog]);',
    'setPlayLog([`[Turn ${turnHistory.turn} - ${turnHistory.phase}] Undo: Reverted last action.`, ...turnHistory.playLog]);\n                if(turnHistory.rolledSiteConditions) setRolledSiteConditions([...turnHistory.rolledSiteConditions]);'
)

with open('index.html', 'w') as f:
    f.write(content)
