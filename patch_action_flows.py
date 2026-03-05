import re

with open('index.html', 'r') as f:
    text = f.read()

# I need to update confirmActionRoll so that "Melee Combat", "Ranged Combat", and "Push" do NOT just run the generic roll logic.
# They should trigger setCombatPrompt or handlePush instead.

old_logic = """            const confirmActionRoll = (charId, vital, actionName) => {
                saveHistory();
                const char = crew.find(c => c.id === charId);
                const sides = parseInt(char.vitals[vital].substring(1));
                const manualVal = charRollInputs[charId];"""

new_logic = """            const confirmActionRoll = (charId, vital, actionName) => {
                const char = crew.find(c => c.id === charId);
                if (actionName === 'Melee Combat') {
                    setCombatPrompt({ charId, weaponType: 'melee' });
                    setActionRollPrompt(null);
                    return;
                }
                if (actionName === 'Ranged Combat') {
                    setCombatPrompt({ charId, weaponType: 'ranged' });
                    setActionRollPrompt(null);
                    return;
                }
                if (actionName === 'Push') {
                    handlePush(charId);
                    setActionRollPrompt(null);
                    return;
                }

                saveHistory();
                const sides = parseInt(char.vitals[vital].substring(1));
                const manualVal = charRollInputs[charId];"""

text = text.replace(old_logic, new_logic)

with open('index.html', 'w') as f:
    f.write(text)
