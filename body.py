import sys

start = int(sys.argv[1])
end = int(sys.argv[2])
file = open(sys.argv[3], encoding = 'utf-8').readlines()


if start < 0 :
    start = 0

if end > len(file):
    end = len(file)

for i in range(start, end):
    print(file[i])
    
