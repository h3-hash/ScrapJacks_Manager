import re

with open("index.html", "r") as f:
    content = f.read()

roll_site = """            const rollSiteCondition = (manualRollStr) => {
                const roll = getRoll(manualRollStr, 1, 10);
                const condition = SITE_CONDITION_TABLE[roll];

                setSiteConditions(prev => ({...prev, [missionLevel]: roll}));
                setSiteFlags(prev => ({...prev, [missionLevel]: { hostileSpawned: false, poiResolved: false }}));

                addLog(`Site Condition (Level ${missionLevel}) [${manualRollStr ? 'Manual Roll' : 'Roll'}: ${roll}]: ${condition}`);
            };"""
content = re.sub(
    r"const rollSiteCondition = \(manualRollStr\) => \{.*?\n\s*\};",
    roll_site,
    content,
    flags=re.DOTALL
)

with open("index.html", "w") as f:
    f.write(content)
