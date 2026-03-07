import re
with open('index.html', 'r') as f:
    text = f.read()

# I see it's completely blank in test1.png! Did I break the syntax in index.html?
# Let's check for compilation errors.
