import re

with open('index.html', 'r') as f:
    content = f.read()

# I also need to make sure applyNewMission and applyNewCrew reset it, which I added. Let's verify.
