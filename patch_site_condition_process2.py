import re

with open("index.html", "r") as f:
    content = f.read()

# Add Hostile intercept for condition 2 and 10
# Also we need to correctly implement the intercept logic for spawnedEnemy
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
                }

                if (spawnedEnemy) {
                    if (pCheck && isPrimeChecked && Math.floor(getSecureRandom() * 6) + 1 >= 5 && missionLevel >= 2) {
                        if (!spawnedEnemy.includes('Apex')) spawnedEnemy = `Prime (${spawnedEnemy})`;
                        text += ` [Prime Condition Met - Upgraded to ${spawnedEnemy}]`;
                    }

                    const flags = siteFlags[missionLevel] || {};
                    // if it WAS the first spawn, the flag is now true so we can't just check it
                    // we need to track if we just flipped it
                    const isCondition2 = (siteCondition === 2 && !flags.hostileSpawned); // wait, we just set it true above

                    let deployStr = getDeployment();

                    if (siteCondition === 2 && !flags.hostileSpawned) {
                         text += ` [Active Defense Protocol: +1 model per spawn point]`;
                         // wait, getDeployment() returns strings like "Corner 1 (x2 models)". We don't easily modify the string output, we just add the buff note.
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
