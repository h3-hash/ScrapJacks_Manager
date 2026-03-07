import re

with open('index.html', 'r') as f:
    lines = f.readlines()

# I see the problem!
# lines 2942 to 2948 are extra garbage left over from my search-and-replace!
# Let's delete them.

del lines[2941:2948]

with open('index.html', 'w') as f:
    f.writelines(lines)
