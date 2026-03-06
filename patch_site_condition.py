import re

with open('index.html', 'r') as f:
    content = f.read()

# We need to change the onChange handler for missionLevel to also trigger a Site Condition roll
# when moving to a new level (or moving to a lower level, meaning higher number).

# Actually, the user can change it anytime. We can handle it in a useEffect, or directly in the onChange.
# Let's see if we should just replace `onChange={e => setMissionLevel(parseInt(e.target.value))}`
# Or we can track `missionLevel` change and if it's during a Breach Phase, we don't automatically roll.
# Wait, rules say "before breaching the first time and when moving lower levels as indicated by the rules".
# "Moving lower levels" = level 2 or 3.
# So if they change missionLevel, it should roll Site Condition.

# Let's check how `advancePhase` works.
# Currently: `if (turn === 1) rollSiteCondition(manualRolls.site);`
# But turn isn't necessarily 1 when changing levels! They might just keep `turn` going, or reset turn?
# Actually, the game doesn't reset turns when changing levels in the UI.
