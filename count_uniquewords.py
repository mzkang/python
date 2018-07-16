import re


enter = input('파일 이름을 입력하세요(따옴표 없이): ')

line = open(enter, mode = 'r', encoding = 'utf-8').read()

line = line.split(' ')


dictionary = {'고향은':0, '고향의':0, '그':0, '그립습니다':0,
              '꽃':0, '꽃-동-네':0, '꽃피는-산골':0, '나의':0}

for a  in line :
    for b in dictionary :
        if re.search(b, a):
            dictionary[b] += 1


