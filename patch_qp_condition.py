import re

with open("index.html", "r") as f:
    content = f.read()

# Implement Quiet Pull Condition 8
qp_logic = """                if (success) {
                    let rewardText = activeQuietPull.reward;
                    const siteCondition = siteConditions[missionLevel];

                    if (siteCondition === 8) {
                        const extraSalvage = rollDice(1, 4);
                        setSalvage(s => s + extraSalvage);
                        setTraces(t => t + 1);
                        rewardText += ` [Tracked Inventory: +${extraSalvage} Salvage, +1 Trace (Active)]`;
                    }

                    addLog(`Quiet Pull SUCCESS by ${actorStr}: ${activeQuietPull.name}. Reward: ${rewardText}`);
"""

content = re.sub(
    r"if \(success\) \{\n\s*addLog\(`Quiet Pull SUCCESS by \$\{actorStr\}: \$\{activeQuietPull.name\}. Reward: \$\{activeQuietPull.reward\}`\);",
    qp_logic,
    content
)

with open("index.html", "w") as f:
    f.write(content)
