import sys


count = int(sys.argv[1])
file = sys.argv[2]

with open(file, encoding = 'utf-8') as f:
    lines = f.readlines()

    if count > len(lines):
        count = len(lines)

    for i in range(count):
        print(lines[i].rstrip())
