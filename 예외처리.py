
# lab4-14
fruits = ['사과','딸기','바나나','블루베리','포도']
fruit = input('과일 이름을 입력하세요...: ')

try:
    index = fruits.index(fruit)
except ValueError:
    print('과일 목록에 존재하지 않습니다.')
else:
    print('과일 목록의 ' + str(fruits.index(fruit) + 1) +'번째에 존재합니다.')
    


# lab4-15
try:
    i = int(input('임의의 양의 정수를 입력하세요: '))
    if type(i) == int and i>0:
        i
except ValueError:
    print('ValueError: 1보다 큰 양의 정수를 입력하세요.')
else:
    for j in range(2,i):
        if i == 0 or i == 1:
            print('이 숫자는 소수가 아닙니다.')
            break
        elif i % j == 0 :
            print('{} x {} = {}\n이 숫자는 소수가 아닙니다.'.format(j, int(i/j), i))
            break
