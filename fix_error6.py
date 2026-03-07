import re

with open('index.html', 'r') as f:
    text = f.read()

# Let's see what {actionRollPrompt && is blocked by.
# If there are modals like `modalConfig` or `redlinePrompt` that share `{... && (() => { ... })()}` they must return correctly.
# Oh, the problem is that it is blocked by ANOTHER condition!
print(text.find("!modalConfig && !combatPrompt && !hostileAttackPrompt && !disableHostilePrompt && !objectivePrompt && !tableRollPrompt && !redlinePrompt && !pendingPenaltyPrompt && !shipChangePrompt && !grenadePrompt"))
