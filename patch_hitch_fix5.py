import re

with open("index.html", "r") as f:
    content = f.read()

# Let's see what advancePhase does:
# if (nextPhase === 'Hitch') {
#   rollHitch(manualRolls.hitch); // Wait, this uses manualRolls.hitch from state.
# But I fill the input "Hitch Roll" AFTER I advance to Sweep. So manualRolls.hitch is set.
# But why does the log say "[Turn 1 - Breach] Phase advanced to: Sweep..." and nothing else?
# Is the click to "Advance to Hitch" not doing anything?
# Wait, advancePhase is called on the click. Does it crash?
# Let's check error messages.
