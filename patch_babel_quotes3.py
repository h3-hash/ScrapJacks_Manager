import re

with open("index.html", "r") as f:
    content = f.read()

content = content.replace("'Spacer\\'s Shake':", '"Spacer\'s Shake":')
content = content.replace("'She\\'s Breaking Up':", '"She\'s Breaking Up":')
content = content.replace('"Spacer\\\\\'s Shake":', '"Spacer\'s Shake":')
content = content.replace('"She\\\\\'s Breaking Up":', '"She\'s Breaking Up":')
content = content.replace("'Spacer's Shake':", '"Spacer\'s Shake":')
content = content.replace("'She's Breaking Up':", '"She\'s Breaking Up":')

with open("index.html", "w") as f:
    f.write(content)
