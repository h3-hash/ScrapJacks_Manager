import re
with open('index.html', 'r') as f:
    text = f.read()

# I need to find the React state declarations and add an actionRollPrompt.
match = re.search(r'const \[modalConfig, setModalConfig\] = React\.useState\(null\);', text)
if match:
    insert_pos = match.end()
    text = text[:insert_pos] + "\n            const [actionRollPrompt, setActionRollPrompt] = React.useState(null);" + text[insert_pos:]

# Replace handleStandardRoll with logic to trigger the modal
old_handle_standard_roll = """            const handleStandardRoll = (charId, vital) => {
                saveHistory();
                const char = crew.find(c => c.id === charId);
                const sides = parseInt(char.vitals[vital].substring(1));
                const manualVal = charRollInputs[charId];

                const roll = manualVal ? parseInt(manualVal) : rollDice(1, sides);
                const success = roll >= 4;

                updateLiveState(charId, `used${vital.charAt(0).toUpperCase() + vital.slice(1)}`, true);
                updateCharRollInput(charId, '');

                addLog(`[ACTION] ${char.name} rolled ${vital.toUpperCase()} (${char.vitals[vital]}): ${manualVal ? `[Manual: ${roll}]` : `Rolled ${roll}`} -> ${success ? 'SUCCESS' : 'FAILED'}.`);
            };"""

new_handle_standard_roll = """            const triggerActionRoll = (charId, vital) => {
                setActionRollPrompt({ charId, vital });
            };

            const confirmActionRoll = (charId, vital, actionName) => {
                saveHistory();
                const char = crew.find(c => c.id === charId);
                const sides = parseInt(char.vitals[vital].substring(1));
                const manualVal = charRollInputs[charId];

                let roll1 = manualVal ? parseInt(manualVal) : rollDice(1, sides);
                let roll2 = null;
                let isTdb = false;

                // Determine if they get TDB based on their Role
                const roleTdbText = ROLES[char.role]?.tdb || '';
                if (roleTdbText.includes(actionName)) {
                    isTdb = true;
                }

                let finalRoll = roll1;
                let logText = manualVal ? `[Manual: ${roll1}]` : `Rolled ${roll1}`;

                if (isTdb && !manualVal) {
                    roll2 = rollDice(1, sides);
                    finalRoll = Math.max(roll1, roll2);
                    logText = `[TDB: ${roll1}, ${roll2} -> ${finalRoll}]`;
                }

                const success = finalRoll >= 4;
                let isCritSuccess = false;
                let isCritFumble = false;
                let logMsg = `[ACTION: ${actionName}] ${char.name} rolled ${vital.toUpperCase()} (${char.vitals[vital]}): ${logText} -> ${success ? 'SUCCESS' : 'FAILED'}.`;

                if (isTdb && roll2 !== null && roll1 === roll2) {
                    if (success) {
                        isCritSuccess = true;
                        logMsg += ` CRITICAL SUCCESS! Die is NOT expended.`;
                    } else {
                        isCritFumble = true;
                        logMsg += ` CRITICAL FUMBLE! Activation ends immediately. -1 Aircharge.`;
                        setAircharge(prev => Math.max(0, prev - 1));
                    }
                }

                if (!isCritSuccess) {
                    // Expend the die unless it's a Grit action that passed
                    if (vital === 'grit' && actionName.includes('Resist') && success) {
                        logMsg += ` (Grit die retained on success).`;
                    } else if (actionName === 'Push') {
                        // Push is handled separately or we log it here
                        logMsg += ` (Push costs 1 AC regardless).`;
                        setAircharge(prev => Math.max(0, prev - 1));
                        updateLiveState(charId, `used${vital.charAt(0).toUpperCase() + vital.slice(1)}`, true);
                    } else {
                        updateLiveState(charId, `used${vital.charAt(0).toUpperCase() + vital.slice(1)}`, true);
                    }
                }

                if (isCritFumble) {
                    // End activation = spend all dice (or just mark them pushed/done)
                    updateLiveState(charId, 'usedMove', true);
                    updateLiveState(charId, 'usedLoad', true);
                    updateLiveState(charId, 'usedFocus', true);
                    updateLiveState(charId, 'usedGrit', true);
                }

                if (actionName === 'Push' && success && !isCritFumble) {
                    updateLiveState(charId, 'usedMove', false);
                    updateLiveState(charId, 'usedLoad', false);
                    updateLiveState(charId, 'usedFocus', false);
                    updateLiveState(charId, 'usedGrit', false);
                    updateLiveState(charId, 'pushed', true);
                    logMsg += ` Regained Free Move and Full Action Dice Pool.`;
                }

                updateCharRollInput(charId, '');
                addLog(logMsg);
                setActionRollPrompt(null);
            };"""

text = text.replace(old_handle_standard_roll, new_handle_standard_roll)

# We also need to change the onClick from handleStandardRoll to triggerActionRoll
text = text.replace("onClick={() => handleStandardRoll(char.id, v)}", "onClick={() => triggerActionRoll(char.id, v)}")

with open('index.html', 'w') as f:
    f.write(text)
