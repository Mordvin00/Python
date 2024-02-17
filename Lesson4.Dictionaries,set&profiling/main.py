'''
Напишите программу, которая принимает на вход строку,
и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам
с помощью постфикса формата _n.

Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split()
'''
# data = input('Введите символы через пробел: ').split()

# count_dict = {}

# # for item in data:
# #     if item in count_dict:
# #         count_dict[item] += 1
# #     else:
# #         count_dict[item] = 0
# #     if count_dict[item] != 0:
# #         string = f'{item}_{count_dict[item]}'
# #     else:
# #         string = item
# #     print(string, end=' ')

# for item in data:
#     count_dict[item] = count_dict.get(item, -1) + 1
#     print(f'{item}_{count_dict[item]}' if count_dict[item] != 0 else item, end=' ')

'''Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.
Input: She sells sea shells on the sea shore The shells
that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea
shore shells
Output: 13'''

# exmp_str = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"

# # exmp_list = exmp_str.replace(".", " ").lower().split()

# # exmp_list = set(exmp_list)

# # print(exmp_list, len(exmp_list))


# for char in '.,!?':
#     exmp_str = exmp_str.replace(char, ' ')
# exmp_str = exmp_str.lower().split()
# print(len(set(exmp_str)))

'''Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.

Примечание: Программные коды см. ниже.

Ваня:
n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)


Петя:
n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n)
'''

'''Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа,
которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

Пример

На входе:

var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел

На выходе:

3 5'''

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# myset_1 = set()
# myset_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     myset_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     myset_2.add(i)
# lok = myset_1 & myset_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')

'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
6 12'''

# from random import randint
# n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m_set)


# var1 = '5 4' 
# var2 = '1 3 5 7 9' 
# var3 = '2 3 4 5'

# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# myset_1 = set()
# myset_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#     myset_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#     myset_2.add(i)
# s_set = sorted(myset_1.intersection(myset_2))
# print(*s_set)


'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
4 -> 1 2 3 4
9'''


# n = 5 # кустов
# from random import randint
# list_1 = list(randint(1, 5) for i in range(int(input('Введите кол-во кустов: '))))
# print(list_1)
# a = int(input('Введите № куста: '))
# res = 0
# if a == 1:
#     res = list_1[0] + list_1[1] + list_1[-1]
# elif a == len(list_1):
#     res = list_1[-2] + list_1[-1] + list_1[0]
# else:
#     res = list_1[a-1] + list_1[a-2] + list_1[a]
# print(res, 'ягод')


arr = [5, 8, 6, 4, 9, 2, 7, 3]

# n = int(input())
# arr = list()
# for i in range(n):
#     x = int(input())
#     arr.append(x)

arr_count = list()

for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))
