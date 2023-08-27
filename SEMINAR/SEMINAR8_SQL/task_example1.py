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
from collections import OrderedDict


def save_contacts(ph_book : dict, file_name):
    with open(file_name, 'w') as file:
        


def print_contacts(ph_dict : dict):
    for key, val in ph_dict.items():
        print(f"Id: {key}")
        print(f"имя {val['first_name']}")
        print(f"фамилия {val['last_name']}")
        print(f"отчество {val['middle_name']}")
        print(f"телефон номер {val['phone_num']}")
        print()


def search_contact(ph_dic : dict, deleted: bool = False):
    search_con = input("Введите искомый контакт: ")
    keys_to_del = []

    for con_id, con_info in ph_dic.items():
        if search_con.lower() in con_info['last_name'].lower() or search_con.lower() in con_info['first_name'].lower() or search_con.lower() in con_info['middle_name'].lower() or search_con.lower() in con_info['phone_num'].lower():
            if not deleted:
                print(f"\nId: {con_id}")
                print(f"имя {con_info['first_name']}")
                print(f"фамилия {con_info['last_name']}")
                print(f"отчество {con_info['middle_name']}")
                print(f"телефон номер {con_info['phone_num']}\n")
            else:
                choise = input(f"\nвы увереы, что хотите удалить Id: {con_id}?\n'1' - Да\nиначе - нет: ")
                if choise == '1':
                    keys_to_del.append(con_id)
                else:
                    return
    if deleted:
        for i in keys_to_del:
            del ph_dic[i]


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


def write_contacts(ph_dic : dict):
    if len(ph_dic) == 0:
        id_contact = 1
    else:
        id_contact = list(ph_dic.keys())[-1] + 1
    con_dic = {}

    con_dic['last_name'] = input("Введитн фамилию: ")
    con_dic['first_name'] = input("Введите имя: ")
    con_dic['middle_name'] = input("Введите отчество: ")
    con_dic['phone_num'] = input("Введите номер телефона:")

    ph_dic[id_contact] = con_dic
    print(f"Контакт с Id {id_contact} добавлен!\n")

    
def user(phone_dic : dict, file_name):
    flag = True
    while(flag):
        inp_user = input(f"\n1. Ввод дааных\n2. Найти контакт\n3. Удалить контакт\n4. Распечатать контакты\n5. Выход\nВведите ваш выбор: ")

        if inp_user == '1':
            write_contacts(phone_dic)
        elif inp_user == '2':
            search_contact(phone_dic)
        elif inp_user == '3':
            search_contact(phone_dic, True)
        elif inp_user == '4':
            print_contacts(phone_dic)
        elif inp_user == '5':
            save_contacts(phone_dic, file_name)
        elif inp_user == '6':
            flag = False


ph_dic = {}
file_name = 'ph_book.txt'
user(ph_dic, file_name)
# for k, v in ph_dic.items():
#     print(k, v)