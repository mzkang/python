# <2018-07-02>


        


### lab4-9 ### 행렬 모양으로 소문자 출력
list = [['A','B','C','D','E'],
	['F','G','H','I','J'],
	['K','L','M','N','O']]

for i in range(len(list)):
	for j in range(len(list[i])):
		print(list[i][j].lower(), end = ' ')
	print('\n')
# lab4-9 교수님 답
for row in list:
    for column in row:
        print(column.lower(), end=' ')
    print('\n')






# lab4-10 구구단 출력
for x in range(2,10):
    for y in range(1,10):
        print(x*y, end = ' ')
    print('\n')
# lab4-10 교수님 답
for x in range(2,10):
    for y in range(1,10):
        print(x*y, end = ' ')
    print()






# lab4-11 윤년 출력
leaps = []
for x in range(2000,3001):
    if x % 400 == 0 :
        leaps.append(x)
    elif x % 100 == 0 :
        continue
    elif x % 4 == 0 :
        leaps.append(x)

print(leaps)
# lab4-11 교수님 답
leaps = [year for year in range(2000,3001)
         if year % 4 == 0 and year % 100 !=0 or year % 400 == 0]

print(leaps)






### lab4-12 ### 천단위 콤마 형식 
staff = {'David' : 30000, 'John' : 50000, 'Andrew' : 45000,
         'Rita' : 70000, 'Micael' : 10000}
for name in staff.keys():
	if staff[name] >= 50000:
		print('{}\'s salary is {:,}'.format(name, staff[name]))





# lab4-13 -(1)
fruits = ['사과','딸기','바나나','블루베리','포도']
fruit = input('과일 이름을 입력하세요...: ')

for i in range(len(fruits)):
    if fruit == fruits[i]:
        print('과일 목록의', str(i+1) + '번째에 존재합니다.')
        break
else:
    print('과일 목록에 존재하지 않습니다.')
# lab4-13 -(2)
fruits = ['사과','딸기','바나나','블루베리','포도']
fruit = input('과일 이름을 입력하세요...: ')

for fruit in fruits:
    print('과일 목록의 ' + str(fruits.index(fruit) +1) +
          '번째에 존재합니다.')
    fruit = input('과일 이름을 입력하세요...: ')
else :
    print('과일 목록에 존재하지 않습니다')
    


