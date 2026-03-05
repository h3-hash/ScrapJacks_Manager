import re

with open('index.html', 'r') as f:
    text = f.read()

# Let's fix ROLES tdb string matching correctly
# Yarddog (Melee) tdb: 'Melee Combat, Push'
# Yarddog (Ranged) tdb: 'Ranged Combat, Push'
# And my action names: 'Melee Combat', 'Ranged Combat', 'Push'.
# So `roleTdbText.includes(name)` should literally match them perfectly!
# "Melee Combat" is in "Melee Combat, Push".
# "Ranged Combat" is in "Ranged Combat, Push".
# "Push" is in "Melee Combat, Push".
# Let's check the code:
# const ROLES = {
#    'Yarddog (Melee)': { tdb: 'Melee Combat, Push', ... },
#    'Yarddog (Ranged)': { tdb: 'Ranged Combat, Push', ... }
# }
# Ah, wait! The review said "Because the Yarddog's role defines their TDB as 'Combat (Melee/Ranged)'".
# Did it? Let's check `ROLES` in `index.html`.
