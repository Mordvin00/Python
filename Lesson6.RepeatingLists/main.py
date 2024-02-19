'''
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод:
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1
(каждое число вводится с новой строки)

Вывод:
3 3 2 12
'''
'''
def listcreate(n):
    nums = []
    for i in range(n):
        number = int(input("Введите элемент массива: "))
        nums.append(number)
    
    return nums

def pleasenumber():
    n = int(input("Введите количество элементов в массиве: "))
    return n


def mainfunc(nums1, nums2):
    nums_result = list()
    for i in nums1:
        count = 0
        for j in nums2:
            if i == j:
                count += 1
        if count == 0:
            nums_result.append(i)

    return nums_result

n = pleasenumber()
nums1 = listcreate(n)

m = pleasenumber()
nums2 = listcreate(m)

print(mainfunc(nums1, nums2))
'''

# from random import randint as ri


# def create_list_of_numbers(size: int = 10, lower_limit: int = 0, upper_limit: int = 10) -> list[int]:
#     '''
#     Функция, которая создает список чисел по заданным параметрам
#     :param size: Размер списка
#     :param lower_limit: Нижний предел рандома
#     :param upper_limit: Верхний предел рандома
#     :return: Готовый список чисел
#     '''
#     # my_list = []
#     # for _ in range(size):
#     #     my_list.append(ri(lower_limit, upper_limit))
#     return [ri(lower_limit, upper_limit) for _ in range(size)]


# def list_size(name: str) -> int:
#     return int(input(f'Введите количество элементов в {name} списке: '))


# def main_function(list_1: list[int], list_2: list[int]):
#     # result_list = []
#     # for item in list_1:
#     #     if item not in set(list_2):
#     #         result_list.append(item)
#     return [item for item in list_1 if item not in set(list_2)]


# if __name__ == '__main__':
#     print(list_a := create_list_of_numbers(list_size('1')))
#     print(list_b := create_list_of_numbers(list_size('2')))
#     print('Новый список: ', main_function(list_a, list_b))



'''
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.

Ввод:
5
1 2 3 4 5

Вывод:
0

Ввод:
5
1 5 1 5 1

Вывод:
2
'''

'''
# from Sem4_1 import listcreate, pleasenumber

def main_function(list_1):
    count = 0
    for i in range(1, len(list_1) - 1):
        if list_1[i - 1] < list_1[i] and list_1[i] > list_1[i + 1]:
            count += 1

    return count

list_main = listcreate(pleasenumber())

print(main_function(list_main))
'''

# def main_function(list_1):
#     # count = 0
#     # for i in range(1, len(list_1) - 1):
#     #     if list_1[i - 1] < list_1[i] > list_1[i + 1]:
#     #         count += 1
#     #
#     # return count
#     return len([i for i in range(1, len(list_1) - 1) if list_1[i - 1] < list_1[i] > list_1[i + 1]])


# print(main_function([1, 5, 1, 5, 1]))



'''
Дан список чисел.
Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать.
Вводится список чисел.
Все числа списка находятся на разных строках.

Ввод:
1 2 3 2 3

Вывод:
2
'''

# my_list = [1, 2, 3, 7, 2, 3, 3, 3, 1, 7]


# def pair_count(lst: list[int]) -> int:
#     # count = 0
#     # for item in set(lst):
#     #     count += lst.count(item)//2
#     # return count

#     return sum([lst.count(item) // 2 for item in set(lst)])


# print(pair_count(my_list))



'''
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 10**5
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).

Ввод:
300

Вывод:
220 284


https://t.me/dirty_python

https://t.me/STONE_Py

'''

n = int(input("Введите число k: "))


def sum_of_proper_divisors(n): # Функция, которая возвращает сумму делителей числа
    s = 0
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            s += k
    return s

for i in range(1, n): # вывод списка дружественных чисел
    j = sum_of_proper_divisors(i)
    if i < j <= n and i == sum_of_proper_divisors(j):
        print(i, j)


'''
Введите число k: 1000000
220 284
1184 1210
2620 2924
5020 5564
6232 6368
10744 10856
12285 14595
17296 18416
63020 76084
66928 66992
67095 71145
69615 87633
79750 88730
100485 124155
122265 139815
122368 123152
141664 153176
142310 168730
171856 176336
176272 180848
185368 203432
196724 202444
280540 365084
308620 389924
319550 430402
356408 399592
437456 455344
469028 486178
503056 514736
522405 525915
600392 669688
609928 686072
624184 691256
635624 712216
643336 652664
667964 783556
726104 796696
802725 863835
879712 901424
898216 980984
'''


'''
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.

Пример

На входе:
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

На выходе:
1
2
3
6
7
9
10
11
13
14
16
19
'''

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# list_2 = []
# for i in range(len(lst_1)):
#     if list_1[i] >= min and list_1[i] <= max:
#         list_2.append(i)
# print(list_2)
# или
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)
#         # print(i, end=' ')


'''
Заполните массив элементами арифметической прогрессии.
Её первый элемент a1 , разность d и количество элементов n будет задано автоматически.
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

Пример

На входе:
a1 = 2
d = 3
n = 4

На выходе:
2
5
8
11
'''

# a1 = 2
# d = 3
# n = 4
# for i in range(n):
#     print(a1 + i * d)
#     # print(a1 + i * d, end=' ')