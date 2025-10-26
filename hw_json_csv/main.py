import json
import os
import datetime
import csv

def prepare_content_from_json_to_scv(file_name):
    with open(file_name, 'r') as file:
        file_content = json.load(file)
        csv_header = []
        csv_file_content = []
        for item in file_content: #На случай, если в json будет не одинаковая структура данных для каждого элемента
            person_data = item
            for key in person_data:
                if key not in csv_header:
                    csv_header.append(key)
        for item in file_content:
            person_data = item
            scv_row = []
            for header_item in csv_header:
                if header_item in list(person_data.keys()):
                    scv_row.append(person_data[header_item])
                else:
                    scv_row.append(' ')
            csv_file_content.append(scv_row)
        return csv_header, csv_file_content


def write_to_csv(headers, content):
    with open("new_csv.csv", 'w') as csv_file:
        csv_content = csv.writer(csv_file)
        csv_content.writerow(headers)
        csv_content.writerows(content)


def enter_name():
    name = input('Enter name of person: ')
    return name


def enter_birthday():
    is_birthday_correct = False
    birthday = ''
    while not is_birthday_correct:
        try:
            birthday = input('Enter day of birth in format: dd.mm.yyyy: ')
            birthday_date = datetime.datetime.strptime(birthday, '%d.%m.%Y')
            is_birthday_correct = True
        except Exception:
            is_birthday_correct = False
            print('Day of birth is incorrect, try again')
    return birthday


def enter_height():
    height = ''
    is_height_correct = False
    while not is_height_correct:
        try:
            height = input('Enter height in sm: ')
            height_sm = float(height)
            is_height_correct = True
            print(height_sm)
        except ValueError:
            is_height_correct = False
            print('Height is incorrect, try again')
    return height


def enter_weight():
    weight = ''
    is_weight_correct = False
    while not is_weight_correct:
        try:
            weight = input('Enter weight in kg: ')
            weight_kg = float(weight)
            is_weight_correct = True
        except ValueError:
            is_weight_correct = False
            print('Weight is incorrect, try again')
    return weight


def enter_car():
    is_car = False
    is_car_correct = False
    while not is_car_correct:
        car = input('Has a person got a car?\nEnter:\n 1 - if "YES"\n 0 - if "NO"\n Your choice: ')
        if car == '1':
            is_car = True
            is_car_correct = True
        elif car == '0':
            is_car = False
            is_car_correct = True
        else:
            is_car_correct = False
            print('Your answer is incorrect, try again')
    return is_car


def enter_languages():
    languages_dict = {0: 'Another', 1: 'C', 2: 'C++', 3: 'Delphi', 4: 'C#', 5: 'Python'}
    is_correct_languages = False
    languages_lst = []
    while not is_correct_languages:
        print('Enter the programming languages from list, if there are several, use "," as a separator')
        for key in languages_dict.keys():
            print(f'{key} - {languages_dict[key]}')
        languages = input('Your choice (number): ')
        languages_str = languages.replace(' ', '')
        languages_number_lst = languages_str.split(',')
        try:
            is_numbers_in_range = True
            for number in languages_number_lst:
                number_int = int(number)
                if 0 <= number_int < len(languages_dict):
                    languages_lst.append(languages_dict[number_int])
                else:
                    is_numbers_in_range = False
            if not is_numbers_in_range == True:
                print(f'Yor choice is incorrect. You need to enter from 0 to {len(languages_dict) - 1}')
                languages_lst = []
            else:
                is_correct_languages = True
        except ValueError:
            is_correct_languages = False
            print('Yor choice is incorrect. You need to enter numbers')
            languages_lst = []
    return languages_lst


def new_data_input_json():
    data_for_json_dict = {'name': enter_name(), 'birthday': enter_birthday(), 'height': enter_height(),
                          'weight': enter_weight(), 'car': enter_car(), 'languages': enter_languages()}
    return data_for_json_dict


def write_new_data_json(json_file, data):
    file_content = []
    with open(json_file, 'r') as json_read_file:
        file_content = json.load(json_read_file)
        file_content.append(data)
        with open(json_file, 'w') as json_write_file:
            json.dump(file_content, json_write_file, indent=4)


def write_new_data_csv(data):
    prepared_headers, prepared_content = prepare_content_from_json_to_scv('employees.json')
    write_to_csv(prepared_headers, prepared_content)
    with open('new_csv.csv', 'a', newline='') as csv_file:
        csv_write = csv.DictWriter(csv_file, fieldnames=['name', 'birthday', 'height', 'weight', 'car', 'languages'])
        csv_write.writerow(data)


