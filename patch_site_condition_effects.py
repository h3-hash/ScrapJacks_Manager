import re

with open("index.html", "r") as f:
    content = f.read()

# 2. Active Defense Protocol & 10. Rival Claim
# Intercept hitch hostile spawn
pattern_hitch = r"const processHitchEvent = \(level, roll\) => \{(.*?)\};\n"

def process_hitch_repl(match):
    body = match.group(1)

    # We need to find the part where hostiles are spawned
    # In the original processHitchEvent, it usually returns a string with the enemy.
    # It might call `spawnEnemy(name, count)`. Actually, looking at the code `processHitchEvent` just returns text and doesn't spawn!
    # Wait, does processHitchEvent spawn enemies? Let's check processHitchEvent content.
    return match.group(0)

content = re.sub(pattern_hitch, process_hitch_repl, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)
