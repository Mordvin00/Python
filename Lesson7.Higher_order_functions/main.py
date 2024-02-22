'''
Задача №47.
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.

Ввод:
values = [1, 23, 42, 'asdfg']
transformed_values = list(map(trasformation, values))
if values == transformed_values:
 print('ok')
else:
 print('fail')

Вывод:
ok
'''







'''
Задача №49.
Планеты вращаются вокруг звезд по эллиптическим орбитам.
Назовем самой далекой планетой ту, орбита которой имеет
самую большую площадь. Напишите функцию
find_farthest_orbit(list_of_orbits), которая среди списка орбит
планет найдет ту, по которой вращается самая далекая
планета. Круговые орбиты не учитывайте: вы знаете, что у
вашей звезды таких планет нет, зато искусственные спутники
были были запущены на круговые орбиты. Результатом
функции должен быть кортеж, содержащий длины полуосей
эллипса орбиты самой далекой планеты. Каждая орбита
представляет из себя кортеж из пары чисел - полуосей ее
эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
где a и b - длины полуосей эллипса. При решении задачи
используйте списочные выражения. Подсказка: проще всего
будет найти эллипс в два шага: сначала вычислить самую
большую площадь эллипса, а затем найти и сам эллипс,
имеющий такую площадь. Гарантируется, что самая далекая
планета ровно одна.

Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

Вывод:
2.5 10
'''
# from math import pi

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(orbits):
#     orbits = list(filter(lambda x: x[0] != x[1], orbits))
#     orbits_area = list(map(lambda x: pi * x[0] * x[1], orbits))
#     for i in range(len(orbits_area)):
#         if orbits_area[i] == max(orbits_area):
#             return [orbits[i], orbits_area[i]]

# print(*find_farthest_orbit(orbits))


# from math import pi

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(list_of_orbits):
#     list_of_orbits_filtered = list(filter(lambda x: x[0] != x[1], list_of_orbits))
#     find_max_squre = list(map(lambda x: x[0] * x[1] * pi, list_of_orbits_filtered))
#     index_with_max = find_max_squre.index(max(find_max_squre))
#     return list_of_orbits[index_with_max]

# print(*find_farthest_orbit(orbits))


# orbits = [(1, 12), (2.5, 10), (7, 2), (6, 6), (4, 3)]


# def find_farthest_orbit(list_of_orbits):
#     validate_orbits = list(filter(lambda x: x[0] != x[1], list_of_orbits))
#     validate_orbits = list(map(lambda x: (x, x[0] * x[1]), validate_orbits))
#     return max(validate_orbits, key=lambda x: x[1])[0]


# print(*find_farthest_orbit(orbits))



'''
Задача №51.
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.

Ввод:
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
print('same')
else:
print('different')

Вывод:
same
'''

# def same_by(characteristic, objects):
#     start_len = len(objects)
#     objects = list(filter(characteristic, objects))
#     filtered_len = len(objects)
#     if filtered_len == start_len:
#         return True
#     else:
#         return False

# def same_by(characteristic, objects):
#     if not objects:
#         return True
#     return len(set(map(characteristic, objects))) == 1




'''
Напишите функцию print_operation_table(operation, num_rows, num_columns),
которая принимает в качестве аргумента функцию,
вычисляющую элемент по номеру строки и столбца.
По умолчанию номер столбца и строки = 9.

Аргументы num_rows и num_columns
указывают число строк и столбцов таблицы, которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: бинарной операцией называется любая операция,
у которой ровно два аргумента, как, например, у операции умножения.

Между элементами должен быть 1 пробел, в конце строки пробел не нужен.

Пример

На входе:
print_operation_table(lambda x, y: x * y, 3, 3)

На выходе:
1 2 3
2 4 6 
3 6 9
'''

# def print_operation_table(operation, num_rows=9, num_columns=9,):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    
#     if num_columns > 2 and num_rows > 2:
#         for i in a:
#             print(*[f"{x:>1}" for x in i])
#     else:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")

# print_operation_table(lambda x, y: x * y, 3, 3)


'''def print_operation_table(operation, num_rows=9, num_columns=9):
    result = []
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                if j != num_columns :
                    result.append(f'{operation(i, j)} ')
                else:
                    result.append(operation(i, j))
            result.append('\n')
        print(''.join([str(i) for i in result[:len(result) - 1]]))

print_operation_table(lambda x, y: x * y, 3, 3)'''



'''
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
Поскольку разобраться в его кричалках не настолько просто,
насколько легко он их придумывает, Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов
(т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов,
то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически
в переменную stroka в виде строки.
В ответе напишите Парам пам-пам,
если с ритмом все в порядке и Пам парам,
если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести:
Количество фраз должно быть больше одной!.

Пример

На входе:
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

На выходе:
Парам пам-пам
'''


'''def count_vowels(word):

    vowels = 'aeiouy'

    count = 0

    for letter in word:

        if letter.lower() in vowels:
            count += 1
            return count



def check_rhythm(poem):

    phrases = poem.split(" ")

    syllables = []

    for phrase in phrases:

        words = phrase.split("-")

        phrase_syllables = []

        for word in words:

            syllable_count = count_vowels(word)

            phrase_syllables.append(syllable_count)

        syllables.append(phrase_syllables)

    for i in range(1, len(syllables)):

        if syllables[i] != syllables[i-1]:

            return "Пам парам"

    return "Парам пам-пам"

# Ввод стихотворения

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# stroka = input("Введите стихоторение: ")

# Проверка ритма

result = check_rhythm(stroka)

print(result)'''




def rhythm(str):
    str = str.split()
    list = []
    for word in str:
        result = 0
        for i in word:
            if i in 'аеёиоуыэюя':
                result += 1
        list.append(result)
    return len(list) == list.count(list[0])

# print('Введите: пара-ра-рам рам-пам-папам па-ра-па-дам')
# stroka = input()

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

if len(stroka.split()) == 1:
    print('Количество фраз должно быть больше одной!')
else:
    if rhythm(stroka):
        print('Парам пам-пам')
    else:
        print('Пам парам')


'''
vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka.split()
if len(phrases) < 2:
 print('Количество фраз должно быть больше одной!')
else:
 countVowels = []

 for i in phrases:
  countVowels.append(len([x for x in i if x.lower() in vowels]))

 if countVowels.count(countVowels[0]) == len(countVowels):
  print('Парам пам-пам')
 else:
  print('Пам парам')
'''