def find_information_by_name(file_name):
    with open(file_name, 'r') as file:
        file_content = json.load(file)
        names = []
        for person_data in file_content:
            names.append(person_data['name'])
        names_str = ', '.join(names)
        is_correct_name = False
        search_name = ''
        while not is_correct_name:
            search_name = input(f'Enter name or part of name from list: {names_str}')
            search_name_lower = search_name.lower()
            if search_name_lower in names_str.lower():
                is_correct_name = True
            else:
                print('This name or part of name is not found in list')
        return_data = []
        for person_data in file_content:
            is_search_item = False
            value_lower = person_data['name'].lower()
            if search_name_lower in value_lower:
                is_search_item = True
                return_data.append(person_data)
    return return_data


def print_information_str(data_list):
    print_lst = []
    for item in data_list:
        print_item_lst = []
        for key in item.keys():
            if isinstance(item[key], list):
                print_item_lst.append(f'{key}: {', '.join(item[key])}')
            else:
                print_item_lst.append(f'{key}: {item[key]}')
        print_item_lst = '; '.join(print_item_lst)
        print_lst.append(print_item_lst)
    print(f'Your list of employees:\n{'\n'.join(print_lst)}')


def find_information_by_language(file_name):
    with open(file_name, 'r') as file:
        file_content = json.load(file)
        languages = ['Another', 'C', 'C++', 'Delphi', 'C#', 'Python']
        languages_str = ', '.join(languages)
        is_correct_language = False
        search_language = ''
        while not is_correct_language:
            search_language = input(f'Enter language from list: {languages_str}')
            search_language_lower = search_language.lower()
            for language in languages:
                if search_language_lower == language.lower():
                    is_correct_language = True
            if not is_correct_language:
                print('This language is not found in list')
        return_data = []
        for person_data in file_content:
            for item in person_data['languages']:
                if search_language_lower == item.lower():
                    return_data.append(person_data['name'])
        print(f'List of employees with knowledge of {search_language}:\n{', '.join(return_data)}')
    return ', '.join(return_data)


def find_by_year(file_name):
    with open(file_name, 'r') as file:
        file_content = json.load(file)
        is_year_correct = False
        while not is_year_correct:
            try:
                search_year = input('Enter the year for filter: ')
                search_year_int = int(search_year)
                height_sum = 0
                for item in file_content:
                    birthday = item['birthday']
                    year_of_birth = int(birthday[-4:])
                    if year_of_birth < search_year_int:
                        height_sum += float(item['height'])
                        is_year_correct = True
                if height_sum == 0:
                    print(f'There are not employees with year of birth lower than {search_year}')
                else:
                    print(f'Sum of height of employees with year of birth lower than {search_year} is {height_sum}')
            except ValueError:
                print('Year must be a number, try again')


def start_work():
    user_start_work = input('Enter:\n'
                            '1 - If you want to start or continue to work with program\n'
                            '0 - If you want to stop program:\n'
                            'Your choice: ')
    is_user_start_work = False
    while not is_user_start_work:
        try:
            user_choice = int(user_start_work)
            if user_choice == 1:
                choice_function()
                is_user_start_work = True
            elif user_choice == 0:
                print('Work of program is stopped')
                is_user_start_work = True
            else:
                print('Your choice is unknown')
        except ValueError:
            print('Your choice must be a number')


def choice_function():
    is_user_start_work = False
    while not is_user_start_work:
        user_choice = input('Enter number of task:\n'
                            '0 - If you want to write data from json to csv file\n'
                            '1 - If you want to add information in json file\n'
                            '2 - If you want to add information in csv file\n'
                            '3 - If you want to find information about employee by name or a part of name\n'
                            '4 - If you want to get a list of employees with knowledge of a certain language\n'
                            '5 - If you want to get a sum of heights of employees with year of birth lower than your choice\n'
                            'Make your choice: ')
        try:
            user_choice_int = int(user_choice)
            if 0 <= user_choice_int <= 5:
                is_user_start_work = True
                match user_choice_int:
                    case 0:
                        prepared_headers, prepared_content = prepare_content_from_json_to_scv('employees.json')
                        write_to_csv(prepared_headers, prepared_content)
                        print('Data from employees.json is written to csv file (new_csv.csv)')
                    case 1:
                        data_for_writing = new_data_input_json()
                        write_new_data_json('employees.json', data_for_writing)
                        print('Your data is added to employees.json')
                    case 2:
                        data_for_writing = new_data_input_json()
                        write_new_data_csv(data_for_writing)
                        print('Your data is added to employees.json')
                    case 3:
                        find_by_name_list = find_information_by_name('employees.json')
                        print_information_str(find_by_name_list)
                        print('Your data is added to new_csv.csv')
                    case 4:
                        find_information_by_language('employees.json')
                    case 5:
                        find_by_year('employees.json')
            else:
                print('Your choice is incorrect, try again')
        except ValueError:
            print('Your choice is incorrect, try again')
    start_work()


start_work()