import os
import platform
import shutil
from copy import copy
import re


def dir_sort_files_by_type():
    dir_contain_lst = os.listdir()
    files_lst = list(filter(lambda item: os.path.isfile(item), dir_contain_lst))
    dir_file_count = {}
    dir_file_memory = {}
    dir_file_dict = {}
    if not files_lst == []:
        for file in files_lst:
            if not file == os.path.basename(__file__):
                file_type_list = file.split('.')
                dir_file_dict[file_type_list[0]] = file_type_list[1]
                if len(file_type_list) == 2:
                    try:
                        if os.path.isdir(file_type_list[1]) and file_type_list[1] in dir_file_count:
                            file_size = os.path.getsize(file)
                            shutil.move(file, file_type_list[1])
                            dir_name = copy(file_type_list[1])
                            counter = int(copy((dir_file_count[dir_name])))
                            counter += 1
                            dir_file_count[file_type_list[1]] = str(counter)
                            memory = float(dir_file_memory[file_type_list[1]])
                            dir_file_memory[file_type_list[1]] = memory + file_size
                        elif os.path.isdir(file_type_list[1]) and not (file_type_list[1] in dir_file_count):
                            file_size = os.path.getsize(file)
                            shutil.move(file, file_type_list[1])
                            dir_file_count[file_type_list[1]] = 1
                            dir_file_memory[file_type_list[1]] = file_size
                        else:
                            file_size = os.path.getsize(file)
                            os.mkdir(file_type_list[1])
                            shutil.move(file, file_type_list[1])
                            dir_file_count[file_type_list[1]] = 1
                            dir_file_memory[file_type_list[1]] = file_size
                    except IndexError:
                        print(f'{file} not a file')
                else:
                    print(f'{file} not a file')
        dir_file_count_keys = list(dir_file_count.keys())
        dir_file_count_values = list(dir_file_count.values())
        for key in dir_file_count_keys:
            print(f'In direction {key} {dir_file_count[key]} file / files are added, they takes {dir_file_memory[key]}B')
        dir_file_dict_keys = list(dir_file_dict.keys())
        dir_file_dict_values = list(dir_file_dict.values())
        old_name = os.path.join(dir_file_dict_values[0], f'{dir_file_dict_keys[0]}.{dir_file_dict_values[0]}')
        new_name = os.path.join(dir_file_dict_values[0], f'new_{dir_file_dict_keys[0]}.{dir_file_dict_values[0]}')
        os.rename(old_name, new_name)
        print(f'File {old_name} is renamed in {new_name}')
    else:
        print(f'No files in directory')


def name_change(text, full_name):
    title_full_name = full_name.title()
    new_text = text.replace(title_full_name, 'N')
    if new_text != text:
        print(f'Your text without full name:\n{new_text}')
    else:
        print(f'Name {full_name} is not found in text: {text}')


def data_replace(file_name, prepared_stop_words_dict):
    prepared_stop_words_list = prepared_stop_words_dict.keys()
    with open(file_name, 'r') as file:
        file_content = str(file.read())
        with open(file_name, 'w') as write_file:
            for item in prepared_stop_words_list:
                file_content = re.sub(f'{item}', f'{prepared_stop_words_dict[item]}', file_content)
            write_file.write(file_content)


def stop_words_list():
    with open('stop_words.txt', 'r') as file:
        file_content = str(file.read())
        words_list = file_content.split(' ')
        return words_list


def stop_words_re_prepared(some_list):
    re_prepared_dict = {}
    for word in some_list:
        re_prepared_word_list = []
        replace_symbols_list = []
        for letter in word:
            re_letter = f'[{letter.lower()}{letter.upper()}]'
            re_prepared_word_list.append(re_letter)
            replace_symbols_list.append('*')
        re_prepared_word_str = ''.join(re_prepared_word_list)
        replace_symbols_str = ''.join(replace_symbols_list)
        re_prepared_dict[re_prepared_word_str] = replace_symbols_str
    return re_prepared_dict


def low_scores(file_name):
    with open(file_name, 'r') as file:
        file_content = str(file.read())
        file_content_list = file_content.split('\n')
        person_score_dict = {}
        for item in file_content_list:
            item_list = item.split(' ')
            score = item_list.pop(len(item_list) - 1)
            person_score_dict[' '.join(item_list)] = score
        bad_students_list = list(filter(lambda key: float(person_score_dict[key]) <= 3, person_score_dict))
        return bad_students_list


