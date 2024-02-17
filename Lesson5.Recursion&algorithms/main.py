'''
Последовательностью Фибоначчи называется
последовательность чисел a0, a1, ..., an, ...,
где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
'''

# def fibonaci(n):
#     if n in (1, 2): # n == 1 or n == 2:
#         return n
#     elif n == 0:
#         return 0
#     else:
#         return fibonaci(n-1) + fibonaci(n-2)
    
# n = int(input("Введите номер числа последовательности: "))

# print(fibonaci(n))

'''
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1


str = input("Введите последовательность чисел через пробел: ")

list1 = str.split()

def functionnew(list1):
    if list1[0] > list1[1]:
        max = list1[0]
        min = list1[1]
    else:
        max = list1[1]
        min = list1[0]

    for i in list1[2:]:
        if i > max:
            max = i
        elif i < min:
            min = i
    
    for j in range(len(list1)):
        if list1[j] == max:
            list1[j] = min

    return list1

print(*functionnew(list1))
'''

# marks = input("Введите последовательность чисел через пробел: ").split()

# def functionnew(list1):
#     max_mark = max(list1)
#     min_mark = min(list1)

#     for j in range(len(list1)):
#         list1[j] = min_mark if list1[j] == max_mark else list1[j]
#     return list1


# print(*functionnew(marks))



'''
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым.
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes

def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

print(is_prime(int(input("введите число: "))))
'''

# def is_simple(number):
#     if number in (1, 2, 3):
#         return True
#     if number % 2 == 0:
#         return False
#     for dev in range(3, int(number**0.5) + 1, 2):
#         if number % dev == 0:
#             return False
#     return True


'''
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание.
В программе запрещается объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
'''

# def reverse_input(count):
#     if not count:
#         return ''
#     char = input('Введите символ: ')
#     return reverse_input(count - 1) + char


# num = int(input('Сколько символов будем вводить: '))
# print(reverse_input(num))


'''
Напишите функцию f, которая на вход принимает два числа a и b,
и возводит число a в целую степень b с помощью рекурсии.

Функция не должна ничего выводить, только возвращать значение.

Пример:

a = 3; b = 5 -> 243 (3⁵)
a = 2; b = 3 -> 8
'''

# a = 3
# b = 5

# def f(a, b):
#     if b == 0:        
#         return 1
#     else:
#         return a * f(a, b - 1)
    
# def f(a, b):
#   if b == 0:
#     return 1
#   return f(a, b - 1) * a


# print(f(a, b))



'''
Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

Функция не должна ничего выводить, только возвращать значение.

Пример:

sum(2, 2)
# 4
'''

a = 3
b = 5

# def sum(a, b):
#     if a == 0:        
#         return b
#     else:        
#         return sum(a - 1, b + 1)
    

def sum(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return sum(a + 1, b - 1)

print(sum(a, b))