import re

with open('index.html', 'r') as f:
    text = f.read()

# I also need to make sure the specific manual rolls from `charRollInputs[charId]` carry over if they entered it before clicking "Roll",
# but neither `setCombatPrompt` nor `handlePush` take a manual roll argument directly from the function call, they read from state or have their own inputs.
# Wait, `handlePush` does read `charRollInputs[charId]`. `setCombatPrompt` shows a new modal with its own inputs. That's fine.
