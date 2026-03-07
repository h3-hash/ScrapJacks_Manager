import re

with open('index.html', 'r') as f:
    text = f.read()

# Let's replace the whole onClick logic for Redline Grit roll
old_onclick = """                                            <button onClick={() => {
                                                const sides = parseInt(char.vitals.grit.substring(1));
                                                const roll = getRoll(redlinePrompt.manualRoll, 1, sides);
                                                if (roll >= 4) {
                                                    addLog(`[REDLINE] ${char.name} rolled ${redlinePrompt.manualRoll ? `[Manual: ${roll}]` : roll} on Grit. They are clinging to life!`);
                                                    setRedlinePrompt({ ...redlinePrompt, step: 'revive' });
                                                } else {
                                                    addLog(`[REDLINE] ${char.name} rolled ${redlinePrompt.manualRoll ? `[Manual: ${roll}]` : roll} on Grit. They did not survive.`);
                                                    updateCharacter(char.id, 'status', 'Dead');
                                                    setRedlinePrompt(null);
                                                }
                                            }}"""

new_onclick = """                                            <button onClick={() => {
                                                const sides = parseInt(char.vitals.grit.substring(1));
                                                const manualVal = redlinePrompt.manualRoll ? parseInt(redlinePrompt.manualRoll) : null;
                                                let roll1 = manualVal || rollDice(1, sides);
                                                let roll2 = null;
                                                let isTdb = ROLES[char.role]?.tdb?.includes('Resist Stress');

                                                let finalRoll = roll1;
                                                let logText = manualVal ? `[Manual: ${roll1}]` : `Rolled ${roll1}`;

                                                if (isTdb && !manualVal) {
                                                    roll2 = rollDice(1, sides);
                                                    finalRoll = Math.max(roll1, roll2);
                                                    logText = `[TDB: ${roll1}, ${roll2} -> ${finalRoll}]`;
                                                }

                                                let isCritSuccess = (isTdb && roll2 !== null && roll1 === roll2 && finalRoll >= 4);
                                                let isCritFumble = (isTdb && roll2 !== null && roll1 === roll2 && finalRoll < 4);

                                                if (finalRoll >= 4) {
                                                    let msg = `[REDLINE] ${char.name} rolled Grit (${char.vitals.grit}): ${logText} -> SUCCESS. They are clinging to life!`;
                                                    if (isCritSuccess) msg += " CRITICAL SUCCESS!";
                                                    addLog(msg);
                                                    setRedlinePrompt({ ...redlinePrompt, step: 'revive' });
                                                } else {
                                                    let msg = `[REDLINE] ${char.name} rolled Grit (${char.vitals.grit}): ${logText} -> FAILED. They did not survive.`;
                                                    if (isCritFumble) msg += " CRITICAL FUMBLE!";
                                                    setAircharge(prev => Math.max(0, prev - 1));
                                                    addLog(msg + " -1 Aircharge.");
                                                    updateCharacter(char.id, 'status', 'Dead');
                                                    setRedlinePrompt(null);
                                                }
                                            }}"""

text = text.replace(old_onclick, new_onclick)

with open('index.html', 'w') as f:
    f.write(text)