def filtered_numbers_sum(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
        numbers_list = re.findall(r'\d+', file_content)
        numbers_sum = 0
        for number in numbers_list:
            numbers_sum += int(number)
        return numbers_sum


def caesar_cipher(some_str, number, cipher):
    eng_alph_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    eng_alph_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_alph_lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    rus_alph_uppercase = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    new_str_lst = []
    if cipher == 1:
        for j in range(len(some_str)):
            some_str_j_index = 0
            if 'A' <= some_str[j] <= 'Z':
                for b in range(len(eng_alph_uppercase)):
                    if some_str[j] == eng_alph_uppercase[b]:
                        some_str_j_index = b
                        break
                new_str_lst.append(eng_alph_uppercase[some_str_j_index + number - len(eng_alph_uppercase)])
            elif 'a' <= some_str[j] <= 'z':
                for b in range(len(eng_alph_lowercase)):
                    if some_str[j] == eng_alph_lowercase[b]:
                        some_str_j_index = b
                        break
                new_str_lst.append(eng_alph_lowercase[some_str_j_index + number - len(eng_alph_lowercase)])
            elif 'А' <= some_str[j] <= 'Я' or some_str[j] == 'Ё':
                for b in range(len(rus_alph_uppercase)):
                    if some_str[j] == rus_alph_uppercase[b]:
                        some_str_j_index = b
                        break
                new_str_lst.append(rus_alph_uppercase[some_str_j_index + number - len(rus_alph_uppercase)])
            elif 'а' <= some_str[j] <= 'я' or some_str[j] == 'ё':
                for b in range(len(rus_alph_lowercase)):
                    if some_str[j] == rus_alph_lowercase[b]:
                        some_str_j_index = b
                        break
                new_str_lst.append(rus_alph_lowercase[some_str_j_index + number - len(rus_alph_lowercase)])
            else:
                new_str_lst.append(some_str[j])
        return ''.join(new_str_lst)
    else:
        for j in range(len(some_str)):
            some_str_j_index = 0
            if 'A' <= some_str[j] <= 'Z':
                for b in range(len(eng_alph_uppercase)):
                    if some_str[j] == eng_alph_uppercase[b]:
                        some_str_j_index = b
                        break
                new_str_lst.append(eng_alph_uppercase[(some_str_j_index - number)])
            elif 'a' <= some_str[j] <= 'z':
                for b in range(len(eng_alph_lowercase)):
                    if some_str[j] == eng_alph_lowercase[b]:
                        some_str_j_index = b
                        break
                new_str_lst.append(eng_alph_lowercase[(some_str_j_index - number)])
            elif 'А' <= some_str[j] <= 'Я' or some_str[j] == 'Ё':
                for b in range(len(rus_alph_uppercase)):
                    if some_str[j] == rus_alph_uppercase[b]:
                        some_str_j_index = b
                        break
                new_str_lst.append(rus_alph_uppercase[(some_str_j_index - number)])
            elif 'а' <= some_str[j] <= 'я' or some_str[j] == 'ё':
                for b in range(len(rus_alph_lowercase)):
                    if some_str[j] == rus_alph_lowercase[b]:
                        some_str_j_index = b
                        break
                new_str_lst.append(rus_alph_lowercase[(some_str_j_index - number)])
            else:
                new_str_lst.append(some_str[j])
        return ''.join(new_str_lst)


def caesar_cipher_with_file(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
        file_content_list = file_content.split('\n')
        row_counter = 0
        cipher_str_list = []
        for row in file_content_list:
            row_counter += 1
            cipher_str_list.append(caesar_cipher(row, row_counter, 1))
        cipher_file_content = '\n'.join(cipher_str_list)
        with open(file_name, 'w') as write_file:
            write_file.write(cipher_file_content)


choice = input('Enter task number from 1 to 7: ')
while not (choice.isdigit() and 1 <= int(choice) <= 7):
    print('Your choice is incorrect, try again')
    choice = input('Enter task number from 1 to 7: ')
choice_int = int(choice)
match choice_int:
    case 1:
        print(f'Name of your OS is {platform.system()}\nLocation of current direction: {os.getcwd()}')
        dir_sort_files_by_type()
    case 2:
        judgment_text = input('Enter text of judgment: ')
        defendant_name = input('Enter full name of the defendant: ')
        name_change(judgment_text, defendant_name)
    case 3:
        print('Task 3 is removed from homework')
    case 4:
        file_path = input('Enter name of file: ')
        is_correct_file = False
        while not is_correct_file == True:
            if os.path.exists(file_path):
                is_correct_file = True
            else:
                file_path = input('Your file name is incorrect, enter name of file: ')
        stop_words = stop_words_list()
        prepared_stop_words = stop_words_re_prepared(stop_words)
        data_replace(file_path, prepared_stop_words)
    case 5:
        file_path = input('Enter name of file: ')
        is_correct_file = False
        while not is_correct_file == True:
            if os.path.exists(file_path):
                is_correct_file = True
            else:
                file_path = input('Your file name is incorrect, enter name of file: ')
        bad_students = low_scores(file_path)
        print(f'Students with scores lower than 3 are {', '.join(bad_students)}')
    case 6:
        file_path = input('Enter name of file: ')
        is_correct_file = False
        while not is_correct_file == True:
            if os.path.exists(file_path):
                is_correct_file = True
            else:
                file_path = input('Your file name is incorrect, enter name of file: ')
        print(f'Sum of numbers in text is {filtered_numbers_sum(file_path)}')
    case 7:
        file_path = input('Enter name of file: ')
        is_correct_file = False
        while not is_correct_file == True:
            if os.path.exists(file_path):
                is_correct_file = True
            else:
                file_path = input('Your file name is incorrect, enter name of file: ')
        caesar_cipher_with_file(file_path)
        print(f'The data in the file {file_path} is encrypted')