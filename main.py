def get_phone_book(file_name: str):
    with open(file_name, 'r') as file:
        phonebook_str = file.read().split()

    phonebook = []

    i = 0
    while i < len(phonebook_str) - 2:
        phonebook.append({'name': phonebook_str[i], 'surname': phonebook_str[i + 1], 'phone_num': phonebook_str[i + 2]})
        i += 3

    return phonebook


def read_phonebook(phonebook: list):
    print('Phonebook:')
    for i in phonebook:
        print(f'Full name {i['name'], i['surname']}, phone num: {i['phone_num']}')


def find_contact(phonebook: list):
    name = input('Enter the contact\'s name: ')
    surname = input('Enter the contact\'s surname: ')

    found = False
    if len(name) > 0 and len(surname) > 0:
        for i in phonebook:
            if i['name'] == name and i['surname'] == surname:
                print(f'Full name {i['name'], i['surname']}, phone num: {i['phone_num']}')
                return
    elif len(name) > 0 and len(surname) == 0:
        for i in phonebook:
            if i['name'] == name:
                print(f'Full name {i['name'], i['surname']}, phone num: {i['phone_num']}')
                found = True
    elif len(name) == 0 and len(surname) > 0:
        for i in phonebook:
            if i['surname'] == surname:
                print(f'Full name {i['name'], i['surname']}, phone num: {i['phone_num']}')
                found = True

    if not found:
        print('No records')


def add_contact(phonebook: list):
    name = input('Enter the name of the new contact: ')
    surname = input('Enter the surname of the new contact: ')
    phone_num = input('Enter the phone_num of the new contact: ')

    phonebook.append({'name': name, 'surname': surname, 'phone_num': phone_num})

    return phonebook


def change_contact(phonebook: list):
    name = input('Enter the contact\'s name: ')
    surname = input('Enter the contact\'s surname: ')

    for i in phonebook:
        if i['name'] == name and i['surname'] == surname:
            new_name = input('New name:')
            new_surname = input('New surname:')
            phone_num = input('New phone number: ')
            if len(new_name) > 0:
                i['name'] = new_name
                print('Name changed')
            if len(new_surname) > 0:
                i['surname'] = new_name
                print('Surname changed')
            if len(phone_num) > 0:
                i['phone_num'] = phone_num
            return phonebook

    print('No records')
    return phonebook


def save_file(phonebook: list, old_file: str):
    with open(old_file, 'w') as file:
        for i in phonebook:
            file.write(f'{i['name']} {i['surname']} {i['phone_num']}\n')


def change_input_file(phonebook: list, old_file: str):
    new_file = input('New file: ')

    save_file(phonebook, old_file)

    phonebook = get_phone_book(new_file)

    return phonebook, new_file


def delete_contact(phonebook: list):
    name = input('Enter the contact\'s name: ')
    surname = input('Enter the contact\'s surname: ')

    for i in phonebook:
        if i['name'] == name and i['surname'] == surname:
            phonebook.remove(i)
            return phonebook

    print('No records')
    return phonebook


def main():
    file_name: str = input('Enter phonebook file name: ')
    phonebook = get_phone_book(file_name)

    while True:
        print('',
              '1. Read phonebook\n',
              '2. Find contact\n',
              '3. Add contact\n',
              '4. Change contact\n',
              '5. Change input file\n',
              '6. Delete contact\n',
              '7. Exit\n'
              )
        try:
            num = int(input('Enter number: '))
        except ValueError:
            num = -1

        if num == 1:
            read_phonebook(phonebook)
        elif num == 2:
            find_contact(phonebook)
        elif num == 3:
            add_contact(phonebook)
        elif num == 4:
            phonebook = change_contact(phonebook)
        elif num == 5:
            phonebook, file_name = change_input_file(phonebook, file_name)
        elif num == 6:
            phonebook = delete_contact(phonebook)
        elif num == 7:
            save_file(phonebook, file_name)
            break
        else:
            print('WRONG NUMBER')

        print('*********************************\n\n')


if __name__ == '__main__':
    main()
