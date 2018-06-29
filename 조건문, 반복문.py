### <if, while, for문> ###



# lab 4-1
x = int(input('x를 입력하세요: '))
y = int(input('y를 입력하세요: '))
if x>y:
    print('x가 y보다 큽니다.')
elif x<y:
    print('x가 y보다 작습니다.')
else:
    print('x와 y가 같습니다.')
    


# lab 4-2
x = int(input('x를 입력하세요: '))
y = int(input('y를 입력하세요: '))
if x%y == 0:
    print('zero')
else:
    if (x%y)%2 == 0:
        print('even')
    else:
        print('odd')



# lab 4-3
t=(1,3,5,7,'a','b','c')
if 5 in t:
    print('5 is in t')
if 'd' in t:
    print('d is in t')



# lab 4-4
integers = [1,2,3,4,5,6,7,8,9,10]
i = 0
while i < len(integers):
    if integers[i] % 2 == 1:
        print(integers[i])
    i += 1
# lab 4-7 (4-4를 for문으로)
for i in range(1,11):
    if i % 2 == 1:
        print(i)



# lab 4-5
colors = ['red','blue','pink','green','yellow','purple']
i=0
while i < len(colors):
    if colors[i][0] == 'p':
        print(colors[i])
    i += 1
### lab 4-5 (startswith 사용)
colors = ['red','blue','pink','green','yellow','purple']
i=0
while i < len(colors):
    if colors[i].startswith('p'):
        print(colors[i])
    i += 1
# lab 4-8 (4-5를 for문으로)
colors = ['red','blue','pink','green','yellow','purple']
for color in colors:
    if color.startswith('p'):
        print(color)




# lab 4-6
fruits = ['사과','딸기','바나나','블루베리','포도']
fruit = input('과일 이름을 입력하세요...: ')
while fruit in fruits :
    print('과일 목록의 ' + str(fruits.index(fruit) + 1) +
          '번째에 존재합니다.')
    fruit = input('과일 이름을 입력하세요...: ')
else:
    print('과일 목록에 존재하지 않습니다')
# lab 4-6 교수님 코딩
target = input('과일 이름을 입력하세요...: ')

fruits = ['사과','딸기','바나나','블루베리','포도']
index = 0
while index < len(fruits):
    if fruits[index] == target:
        print('과일 목록의 {}번째에 존재합니다.'.format(index +1))
        break
    index += 1
else:
    print('과일 목록에 존재하지 않습니다.')



        
