## <file handling>



#lab 7-1 ------틀림(format)------

enter = input('파일 이름을 입력하세요...: ')


file = open(enter, mode = 'r', encoding = 'utf-8').readlines()

for i in range(len(file)):
    print('{:4}:{}'.format(i+1, file[i]), end = '')


#lab 7-2-A
 # 내용을 'head.py'로 저장

#lab 7-2-B
 # 내용을 'tail.py'로 저장

#lab 7-2-C
 # 내용을 'body.py'로 저장

#lab 7-3-A
 # 내용을 'count_uniquewords.py'로 저장
 
#lab 7-4
 # 내용을 'ANSWER_grepword.py'로 저장



#lab 7-5


import string


enter = input('파일 이름을 입력하세요(따옴표 없이): ')

lines = open(enter, encoding = 'utf-8').readlines()

total_lines = len(lines)
total_words = 0
total_letters = 0

for line in lines :
    line = line.split()
    for word in line :
        for t in string.punctuation :
            word = word.replace(t,'')

        if word:
            total_words += 1
            total_letters += len(word)

print('=> {} 파일은 {} 줄, {} 단어, {} 문자로 구성되어 있습니다.'.format(
    enter, total_lines, total_words, total_letters))



# parsing

file = open('grades.txt', encoding = 'utf-8-sig')

data = file.read().splitlines()

file.close()

print(len(data))
print(data)


data_parsed = data

for i in range(len(data_parsed)):
    data_parsed[i] = data_parsed[i].split(',')

print(data_parsed)




#lab 7-6

file = open('pitcher_stats.txt', encoding = 'utf-8-sig')

data = file.read().splitlines()
file.close()



for i in range(len(data)):
    data[i] = data[i].split('/')



for i in range(len(data)):
    data[i][1] = int(data[i][1])
    data[i][2] = int(data[i][2])
    data[i][3] = float(data[i][3])

print(data)






#lab 7-7

with open('pitcher_stats.txt', mode = 'r', encoding = 'utf-8') as f:
    data = f.read().splitlines()
    for i in range(len(data)):
        data[i] = data[i].split('/')

for i in range(len(data)):
    # join은 string을 return
    data[i] = '/'.join(data[i])


with open('pitcher_stats_new.txt', mode = 'w', encoding = 'utf-8') as f:
    for row in data :
        f.write(row + '\n')
        




#lab 7-8-A

data = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently."

data = data.split('. ')

with open('zen_of_python.txt', mode = 'w', encoding = 'utf-8-sig') as f:
    for sentence in data:
        if sentence.endswith('.'):
            f.write(sentence + '\n')
        else:
            f.write(sentence + '. \n')


#lab 7-8-B

zen = [
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!"]

with open('zen_of_python.txt', mode = 'a', encoding = 'utf-8') as f:
    for sentence in zen:
        f.write(sentence + '\n')





#lab 7-9-A

enter = input('파일 이름을 입력하세요...: ')

with open(enter, encoding = 'utf-8') as f:
    for i in f:
        print(i.upper(), end='')
        #(==)----------------------
        # print(i.upper().rstrip())




#lab 7-9-B


from os.path import abspath


enter = input('파일 이름을 입력하세요...: ')

with open(enter, encoding = 'utf-8') as f:
    with open('UPPER'+enter, mode = 'w', encoding = 'utf-8') as u:
        for line in f:
            u.write(line.upper())

print('"{}" 파일이 {} 디렉토리에 생성되었습니다.'.format(
    'UPPER'+enter, abspath('UPPER'+enter)))

 #===교수님 답 (더 정확)
from os import path

file = input('파일 이름을 입력하세요...: ')

if path.isfile(file):
    directory, filename = path.split(file)
else :
    raise FileNotFoundError


outfile = path.join(directory, 'UPPER' + filename)

with open(file, encoding = 'utf-8') as fin:
    with open(outfile, mode = 'w', encoding = 'utf-8') as fout :
        for line in fin :
            fout.write(line.upper())

print('"{}" 파일이 {} 디렉토리에 생성되었습니다.'.format(path.basename(outfile),
                                          path.dirname(path.abspath(outfile))))
