import sys


if len(sys.argv) != 3 or sys.argv[1] == '-help':
    print('usage: python grepword.py word filename')
    sys.exit()

word = sys.argv[1]
file = sys.argv[2]

with open(file, encoding = 'utf-8') as f:
    for lino, line in enumerate(f, start = 1):
        if word in line :
            print('{:4}: {}'.format(lino, line.rstrip()))

