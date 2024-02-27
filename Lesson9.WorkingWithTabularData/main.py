'''
https://t.me/STONE_Py
https://gbcdn.mrgcdn.ru/uploads/record/316015/attachment/3bc348a70ba118d04f3a0b07374d8f26.mp4
Разбор телефонного справочника по модулю
'''

'''
Домашнее задание через автотест
Дан файл california_housing_train.csv.
Определить среднюю стоимость дома,
где количество людей от 0 до 500 (population)
и сохранить ее в переменную avg.
Используйте модуль pandas.

Идеальное решение:

import pandas as pd

df = pd.read_csv('california_housing_train.csv')
avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean()
# Средняя стоимость дома, где количество людей от 0 до 500

'''

# # Моё решение:

# import pandas as pd

# df = pd.read_csv('california_housing_train.csv')
# mask = (df['population'] > 0) & (df['population'] < 500)
# filtered_df = df[mask]
# avg = filtered_df['median_house_value'].mean()
# print(avg)

'''
Домашнее задание через автотест
Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households"
в зоне минимального значения переменной min_population
и сохраните это значение в переменную
max_households_in_min_population.
Используйте модуль pandas.

Идеальное решение:

import pandas as pd

df = pd.read_csv('california_housing_train.csv')

# Найти минимальное значение 'population'
min_population = df['population'].min()

# Отфильтровать строки с минимальным значением 'population' и найти максимальное значение 'households'
max_households_in_min_population = df[df['population'] == min_population]['households'].max()

'''

# # Моё решение:

# import pandas as pd

# df = pd.read_csv('california_housing_train.csv')
# min_population = df['population'].min()
# max_households_in_min_population = df[df['population'] == min_population]['households'].max()
# print(max_households_in_min_population)


