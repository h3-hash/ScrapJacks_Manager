import re

with open('index.html', 'r') as f:
    lines = f.readlines()

for i in range(2880, 2920):
    print(f"{i+1}: {lines[i].rstrip()}")
