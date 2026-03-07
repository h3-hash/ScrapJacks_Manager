import re

with open('index.html', 'r') as f:
    text = f.read()

# Let's fix the layout of the Action Selection modal so it doesn't get cut off at the bottom and is scrollable properly.
# The UI has `max-h-64`, maybe change to `max-h-80`
text = text.replace("max-h-64 overflow-y-auto mb-4 pr-1", "max-h-96 overflow-y-auto mb-4 pr-1")
text = text.replace("flex flex-col gap-2 max-h-96 overflow-y-auto", "flex flex-col gap-2 max-h-[60vh] overflow-y-auto")

# Wait, `Break/Brace` isn't fully visible because there are 6 options? Oh no, wait, there are actually only 6 items listed in the screenshot!
# Oh, that's because we only show actions that are 'Any' or match the 'Load' vital!
# Ah, I see: Aim (Any), Assist (Any), Interact/Use (Any), Move (Load), Melee Combat (Load), Break/Brace (Load). This is perfectly correct!
# It's scrollable, but my script just clicked it.

with open('index.html', 'w') as f:
    f.write(text)
