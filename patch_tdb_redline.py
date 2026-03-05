import re

with open('index.html', 'r') as f:
    text = f.read()

# Make sure actionRollPrompt triggers properly over everything except modalConfig
# Wait, redlinePrompt is not a generic modal using setModalConfig, it has its own UI.
# And actionRollPrompt also has its own UI.
# Is actionRollPrompt placed correctly?
# Yes, it looks like:
# {actionRollPrompt && (() => { ... })()}
# It renders unconditionally if `actionRollPrompt` is truthy.
# Let's fix redline prompt to use TDB if it's a Grit roll and the character gets TDB for it.
# Wait, "Resist Stress & Terror" is listed as getting TDB for Riggers. "Redlined" is listed as a separate section, but uses Grit. Does it count as Resist Stress?
# The rulebook text says:
# "Resist Stress & Terror (Individual Roll) A Scrapjack rolls Grit individually when: • Confronted by Terror • Becoming Redlined"
# Ah! Redline IS a Resist Stress roll!
# So Riggers should get TDB on Redline Grit rolls.

# Let's patch Redline Grit roll to use TDB if applicable.
old_roll_logic = """const sides = parseInt(char.vitals.grit.substring(1));
                                                const roll = getRoll(redlinePrompt.manualRoll, 1, sides);
                                                if (roll >= 4) {"""

new_roll_logic = """const sides = parseInt(char.vitals.grit.substring(1));
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
                                                        setAircharge(prev => Math.max(0, prev - 1));
                                                    } else {
                                                        msg += " -1 Aircharge.";
                                                        setAircharge(prev => Math.max(0, prev - 1));
                                                    }
                                                    addLog(msg);
                                                    updateCharacter(char.id, 'status', 'Dead');
                                                    setRedlinePrompt(null);
                                                }"""
# Wait, let's just make it simpler by injecting it properly
text = text.replace(old_roll_logic, new_roll_logic)

# Also, when the rule says "Failure: -1 Aircharge from the Crew Pool and Permanent death", I should make sure my existing code was already deducting 1 Aircharge, or add it. I added it in the patch.
with open('index.html', 'w') as f:
    f.write(text)
