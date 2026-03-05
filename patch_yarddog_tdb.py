import re

with open('index.html', 'r') as f:
    text = f.read()

# Fix TDB matching for Yarddogs
old_match_tdb = """// Check if this action triggers TDB for this character
                                            const roleTdbText = ROLES[char.role]?.tdb || '';
                                            const isTdb = roleTdbText.includes(name);"""

new_match_tdb = """// Check if this action triggers TDB for this character
                                            const roleTdbText = ROLES[char.role]?.tdb || '';
                                            const isTdb = roleTdbText.includes(name) || (name === 'Push' && roleTdbText.includes('Push'));"""

text = text.replace(old_match_tdb, new_match_tdb)

old_match_tdb2 = """// Determine if they get TDB based on their Role
                const roleTdbText = ROLES[char.role]?.tdb || '';
                if (roleTdbText.includes(actionName)) {
                    isTdb = true;
                }"""

new_match_tdb2 = """// Determine if they get TDB based on their Role
                const roleTdbText = ROLES[char.role]?.tdb || '';
                if (roleTdbText.includes(actionName) || (actionName === 'Push' && roleTdbText.includes('Push'))) {
                    isTdb = true;
                }"""

text = text.replace(old_match_tdb2, new_match_tdb2)

with open('index.html', 'w') as f:
    f.write(text)
