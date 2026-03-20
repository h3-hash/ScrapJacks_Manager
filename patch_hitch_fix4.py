import re

with open("index.html", "r") as f:
    content = f.read()

# I need to properly restore `spawnSpecificEnemy` inside the `if (spawnedEnemy) { ... }` block
# The exact replacement string should be:
original_logic_fixed = """if (spawnedEnemy) {
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

                    const deployText = getDeploymentText();

                    let extraModels = 0;
                    if (isFirstSpawn && siteCondition === 2) {
                        text += ` [Active Defense Protocol: +1 model per spawn point (applied to total quantity)]`;
                        extraModels = deployText.includes(',') ? 2 : 1;
                    }

                    if (isPrimeChecked && pCheck) {
                        const primeRoll = Math.floor(getSecureRandom() * 6) + 1;
                        if (primeRoll <= 3 || nextMhuHitchPrime) {
                            text += ` -> [Prime Check: ${primeRoll}] [PRIME SPAWNS!] [Deploy: ${deployText}]`;
                            let primeType = `Prime (${spawnedEnemy})`;
                            if (!HOSTILES_DATA[primeType]) primeType = spawnedEnemy;
                            spawnSpecificEnemy(primeType, 1, deployText);
                            spawnSpecificEnemy(spawnedEnemy, 3 + extraModels, deployText);
                            if(nextMhuHitchPrime) setNextMhuHitchPrime(false);
                        } else {
                            text += ` -> [Prime Check: ${primeRoll}] Normal. [Deploy: ${deployText}]`;
                            spawnSpecificEnemy(spawnedEnemy, 4 + extraModels, deployText);
                        }
                    } else {
                         text += ` [Deploy: ${deployText}]`;
                         spawnSpecificEnemy(spawnedEnemy, 4 + extraModels, deployText);
                    }
                }

                return text;"""

content = re.sub(
    r"if \(spawnedEnemy\) \{.*?return text;",
    original_logic_fixed,
    content,
    flags=re.DOTALL
)

with open("index.html", "w") as f:
    f.write(content)
