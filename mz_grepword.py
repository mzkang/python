import sys


word = str(sys.argv[1])
file = sys.argv[2]

lines = open(file, mode = 'r', encoding = 'utf-8').readlines()

for i in range(len(lines)) :
    if word in lines[i] :
        print('{:2}: {}'.format(i+1, lines[i]), end = '')

