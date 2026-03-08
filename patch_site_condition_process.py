import re

with open("index.html", "r") as f:
    content = f.read()

# Replace processHitchEvent definition to intercept conditions
new_process = """            const processHitchEvent = (lvl, rollVal, isPrimeChecked = true) => {
                let text = "";
                let spawnedEnemy = null;
                let pCheck = false;

                const siteCondition = siteConditions[missionLevel];

                // 6. Unstable Section: All Hazard results from Hitch rolls in MHU 3 are replaced by Hull Shift.
                if (siteCondition === 6 && missionLevel === 3) {
                    const isHazard = (lvl === 3 && [1, 2, 3, 8].includes(rollVal));
                    if (isHazard) {
                        text = "Unstable Section (Site Condition) converts Hazard to Hull Shift! All Scrapjacks roll DD. Fail: suffer 1 Wound.";
                        addHazard('Hull Shift');
                        return text;
                    }
                }

                if (lvl === 1) {
                    if (rollVal === 1) { text = "All Clear. No Hazards or Hostiles this turn."; }
                    else if (rollVal === 2) { text = "Arcs and Sparks. Electrical discharge. Scrapjacks risk Stun when entering or moving this turn."; addHazard('Arcs and Sparks'); }
                    else if (rollVal === 3) { text = "Power Loss. MHU goes dark. Darkness penalties apply until end of Hitch Phase."; addHazard('Power Loss'); }
                    else if (rollVal === 4) { text = "Ghosts in the Alloy. All Scrapjacks roll Grit –1. Fail: lose Grit die next activation."; addHazard('Ghosts in the Alloy'); }
                    else if (rollVal === 5) { text = "Toxic Fumes. One tile affected. LOS reduced. Resolve as standard Toxic Fumes Hazard."; addHazard('Toxic Fumes'); }
                    else if (rollVal === 6) { text = "Void Rats (Ghost Step). Spawn normally."; spawnedEnemy = 'Void Rats'; pCheck = true; }
                    else if (rollVal === 7) { text = "Small Maintenance Droids (Fast-Mover). Spawn normally."; spawnedEnemy = 'Small Maintenance Droids'; pCheck = true; }
                    else if (rollVal === 8) { text = "Infested Crew (Frenzied). Spawn normally."; spawnedEnemy = 'Infested Crew'; pCheck = true; }
                    else if (rollVal === 9) { text = "Hull Shift. All Scrapjacks roll DD. Fail: suffer 1 Wound."; addHazard('Hull Shift'); }
                    else if (rollVal === 10) { text = "Pressure Building. No immediate effect. Next Hitch roll uses Level II table."; }
                } else if (lvl === 2) {
                    if (rollVal === 1) {
                        const subRoll = Math.floor(getSecureRandom() * 6) + 1;
                        if (subRoll <= 3) { text = "Uneasy Silence -> Raiders spawn (Cull Protocol)."; spawnedEnemy = 'Raiders'; pCheck = true; }
                        else { text = "Uneasy Silence -> All Clear."; }
                    }
                    else if (rollVal === 2) { text = "Arcs and Sparks. Electrical discharge. Risk Stun this turn."; addHazard('Arcs and Sparks'); }
                    else if (rollVal === 3) { text = "Radiation Spike. All Scrapjacks roll Focus –1. Fail: lose Focus die next activation."; addHazard('Radiation Spike'); }
                    else if (rollVal === 4) { text = "Hull Breach. Roll D4 for quadrant. Damage at center (or nearest). Scrapjacks roll Load –1 or move 3″ toward breach."; addHazard('Hull Breach'); }
                    else if (rollVal === 5) { text = "Pirates (Low-Profile). Spawn normally."; spawnedEnemy = 'Pirates'; pCheck = true; }
                    else if (rollVal === 6) { text = "Small Security Droids (Double-Tap). Spawn and activate immediately."; spawnedEnemy = 'Small Security Droids'; pCheck = true; }
                    else if (rollVal === 7) { text = "Nanite Swarm (System Shock). Spawn normally."; spawnedEnemy = 'Nanite Swarm'; pCheck = true; }
                    else if (rollVal === 8) { text = "Large Maintenance Droid (Heavy Hit). Spawn normally."; spawnedEnemy = 'Large Maintenance Droids'; pCheck = true; }
                    else if (rollVal === 9) { text = "Small Xeno Types (First Contact). Spawn normally."; spawnedEnemy = 'Small Xeno Types'; pCheck = true; }
                    else if (rollVal === 10) { text = "Toxic Fumes. LOS reduced to 6″. Scrapjacks roll Resist (Grit) or lose 1 Aircharge."; addHazard('Toxic Fumes'); }
                } else if (lvl === 3) {
                    if (rollVal === 1) { text = "She's Breaking Up. Resolve Hull Shift and Arcs and Sparks simultaneously."; addHazard('Hull Shift'); addHazard('Arcs and Sparks'); }
                    else if (rollVal === 2) { text = "Double Hull Breach. Two quadrants lose pressure. Resolve as two Hull Breach effects."; addHazard('Hull Breach'); addHazard('Double Hull Breach'); }
                    else if (rollVal === 3) { text = "Total Power Loss. MHU goes dark until end of the next activation."; addHazard('Total Power Loss'); }
                    else if (rollVal === 4) { text = "Large Security Droids (Plated, Double-Tap). Spawn normally."; spawnedEnemy = 'Large Security Droids'; pCheck = true; }
                    else if (rollVal === 5) { text = "VRG Compliance Team (Low-Profile, Pinning Fire). Spawn normally."; spawnedEnemy = 'VRG Compliance Team'; pCheck = true; }
                    else if (rollVal === 6) { text = "Bio-Asset (Frenzied, Cull Protocol). Spawn normally."; spawnedEnemy = 'Bio-Asset'; pCheck = true; }
                    else if (rollVal === 7) { text = "C-FRAME Combat Units (Redundant Core, Self-Sealing). Spawn and activate immediately."; spawnedEnemy = 'C-FRAME Combat Units'; pCheck = true; }
                    else if (rollVal === 8) { text = "Radiation Spike + Toxic Fumes. Both Hazards apply simultaneously in the MHU."; addHazard('Radiation Spike'); addHazard('Toxic Fumes'); }
                    else if (rollVal === 9) { text = "Large Xeno Types (Reach, Frenzied). Spawn normally."; spawnedEnemy = 'Large Xeno Types'; pCheck = true; }"""
content = re.sub(
    r"const processHitchEvent = \(lvl, rollVal, isPrimeChecked = true\) => \{.*?(?=else if \(rollVal === 10 && lvl === 3\))",
    new_process + "\n                    ",
    content,
    flags=re.DOTALL
)

with open("index.html", "w") as f:
    f.write(content)
