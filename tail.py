import sys

file = sys.argv[2]
count = int(sys.argv[1])

with open(file, encoding = 'utf-8') as f:
    lines = f.readlines()

    if count > len(lines):
        count = len(lines)

    for i in range(len(lines) - count, len(lines)) :
        print(lines[i].rstrip())
        
