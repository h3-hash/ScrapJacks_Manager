import re

with open('index.html', 'r') as f:
    text = f.read()

# Fix handlePush to handle critical rolls.
old_handle_push = """                if (isYarddog && parsedVal === null) {
                    let roll2 = rollDice(1, sides);
                    finalRoll = Math.max(roll1, roll2);
                    logText = `[Grit (TDB): ${roll1}, ${roll2} -> ${finalRoll}]`;
                }

                updateCharRollInput(char.id, '');

                if (finalRoll >= 4) {
                    setCrew(prev => prev.map(c => {
                        if (c.id === char.id) {
                            return { ...c, live: { ...c.live, pushed: true, usedMove: false, usedLoad: false, usedFocus: false, usedGrit: false } };
                        }
                        return c;
                    }));
                    addLog(`Push Action: ${char.name} SUCCESS (-1 AC) ${logText}. Regained Free Move and Full Action Dice Pool.`);
                } else {
                    setCrew(prev => prev.map(c => {
                        if (c.id === char.id) {
                            return { ...c, live: { ...c.live, pushed: true } };
                        }
                        return c;
                    }));
                    addLog(`Push Action: ${char.name} FAILED (-1 AC) ${logText}. Action lost.`);
                }"""

new_handle_push = """                let roll2 = null;
                if (isYarddog && parsedVal === null) {
                    roll2 = rollDice(1, sides);
                    finalRoll = Math.max(roll1, roll2);
                    logText = `[Grit (TDB): ${roll1}, ${roll2} -> ${finalRoll}]`;
                }

                let isCritSuccess = (isYarddog && roll2 !== null && roll1 === roll2 && finalRoll >= 4);
                let isCritFumble = (isYarddog && roll2 !== null && roll1 === roll2 && finalRoll < 4);

                updateCharRollInput(char.id, '');

                if (finalRoll >= 4) {
                    setCrew(prev => prev.map(c => {
                        if (c.id === char.id) {
                            return { ...c, live: { ...c.live, pushed: true, usedMove: false, usedLoad: false, usedFocus: false, usedGrit: false } };
                        }
                        return c;
                    }));
                    let msg = `Push Action: ${char.name} SUCCESS (-1 AC) ${logText}. Regained Free Move and Full Action Dice Pool.`;
                    if (isCritSuccess) msg += " CRITICAL SUCCESS! Grit die remains active (not applicable to Push refresh).";
                    addLog(msg);
                } else {
                    let msg = `Push Action: ${char.name} FAILED (-1 AC) ${logText}. Action lost.`;
                    if (isCritFumble) {
                        msg += " CRITICAL FUMBLE! Activation ends immediately. -1 additional Aircharge.";
                        setAircharge(prev => Math.max(0, prev - 1));
                    }
                    setCrew(prev => prev.map(c => {
                        if (c.id === char.id) {
                            return { ...c, live: { ...c.live, pushed: true, usedMove: isCritFumble ? true : c.live.usedMove, usedLoad: isCritFumble ? true : c.live.usedLoad, usedFocus: isCritFumble ? true : c.live.usedFocus, usedGrit: isCritFumble ? true : c.live.usedGrit } };
                        }
                        return c;
                    }));
                    addLog(msg);
                }"""

text = text.replace(old_handle_push, new_handle_push)
with open('index.html', 'w') as f:
    f.write(text)
