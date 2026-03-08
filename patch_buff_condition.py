import re

with open("index.html", "r") as f:
    content = f.read()

# Add buff notes for Condition 1 and 9 when rolled
roll_site = """            const rollSiteCondition = (manualRollStr) => {
                const roll = getRoll(manualRollStr, 1, 10);
                const condition = SITE_CONDITION_TABLE[roll];

                setSiteConditions(prev => ({...prev, [missionLevel]: roll}));
                setSiteFlags(prev => ({...prev, [missionLevel]: { hostileSpawned: false, poiResolved: false }}));

                addLog(`Site Condition (Level ${missionLevel}) [${manualRollStr ? 'Manual Roll' : 'Roll'}: ${roll}]: ${condition}`);

                if (roll === 1) {
                    setCrewBuffs(prev => [...prev, { id: generateId(), text: 'Residual Power Grid: Ignore the AC cost to open one MHU this level.' }]);
                } else if (roll === 9) {
                    setCrewBuffs(prev => [...prev, { id: generateId(), text: 'Functional Air Recycler: Ignore the first Suit Breach AC loss in one MHU.' }]);
                }
            };"""

content = re.sub(
    r"const rollSiteCondition = \(manualRollStr\) => \{.*?\n\s*\};",
    roll_site,
    content,
    flags=re.DOTALL
)

with open("index.html", "w") as f:
    f.write(content)
