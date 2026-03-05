import re

with open('index.html', 'r') as f:
    text = f.read()

# Did it replace correctly?
if "const manualVal = redlinePrompt.manualRoll" not in text:
    print("Replace failed!")

# Wait, `getRoll(redlinePrompt.manualRoll` was probably not exactly formatted like that in index.html.
match = re.search(r'const sides = parseInt\(char\.vitals\.grit\.substring\(1\)\);\s+const roll = getRoll\(redlinePrompt\.manualRoll, 1, sides\);\s+if \(roll >= 4\) \{', text)
if match:
    print("Found it!")
    text = text[:match.start()] + """const sides = parseInt(char.vitals.grit.substring(1));
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
                                                    if (isCritFumble) {
                                                        msg += " CRITICAL FUMBLE! -1 Aircharge.";
                                                    }
                                                    setAircharge(prev => Math.max(0, prev - 1));
                                                    addLog(msg);
                                                    updateCharacter(char.id, 'status', 'Dead');
                                                    setRedlinePrompt(null);
                                                }""" + text[match.end():]

    # We also need to remove the old lines after if(roll>=4) that I didn't match.
    # Actually, I matched `if (roll >= 4) {`, so the next lines are `addLog(...) setRedlinePrompt(...) } else { addLog(...) ... }`
    # My replacement code replaces those too, wait, no, my replacement code INCLUDES the `if(finalRoll >= 4)` and its branches, so I need to replace the entire `if(roll >= 4) { ... }` block!
