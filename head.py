import sys


file = open(sys.argv[2], mode = 'r', encoding = 'utf-8').readlines()
count = int(sys.argv[1])

if count > len(file):
    count = len(file)

for i in range(count):
    print(file[i])
