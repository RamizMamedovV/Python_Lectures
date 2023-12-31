"""
Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной
записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной
"""
# from collections import OrderedDict
#               не получилось отсортировать словарь после удаления

    # keys_ph_dic = sorted(ph_dic.keys())
    # sorted_ph_dic = {}
    # len_ph_dic = len(ph_dic)
    # for i in range(len_ph_dic):
    #     sorted_ph_dic[i] = ph_dic[keys_ph_dic[i - 1]]
    # ph_dic = sorted_ph_dic
    # sorted_ph_dic = OrderedDict()

    # sorted_keys = sorted(ph_dic.keys())
    # for key in sorted_keys:
    #     sorted_ph_dic[key] = ph_dic[key]
    # ph_dic = sorted_ph_dic

#                       куски кода из урока

"""
def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')
"""
"""
def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number
"""
"""
import json

phonebook = {"Дядя Петя": {"phone_numbers": ["12345", "12346"], "birthday": "01.03/1996", "e-mail": "petya@mail.ru"} }

with open("phonebook.json", "w", encoding = "utf-8") as phonebookjson:
    phonebookjson.write(json.dumps(phonebook, ensure_ascii = False))
"""
"""
def save():
    with open("dishes.json", "w", encoding = "utf-8") as cul_bot:
        cul_bot.write(json.dumps(dishes, ensure_ascii = False))
    print("Бот успешно сохранил вашу кулинарную библиотеку. Проверьте изменения в файле dishes.json")

def load():
    with open("dishes.json", "r", encoding = "utf-8") as cul_bot:
        dishes = json.load(cul_bot)
    print("Бот успешно загрузил измененную библиотеку в файл dishes.json")
"""
"""
def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts

    def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list

    def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()
"""

"""
# Создать телефонный справочник с возможностью импорта и экспорта данных в 
# формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной """


# def choose_action(phonebook):
#     while True:
#         print('Что вы хотите сделать?')
#         user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
# 4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
#         print()
#         if user_choice == '1':
#             file_to_add = input('Введите название импортируемого файла: ')
#             import_data(file_to_add, phonebook)
#         elif user_choice == '2':
#             contact_list = read_file_to_dict(phonebook)
#             find_number(contact_list)
#         elif user_choice == '3':
#             add_phone_number(phonebook)
#         elif user_choice == '4':
#             change_phone_number(phonebook)
#         elif user_choice == '5':
#             delete_contact(phonebook)
#         elif user_choice == '6':
#             show_phonebook(phonebook)
#         elif user_choice == '0':
#             print('До свидания!')
#             break
#         else:
#             print('Неправильно выбрана команда!')
#             print()
#             continue


# def import_data(file_to_add, phonebook):
#     try:
#         with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
#             contacts_to_add = new_contacts.readlines()
#             file.writelines(contacts_to_add)
#     except FileNotFoundError:
#         print(f'{file_to_add} не найден')


# def read_file_to_dict(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
#     headers = ['Фамилия', 'Имя', 'Номер телефона']
#     contact_list = []
#     for line in lines:
#         line = line.strip().split()
#         contact_list.append(dict(zip(headers, line)))
#     return contact_list


# def read_file_to_list(file_name):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         contact_list = []
#         for line in file.readlines():
#             contact_list.append(line.split())
#     return contact_list


# def search_parameters():
#     print('По какому полю выполнить поиск?')
#     search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
#     print()
#     search_value = None
#     if search_field == '1':
#         search_value = input('Введите фамилию для поиска: ')
#         print()
#     elif search_field == '2':
#         search_value = input('Введите имя для поиска: ')
#         print()
#     elif search_field == '3':
#         search_value = input('Введите номер для поиска: ')
#         print()
#     return search_field, search_value


# def find_number(contact_list):
#     search_field, search_value = search_parameters()
#     search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
#     found_contacts = []
#     for contact in contact_list:
#         if contact[search_value_dict[search_field]] == search_value:
#             found_contacts.append(contact)
#     if len(found_contacts) == 0:
#         print('Контакт не найден!')
#     else:
#         print_contacts(found_contacts)
#     print()


# def get_new_number():
#     last_name = input('Введите фамилию: ')
#     first_name = input('Введите имя: ')
#     phone_number = input('Введите номер телефона: ')
#     return last_name, first_name, phone_number


# def add_phone_number(file_name):
#     info = ' '.join(get_new_number())
#     with open(file_name, 'a', encoding='utf-8') as file:
#         file.write(f'{info}\n')


# def show_phonebook(file_name):
#     list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
#     print_contacts(list_of_contacts)
#     print()
#     return list_of_contacts


# def search_to_modify(contact_list: list):
#     search_field, search_value = search_parameters()
#     sea
"""

# """
# serial_num_phone_book = []

# def search():
#     search_family = input('Введите фамилию иначе нажмите ввод:')
#     search_name = input('Введите имя иначе нажмите ввод:')
#     search_surname = input('Введите отчество иначе нажмите ввод:')
#     search_tel_num = input('Введите номер телефона иначе нажмите ввод:')

#     for i in len(serial_num_phone_book):
#         if search_family in serial_num_phone_book[i] or search_family != '':
#             if search_name in serial_num_phone_book[i] or search_name != '':
#                 if search_surname in serial_num_phone_book[i] or search_surname != '':
#                     if search_tel_num in serial_num_phone_book[i] or search_tel_num != '':


    

# def data_input():
#     phone_book = {'family':'', 'name':'', 'surname':'','tel_num':''}
#     phone_book['family'] = input('Введите фамилию:')
#     phone_book['name'] = input('Введите имя:')
#     phone_book['surname'] = input('Введите отчество:')
#     phone_book['tel_num'] = input('Введите номер телефона:')
#     serial_num_phone_book.append(phone_book)
#     print(serial_num_phone_book) 
#     print(f"спасибо ввод {len(serial_num_phone_book)} запмсм завершён")
#     user_input()

# def user_input():
#     search_wish = input('Для поиска введите "1", Для ввода данных введите "2", иначе выход: ')

#     if search_wish == '1':
#         search()
#     elif search_wish == '2':
#         data_input()
#     else:
#         print('Bye')

# user_input()   
# print(serial_num_phone_book) 
# """

"""
def search_to_modify(contact_list: list):
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


def change_phone_number(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'Phonebook.txt'
    choose_action(file)
"""