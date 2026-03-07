import re
with open('index.html', 'r') as f:
    text = f.read()

# Make sure combat logic is not replacing the actual 'return' if they miss but don't critical fumble.
# Wait, my code does:
# if (isCritFumble) { return; } else { updateLiveState(...) }
# if (finalAtk < 4) { addLog(...) return; }
# This is correct.

# Wait, `isYarddog` is set to `true` if `isAssisted && !isYarddog`.
# So non-Yarddogs get TDB if assisted. Do they get critical successes/fumbles if they are assisted?
# The rulebook states: "Critical Rolls - a Crit-Success or a Crit-Fumble – can only occur for Scrapjacks when rolling a Two Dice Bonus action."
# "If the player succeeds and rolls doubles (5,5) when attempting a Role related action..."
# Okay, "Role related action" implies only natural TDB, not assisted TDB!
# Let me look at my condition:
# let isCritSuccess = (!assistedNonYarddog && isYarddog && manualAtk === null && roll1 === roll2 && baseAtk >= 4);
# This exactly excludes `assistedNonYarddog`. So non-Yarddogs don't get crits from Assist. That's perfect.
