import re

with open('index.html', 'r') as f:
    content = f.read()

# Make shipUpgrades NOT clear when changing ship.
content = content.replace("setShipUpgrades([]); ", "// setShipUpgrades([]); // User request: Upgrades persist")
content = content.replace("setShipUpgrades([]);", "// setShipUpgrades([]); // User request: Upgrades persist")

# Also, applyShipChange currently does: suit: 'Default' for all crew. Let's fix that.
# Find the setCrew map inside applyShipChange
old_set_crew = """                setCrew(prev => {
                    let updatedCrew = [...prev];

                    // Add standard loadouts to new hires if crew expands
                    if (updatedCrew.length < newConfig.crewCount) {
                        for (let i = updatedCrew.length; i < newConfig.crewCount; i++) {
                            updatedCrew.push({
                                id: generateId(),
                                name: `Scrapjack ${i + 1}`,
                                role: 'Wrench',
                                suit: 'Default',
                                loadOut: {
                                    melee: 'Wrecking Bar',
                                    ranged: 'None',
                                    mods: [],
                                    uItems: []
                                },
                                stats: { load: 'd6', focus: 'd6', grit: 'd6' },
                                status: { load: true, focus: true, grit: true, move: true },
                                wounds: 0,
                                active: true,
                                tempBuffs: [],
                                inReserve: false
                            });
                        }
                    } else if (updatedCrew.length > newConfig.crewCount) {
                        // Trim crew if downsizing
                        updatedCrew = updatedCrew.slice(0, newConfig.crewCount);
                    }

                    // For all kept crew, we should keep their suits. Currently this block doesn't reset suits, it only adds new ones! Wait, let me check.
                    return updatedCrew;
                });"""

# Let's inspect applyShipChange properly.
