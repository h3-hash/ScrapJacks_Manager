import re

with open('index.html', 'r') as f:
    content = f.read()

# Wait, applying ship change only truncates or expands the crew array.
# Let's see what applyShipChange does to updatedCrew exactly.
