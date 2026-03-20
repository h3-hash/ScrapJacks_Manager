import re

with open("index.html", "r") as f:
    content = f.read()

# Implement POI conditions (3, 5, 7)
poi_logic = """                    // Site Conditions POI Intercepts
                    const siteCondition = siteConditions[missionLevel];
                    const flags = siteFlags[missionLevel] || {};
                    const isFirstPOI = !flags.poiResolved;

                    if (isFirstPOI) {
                        setSiteFlags(prev => ({
                            ...prev,
                            [missionLevel]: { ...prev[missionLevel], poiResolved: true }
                        }));

                        if (siteCondition === 3 && missionLevel === 1) {
                            gear.push('Power Cell', 'Patch-Kit');
                            special += " [Abandoned Tool Cache: +1 Power Cell, +1 Patch Kit]";
                        }
                        if (siteCondition === 7 && missionLevel === 3) {
                            gear.push('Med-Kit', 'Patch-Kit');
                            special += " [Emergency Medical Supply: +1 Med-Kit, +1 Patch-Kit]";
                        }
                    }

                    if (siteCondition === 5 && missionLevel === 2) {
                        const extraSalvage = rollDice(1, 4);
                        sAdd += extraSalvage;
                        special += ` [Forgotten Salvage Surplus: +${extraSalvage} Salvage]`;
                    }

                    if (sAdd > 0) setSalvage(prev => prev + sAdd);"""

content = re.sub(
    r"if \(sAdd > 0\) setSalvage\(prev => prev \+ sAdd\);",
    poi_logic,
    content
)

with open("index.html", "w") as f:
    f.write(content)
