import re

with open('index.html', 'r') as f:
    content = f.read()

# Make shipUpgrades NOT clear when changing ship.
content = content.replace("setShipUpgrades([]);", "// setShipUpgrades([]); // User request: Upgrades persist")
content = content.replace("setShipUpgrades([]); ", "// setShipUpgrades([]); // User request: Upgrades persist")

# The user said: "When you upgrade your ship, you keep all your current Eva suits".
# The issue might be that applyShipChange resets the crew's suits to Default.
# Let's see what applyShipChange does.
