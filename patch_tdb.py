import re
with open('index.html', 'r') as f:
    text = f.read()

# I want to add an Action Modal for generic rolls.
# Wait, handleStandardRoll is just called right from the Roll button next to the dice.
# But there's also the ANY DIE TYPE ACTIONS, LOAD DIE TYPE ACTIONS, etc.
# Instead of a simple "Roll" button, maybe the "Roll" button opens an `actionRollPrompt` modal?
# Let's create an Action Selection modal.

# First, define the actions and their required dice types.
ACTION_TYPES = """
        const ACTION_TYPES = {
            'Aim': { type: 'Any', desc: '+2 to next Combat action, -2 to enemy DD.' },
            'Assist': { type: 'Any', desc: 'Grants ally TDB or +2 to their next action.' },
            'Interact/Use': { type: 'Any', desc: 'Use items, open doors, minor interactions.' },
            'Move': { type: 'Load', desc: 'Additional movement after Free Move.' },
            'Melee Combat': { type: 'Load', desc: 'Close-quarters fighting.' },
            'Break/Brace': { type: 'Load', desc: 'Forceful dismantling or stabilizing.' },
            'Ranged Combat': { type: 'Focus', desc: 'Attacking with firearms.' },
            'Repair/Heal': { type: 'Focus', desc: 'Treat injuries, patch suits.' },
            'Scan/Hack': { type: 'Focus', desc: 'Technical interaction with systems.' },
            'Resist': { type: 'Grit', desc: 'Reaction. Die spent only on failure.' },
            'Resist Stress': { type: 'Grit', desc: 'Save vs Terror or Redlined.' },
            'Push': { type: 'Grit', desc: 'Costs 1 Aircharge. Success = refresh dice & move.' }
        };
"""

# Let's insert ACTION_TYPES into index.html
text = text.replace("const WEAPONS_MELEE", ACTION_TYPES + "\n        const WEAPONS_MELEE")

with open('index.html', 'w') as f:
    f.write(text)
