import re

with open("index.html", "r") as f:
    content = f.read()

pattern = r"const rollSiteCondition = \(manualRollStr\) => \{.*?\n\s*\};"
new_roll_site = """const rollSiteCondition = (manualRollStr) => {
                const roll = getRoll(manualRollStr, 1, 10);
                const condition = SITE_CONDITION_TABLE[roll];
                addLog(`Site Condition (Level ${missionLevel}) [${manualRollStr ? 'Manual Roll' : 'Roll'}: ${roll}]: ${condition}`);
            };"""

content = re.sub(pattern, new_roll_site, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)
