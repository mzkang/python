#lab 5-1-1

integer = list(range(1,101))
for i in range(len(integer)):
    integer[i] = integer[i] + 1
print(integer)



#lab 5-1-2

t = (1,3,5,7,9)
t = list(t)

for i in range(len(t)):
    t[i] = str(t[i])

t += ['x','y','z']
 #(==) t += list('xyz')
 #(==) t.append('x') 3번
 #(==) t.extend(['x','y','z'])

for j in t:
    print(j, type(j))




#lab 5-1-3

def xor(x,y):
    if x != y :
        print('True')
    else :
        print('False')

xor(True, True)

 #------------------위는 print/ 아래는 return---

def xor(x,y):
    if x != y :
        return True
    else :
        return False

print(xor(True, True))




#lab 5-1-4

def expand_rectangle(x, y):
    print('Width =', x+5)
    print('Length =', 2*y)
    a = x * y
    b = (x+5)*(2*y)
    print('Area Ratio =', round(a/b,2))
 #-----교수님
    
def expand_rectangle(x, y):
    area_original = x * y
    w = x + 5
    h = y * 2
    area_expanded = w * h
    print('Width =', w)
    print('Length =',h)
    print('Area Ratio =', round(area_original/area_expanded,2))
    
expand_rectangle(7,10)

 



#lab 5-1-5

def calculator(operator, int1, int2):
    if operator == 'add':
        return int1 + int2
    elif operator == 'sub':
        return int1 - int2
    elif operator == 'mul':
        return int1 * int2
    elif operator == 'div':
        return int1 / int2
    else :
        print('{} is not supported.'.format(operator))

calculator('addition',3,5)



#lab 5-1-6

def vowel(x):
    list = ['a','e','i','o','u']
    count = 0
    for i in range(len(x)):
        if x[i].lower() in list :
            #(==)------------
            for char in x:
                if char.lower() in list 
            #----------------
            count += 1
                      
    return count

print(vowel('Apples'))
print(vowel('I love Python'))





#lab 5-2-1

def calculator_int(*x):
    my_sum = 0
    my_count = 0
    for a in x:
        if a == 0 :
            break
        else :
            my_sum += a
            my_count += 1
    return my_sum, int(my_sum/my_count)

print(calculator_int(1,2,3,4,5))
print(calculator_int(1,3,5,7,9,10))
print(calculator_int(-3,2,0,4,5))        




#lab 5-2-2

mylist = [1,2,3]
mytuple = ('a','b','c')

def search(x, obj):
    a = False
    for i in range(len(x)):
        if x[i] == obj:
            return  i
            a = True
    if a == False :
        return a
 #(==)교수님 코딩
#
def search(seq, e):
    if e in seq:
        return seq.index(e)
    return False

print(search(mylist,2))
print(search(mylist, 10))
print(search(mytuple,'c'))
print(search(mytuple,'1'))
    



#lab 5-2-3

def search_char(word, char):
    if char in word:
        return word.index(char)
    return -1




#lab 5-2-4

def reverse_odd_text(*word):
    count = 0
    for a in word:
        if len(a) % 2 == 1:
            print(a[::-1])
            count += 1
        else :
            print(a)
    return count

odd_count = reverse_odd_text('red','blue','green','yellow','purple',
                             'black','white')
print(odd_count)


odd_count = reverse_odd_text('나는 드러머입니다','베이스','기타','키보드','보컬')
print(odd_count)





#lab 5-2-5

def sort_scores(*score):
    score = list(score)
    score.sort(reverse = True)
    for i in score:
        print(i)

sort_scores(100, 27, 65, 88, 46, 97, 75, 53)




####틀림####lab 5-2-6

def sort_by_word_length(words):
    t = []
    for w in words:
        t.append((len(w),w))

    t. sort(reverse=True)
    sorted_words = []
    for length, w in t:
        sorted_words.append(w)
    return sorted_words

  #------------list 축약형-------
#
def sort_by_word_length_lc(words):
    t = [(len(w), w) for w in words]
    t.sort(reverse=True)
    return [w for length, w in t]








