
# Задача 16

# import random
# list1 = []
# for i in range(1,10):
#     i = random.randint(1,10)
#     list1.append(i)
# print(list1)
# count = 0
# for i in range(1, len(list1)-1):
#     if list1[i-1] < list1[i] > list1[i+1]:
#         count += 1
# print(count)
 
# Задача 18

#import random

# N = int(input("Введите количество элементов в массиве "))
# list = [random.randint(1, 20) for i in range(N)]
# print(list)
# x = int(input("Введите искомое число "))
# index_element = 0
# min_element = abs(x - list[0])
# for i in range(1, N):
#     buffer_element = abs(x -list[i])
#    if buffer_element < min_element:
#        min_element = buffer_element
#        index_element = i

# print(f"Самый близкий по величине элемент к заданному числу {list[index_element]}")

# Задача 20

eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
N = abs(int(input('Введите 1, если играем в английской раскладке, либо 0, если в русской: ')))
word = input('Введите слово: ').upper()
if N == 1:
	print('вы получаете', sum([k for i in word for k, v in eng.items() if i in v]), 'очков')
elif N == 0:
	print('вы получаете', sum([k for i in word for k, v in rus.items() if i in v]), 'очков')
else:
    print('играете не по правилам!')
