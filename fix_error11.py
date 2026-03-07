import re

with open('index.html', 'r') as f:
    text = f.read()

# Make sure Critical Rolls text correctly handles 1s for crits?
# "Crit-Success - If the player succeeds and rolls doubles (5,5 - 6,6 - 7,7...) when attempting a Role related action"
# "Crit-Fumble - On a failed double result, something goes catastrophically wrong."

# My implementation:
# if (isTdb && roll2 !== null && roll1 === roll2) {
#   if (success) { isCritSuccess = true; ... }
#   else { isCritFumble = true; ... }
# }

# This exactly matches the rules.

# The user also asked: "also, make sure when a relevant skill is required to be rolled, only the die associated with that vital is able to be rolled"
# Yes, by clicking the specific die's "Roll" button, you only see the actions associated with that die (e.g. Load -> Break/Brace, Melee, etc).

# What about Resist and Resist Stress?
# They both use Grit.
# The user's prompt specifically mentions "Resist Stress & Terror" and "Redlined" and "Push".
# When redlined: success(4+), failure (-1 Aircharge, Permanent death). This logic is already in `redlinePrompt` logic.

# Let's verify `redlinePrompt` doesn't conflict with TDB.
