import re

with open('index.html', 'r') as f:
    text = f.read()

# Let's search around actionRollPrompt to make sure it's validly placed in the JSX tree.
# It should be placed at the root level of the main return statement, after {modalConfig && <Modal ... />}
# Let's find exactly where I placed it.
start = text.find("{actionRollPrompt")
print(text[start-100:start+200])
