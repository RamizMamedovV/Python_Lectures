def add_contact(phonebook, last_name, first_name, middle_name, phone_number):
    new_id = len(phonebook) + 1
    phonebook[new_id] = {
        'last_name': last_name,
        'first_name': first_name,
        'middle_name': middle_name,
        'phone_number': phone_number
    }
    print("Контакт добавлен.")

def display_contacts(phonebook):
    for contact_id, contact_info in phonebook.items():
        print(f"ID: {contact_id}")
        print(f"Фамилия: {contact_info['last_name']}")
        print(f"Имя: {contact_info['first_name']}")
        print(f"Отчество: {contact_info['middle_name']}")
        print(f"Телефон: {contact_info['phone_number']}")
        print("-" * 20)

def save_to_txt(phonebook, filename):
    with open(filename, 'w') as file:
        for contact_id, contact_info in phonebook.items():
            file.write(f"{contact_id},{contact_info['last_name']},{contact_info['first_name']},{contact_info['middle_name']},{contact_info['phone_number']}\n")
    print("Данные сохранены в файл.")

def load_from_txt(filename):
    phonebook = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                contact_id, last_name, first_name, middle_name, phone_number = data
                phonebook[int(contact_id)] = {
                    'last_name': last_name,
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'phone_number': phone_number
                }
        print("Данные загружены из файла.")
        return phonebook
    except FileNotFoundError:
        print("Файл не найден.")
        return {}

def search_contact(phonebook, search_term):
    for cont_id, contact_info in phonebook.items():
        if (search_term.lower() in contact_info['last_name'].lower() or
            search_term.lower() in contact_info['first_name'].lower() or
            search_term.lower() in contact_info['middle_name'].lower() or
            search_term in contact_info['phone_number']):
            print(f"Найден контакт (ID: {cont_id}):")
            print(f"Фамилия: {contact_info['last_name']}")
            print(f"Имя: {contact_info['first_name']}")
            print(f"Отчество: {contact_info['middle_name']}")
            print(f"Телефон: {contact_info['phone_number']}")
            print("-" * 20)

def main():
    phonebook = {}
    filename = "phonebook.txt"

    try:
        phonebook = load_from_txt(filename)
    except Exception as e:
        print("Ошибка при загрузке данных:", e)

    while True:
        print("1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Поиск контакта")
        print("4. Сохранить данные в файл")
        print("5. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            add_contact(phonebook, last_name, first_name, middle_name, phone_number)

        elif choice == '2':
            display_contacts(phonebook)

        elif choice == '3':
            search_term = input("Введите строку для поиска: ")
            search_contact(phonebook, search_term)

        elif choice == '4':
            save_to_txt(phonebook, filename)

        elif choice == '5':
            print("Программа завершена.")
            break

if __name__ == "__main__":
    main()
