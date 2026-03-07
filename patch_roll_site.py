import re

with open("index.html", "r") as f:
    content = f.read()

new_roll_site = """            const rollSiteCondition = (manualRollStr) => {
                const roll = getRoll(manualRollStr, 1, 10);
                const condition = SITE_CONDITION_TABLE[roll];
                addLog(`Site Condition (Level ${missionLevel}) [${manualRollStr ? 'Manual Roll' : 'Roll'}: ${roll}]: ${condition}`);
            };"""

content = re.sub(
    r"const rollSiteCondition = \(manualRollStr\) => \{[^\}]+\};",
    new_roll_site,
    content,
    flags=re.MULTILINE
)

with open("index.html", "w") as f:
    f.write(content)
