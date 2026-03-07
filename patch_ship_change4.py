import re

with open('index.html', 'r') as f:
    text = f.read()

text = text.replace("setShipUpgrades([]);", "// setShipUpgrades([]);")
text = text.replace("Acquired ${newShip}. Ship upgrades reset.", "Acquired ${newShip}. Ship upgrades persist.")
text = text.replace("This will reset your Ship Upgrades.", "Your Ship Upgrades will persist.")

# Also update the rules text
text = text.replace("Upgrades and the Crew Locker persist.", "Upgrades, the Crew Locker, and existing EVA Suits persist.")

with open('index.html', 'w') as f:
    f.write(text)
