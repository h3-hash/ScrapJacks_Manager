import re

with open('index.html', 'r') as f:
    text = f.read()

old_execute_combat = """                let isYarddog = char.role.startsWith('Yarddog');
                let assistedNonYarddog = false;

                if (combatForm.isAssisted && !isYarddog) {
                    isYarddog = true;
                    assistedNonYarddog = true;
                }

                const sides = parseInt(char.vitals[vital].substring(1));
                const roll1 = rollDice(1, sides);
                const roll2 = isYarddog ? rollDice(1, sides) : 0;

                let baseAtk = manualAtk !== null ? manualAtk : (isYarddog ? Math.max(roll1, roll2) : roll1);

                // Attack Mods
                let atkMod = 0;
                const wEffects = wData?.effects || '';

                if (wEffects.includes('–1 to Melee attacks') && weaponType === 'melee') atkMod -= 1;
                if (tData.traits.includes('Low-Profile') && weaponType === 'ranged') atkMod -= 1;

                if (combatForm.isAiming) atkMod += 2;
                if (combatForm.isAssisted && char.role.startsWith('Yarddog')) atkMod += 2; // Yarddogs get flat +2 if assisted since they already have TDB

                let finalAtk = baseAtk + atkMod;
                let isNat1 = manualAtk !== null ? (manualAtk === 1) : (isYarddog ? (roll1 === 1 && roll2 === 1) : (roll1 === 1));

                if (wModData.effect.includes('Reroll 1s') && baseAtk === 1 && manualAtk === null) {
                    baseAtk = rollDice(1, sides);
                    finalAtk = baseAtk + atkMod;
                    isNat1 = baseAtk === 1;
                }

                let logMsg = `[COMBAT] ${char.name} attacked ${target.type} with ${weaponName}. Atk Roll: ${manualAtk !== null ? `[Manual: ${manualAtk}]` : (isYarddog ? `[${roll1}, ${roll2}]` : `[${roll1}]`)}`;
                if (atkMod !== 0) logMsg += ` (Mod: ${atkMod>0?'+':''}${atkMod})`;
                logMsg += ` -> Total: ${finalAtk}. `;

                if (finalAtk < 4) {
                    addLog(logMsg + "MISSED.");
                    updateLiveState(char.id, `used${vital.charAt(0).toUpperCase() + vital.slice(1)}`, true);
                    setCombatPrompt(null);
                    return;
                }"""


new_execute_combat = """                let isYarddog = char.role.startsWith('Yarddog');
                let assistedNonYarddog = false;

                if (combatForm.isAssisted && !isYarddog) {
                    isYarddog = true;
                    assistedNonYarddog = true;
                }

                const sides = parseInt(char.vitals[vital].substring(1));
                const roll1 = rollDice(1, sides);
                const roll2 = isYarddog ? rollDice(1, sides) : 0;

                let baseAtk = manualAtk !== null ? manualAtk : (isYarddog ? Math.max(roll1, roll2) : roll1);

                // Attack Mods
                let atkMod = 0;
                const wEffects = wData?.effects || '';

                if (wEffects.includes('–1 to Melee attacks') && weaponType === 'melee') atkMod -= 1;
                if (tData.traits.includes('Low-Profile') && weaponType === 'ranged') atkMod -= 1;

                if (combatForm.isAiming) atkMod += 2;
                if (combatForm.isAssisted && char.role.startsWith('Yarddog')) atkMod += 2; // Yarddogs get flat +2 if assisted since they already have TDB

                let finalAtk = baseAtk + atkMod;
                let isNat1 = manualAtk !== null ? (manualAtk === 1) : (isYarddog ? (roll1 === 1 && roll2 === 1) : (roll1 === 1));

                if (wModData.effect.includes('Reroll 1s') && baseAtk === 1 && manualAtk === null) {
                    baseAtk = rollDice(1, sides);
                    finalAtk = baseAtk + atkMod;
                    isNat1 = baseAtk === 1;
                }

                let isCritSuccess = (!assistedNonYarddog && isYarddog && manualAtk === null && roll1 === roll2 && baseAtk >= 4);
                let isCritFumble = (!assistedNonYarddog && isYarddog && manualAtk === null && roll1 === roll2 && baseAtk < 4);

                let logMsg = `[COMBAT] ${char.name} attacked ${target.type} with ${weaponName}. Atk Roll: ${manualAtk !== null ? `[Manual: ${manualAtk}]` : (isYarddog ? `[${roll1}, ${roll2}]` : `[${roll1}]`)}`;
                if (atkMod !== 0) logMsg += ` (Mod: ${atkMod>0?'+':''}${atkMod})`;
                logMsg += ` -> Total: ${finalAtk}. `;

                if (isCritSuccess && finalAtk >= 4) {
                    logMsg += "CRITICAL SUCCESS! Die is NOT expended. ";
                } else if (isCritFumble) {
                    logMsg += "CRITICAL FUMBLE! Activation ends immediately. -1 Aircharge. ";
                    setAircharge(prev => Math.max(0, prev - 1));
                    updateLiveState(char.id, 'usedMove', true);
                    updateLiveState(char.id, 'usedLoad', true);
                    updateLiveState(char.id, 'usedFocus', true);
                    updateLiveState(char.id, 'usedGrit', true);
                    setCombatPrompt(null);
                    addLog(logMsg);
                    return;
                } else {
                    updateLiveState(char.id, `used${vital.charAt(0).toUpperCase() + vital.slice(1)}`, true);
                }

                if (finalAtk < 4) {
                    addLog(logMsg + "MISSED.");
                    setCombatPrompt(null);
                    return;
                }"""

text = text.replace(old_execute_combat, new_execute_combat)
with open('index.html', 'w') as f:
    f.write(text)
