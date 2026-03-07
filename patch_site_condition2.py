import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the advancePhase condition for rollSiteCondition:
# Instead of `if (turn === 1) rollSiteCondition(manualRolls.site);`
# Wait, if they enter a new level, the rule says "before breaching the first time and when moving lower levels".
# In Scrapjacks, you roll Site Condition "before breaching the first time and when moving lower levels".
# If they change the mission level dropdown, they are moving lower levels.
# We can track previous mission level, or just roll it when the dropdown is changed.
# Actually, the user can manually change the level. If they do it, maybe they want to roll site condition right away? Or they wait for Breach phase?
# "before breaching the first time and when moving lower levels" - actually the Breach phase is when you roll for the MHU entry.
# So if they change `missionLevel`, and then click "Advance Phase" (which does the breach), they should roll it.
# How to track if it's the first breach of a level?

# Let's create a state `levelBreached: [false, false, false, false]`
# No, simpler: `siteConditionRolledForLevel: {1: false, 2: false, 3: false}`
# We can just add this to the app state.
