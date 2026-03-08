import re

with open("index.html", "r") as f:
    content = f.read()

# Fix the condition 2 logic because `hostileSpawned` gets set to true before condition 2 check
intercept_hostile = """
                if (spawnedEnemy) {
                    const flags = siteFlags[missionLevel] || {};
                    const isFirstSpawn = !flags.hostileSpawned;

                    if (isFirstSpawn) {
                        setSiteFlags(prev => ({
                            ...prev,
                            [missionLevel]: { ...prev[missionLevel], hostileSpawned: true }
                        }));

                        if (siteCondition === 10) {
                            spawnedEnemy = (missionLevel === 3) ? 'Pirates' : 'Raiders';
                            text += ` [Rival Claim Site Condition: Hostile converted to ${spawnedEnemy}]`;
                        }
                    }

                    if (pCheck && isPrimeChecked && Math.floor(getSecureRandom() * 6) + 1 >= 5 && missionLevel >= 2) {
                        if (!spawnedEnemy.includes('Apex')) spawnedEnemy = `Prime (${spawnedEnemy})`;
                        text += ` [Prime Condition Met - Upgraded to ${spawnedEnemy}]`;
                    }

                    let deployStr = getDeployment();

                    if (isFirstSpawn && siteCondition === 2) {
                         text += ` [Active Defense Protocol: +1 model per spawn point. (Manually adjust quantity)]`;
                    }

                    text += ` Deployment: ${deployStr}`;
                }

                return text;
            };"""

content = re.sub(
    r"if \(spawnedEnemy\) \{.*?return text;\n\s*\};",
    intercept_hostile,
    content,
    flags=re.DOTALL
)

with open("index.html", "w") as f:
    f.write(content)
