import re

with open('index.html', 'r') as f:
    lines = f.readlines()

for i in range(2885, 2900):
    print(f"{i+1}: {lines[i].rstrip()}")
