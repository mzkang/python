
#lab 6-1
from collections import Counter

L = [1,1,7,7,7,4,4,4,2,1,5,5,9,11,3,'a','x',9,8,'b','b','z','b']
counts = Counter(L)

for key in counts.keys():
 #(==)------------------
 #for key in counts : 해도 키만 꺼내는 것이 됨 
    if counts[key] >= 3:
        print(key)




#lab 6-2
import math
y = math.exp(math.pi) + 10
print(y)




#lab 6-3
from itertools import product

first = ['A','E','I','O','U']
second = ['A','B','C','D','E','a','b','c','d','e']
third = [2,3]
forth = [1,3,5]

combinations = list(product(first,second,third,forth))
len(combinations)



#lab 6-4
def superviesd_learning():
    return '지도학습은 정답을 아는 학습 데이터로부터 하나의 함수를 추론하는 기계학습의 한 방법'

def unsuperviesed_learning():
    return '비지도학습은 정답을 모르는 데이터로부터 숨겨진 관계를 설명하는 함수를 추론하는 기계학습의 한 방법'

