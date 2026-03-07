import re

with open('index.html', 'r') as f:
    text = f.read()

# Fix Upgrades Reseting. Wait, I already did this with python patch_ship_change2.py? Oh, wait, I just generated the file, I didn't run the replacement properly.
text = text.replace("setShipUpgrades([]); ", "// setShipUpgrades([]); // User request: Upgrades persist")
text = text.replace("addCampaignLog(`Acquired ${newShip}. Ship upgrades reset.`);", "addCampaignLog(`Acquired ${newShip}. Ship upgrades persist.`);")

# The user states: "When you upgrade your ship, you keep all your current Eva suits".
# Looking at the code: applyShipChange DOES NOT override existing suits!
# wait, it says:
# if (updatedCrew.length > newConfig.crewCount) { updatedCrew = updatedCrew.slice(0, newConfig.crewCount); }
# while (updatedCrew.length < newConfig.crewCount) { updatedCrew.push({ ... suit: newConfig.suits[i] || 'Workskin' ... }) }
# It only assigns suits to new crew members if the crew expands.
# BUT wait! Does newShip have a "suits" array that usually overrides the existing crew?
# Let's check generateInitialCrew or if players ever expect the newShip's suits to override.
# Actually, the user says "you keep all your current Eva suits". This is what the code ALREADY does for existing crew! Wait, let me double check the help text or rulebook.
# The user said: "When you upgrade your ship, you keep all your current Eva suits" - this could be a statement of fact they want to make sure of, OR it might be because the older game code *did* reset them or they thought it did. Or maybe they noticed that when ACR debt hits 0 and they get a new ship, they get the new ship's suits for *new* characters, which is fine, but they wanted to make sure their old characters don't lose their suits. The current code preserves the `.suit` attribute for any crew that are kept (via `slice`).

with open('index.html', 'w') as f:
    f.write(text)
