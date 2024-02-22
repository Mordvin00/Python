'''
Задача №49.
Создать телефонный справочник с возможностью
импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные,
которые должны находиться в файле.
1. Программа должна выводить данные.
2. Программа должна сохранять данные в текстовом файле.
3. Пользователь может ввести одну из характеристик для
   поиска определенной записи (Например имя или фамилию человека).
4. Использование функций. Ваша программа не должна быть линейной.

1. Показывать все контакты
2. Создавать новый контакт
3. Поиск по контактам
4. Изменение контакта
5. Удаление контакта
6. Контакт должен содержать имя и фамилию, номер телефона и комментарий

Дополнительные опции
1. Открыть файл
2. Сохранить файл
'''

'''
Код из семинара (рабочий см. далее)
file = open('file.txt','a')
file.close()

def read_direct():
    file = open('file.txt', 'r')
    list_direct = file.readlines()
    list_direct_end = []
    for i in list_direct:
        i = i.split('|')
        list_direct_end.append(i)
        list_direct_end.append(' ')

    file.close()
    
    return list_direct_end

def append_contact():
    file = open('file.txt', 'a')
    print("Пример добавления: Иванов Иван|891544444|Друг")
    contact = input("")
    file.writelines(contact)
    file.close()

def check_contact(list1, check):
    list_checks = []
    for i in range(len(list1)):
        if list1[i] == check:
            list_checks.append(list1[i])
            list_checks.append(list1[i+1])
            list_checks.append(list1[i+2])
            list_checks.append(" ")
    
    return list_checks

def change_file(list1):
    file = open("file.txt", 'w')
    for i in range(len(list1)):
        endString = list1[i] + '|' + list1[i + 1] + '|' + list1[i + 2]
        file.writelines(endString)
    file.close()

def change_direct(list1):
    change = input("Введите фамилию и имя, которые хотите изменить: ")
    changeble = input("Пример изменения: Иванов Иван|891544444|Друг")
    changeble_list = changeble.split('|')
    for i in range(len(list1)):
        if list1[i] == change:
            list1[i] = changeble_list[0]
            list1[i+1] = changeble_list[1]
            list1[i + 2] = changeble_list[2]
    
    return list1

def delete_element(list1: list):
    deletedElem = input("Введите фамилию и имя, которые хотите удалить: ")
    
    



def main():
    print("Выберите действие\n 1.Показать все контакты\n 2.Добавить контакт\n 3. Поиск контакта \n 4.Изменение контакта \n 5.Удаление контакта")
    check = int(input(" "))
    if check == 1:
        list_direct = read_direct()
        for i in list_direct:
            print(i)
    elif check == 2:
        append_contact()
    elif check == 3:
        list_direct = read_direct()
        checking = input("Какую фамилию вы хотите найти: ")
        list_checks = check_contact(list_direct, checking)
        if len(list_checks) > 0:
            for i in list_checks:
                print(i)
        else:
            print("Такого контакта не существует")
    elif check == 4:
        list_direct = read_direct()
        new_list_direct = change_direct(list_direct)
        change_file(new_list_direct)
    elif check == 5:
        55
    else:
        print("Введите цифру из перечня доступных")
'''

# Телефонный справочник с возможностью импорта, чтения и записи данных в файл формата .txt:

def choose_action(phonebook): # Главный интерфейс
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Создать новый контакт\n\
4 - Изменить контакт\n5 - Удалить контакт\n6 - Показать все контакты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            file_to_add = input('Введите название импортируемого файла: ')
            import_data(file_to_add, phonebook)
        elif user_choice == '2':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '3':
            add_phone_number(phonebook)
        elif user_choice == '4':
            change_phone_number(phonebook)
        elif user_choice == '5':
            delete_contact(phonebook)
        elif user_choice == '6':
            show_phonebook(phonebook)
        elif user_choice == '0':
            print('Приложение закрыто!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue


def import_data(file_to_add, phonebook): # Импорт данных из файла
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
            contacts_to_add = new_contacts.readlines()
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'{file_to_add} не найден')


def read_file_to_dict(file_name): # Чтение данных из файла для дальнейшего вывода в консоль (Поиск, вывод всех контактов)
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона', 'Комментарий']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list(file_name): # Чтение данных из файла для дальнейшей записи в файл (изменение контактов)
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


def search_parameters():  # Интерфейс для пользователя при поиске контактов
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n4 - по комментарию\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    elif search_field == '4':
        search_value = input('Введите комментарий для поиска: ')
        print()
    return search_field, search_value


def find_number(contact_list): # Приём критериев поиска и поиск контактов
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона', '4': 'Комментарий'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_number(): # Интерфейс создания нового контакта
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    a_comment = input('Введите номер комментарий: ')
    return last_name, first_name, phone_number, a_comment


def add_phone_number(file_name): # Приём критериев создания нового контакта и запись в файл
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')


def show_phonebook(file_name): # Передача всего списка контактов с сортировкой по фамилии
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_to_modify(contact_list: list): # Поиск контактов в файле
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def change_phone_number(file_name): # Интервейс для пользователя при работе с контактами
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n4 - Комментарий\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    elif field == '4':
        number_to_change[3] = input('Введите комментарий: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name): # Удаление контакта
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list): # Вывод списка в консоль
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__': # Отсылка к главному интерфейсу и файлу с данными
    file = 'Phonebook.txt'
    choose_action(file)

'''
Представляю вашему вниманию более-менее рабочую версию согласно нашему заданию,
проверил - основное всё работает, некоторые моменты сыроваты,
например при поиске необходимо полное соответсвие критерию поиска,
а так же, пока не знаю как исключить глюк в некоторых итерациях если какое то поле пустое.
В целом, логика и работа программы понятна, а вот с синтаксисом проблема,
сложно сразу смекнуть какую команду или функию применить, но это дело наживное!
На начальном этапе тяжело морально, когда ничего не работает, а потом,
когда уже получаешь в консоли хоть что то - сразу легче, уже видно на каком этапе ошибка:)
'''