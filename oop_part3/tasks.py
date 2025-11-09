import copy

def fibonacci_gen(finish):
    start = 0
    first_number = 0
    second_number = 1
    while start <= finish:
        yield first_number
        first_sub_number = copy.copy(second_number)
        second_number = first_number + second_number
        first_number = first_sub_number
        start += 1


def fibonacci(finish):
    fibonacci_numbers = fibonacci_gen(finish)
    fibonacci_lst = []
    for number in fibonacci_numbers:
        fibonacci_lst.append(number)
    return fibonacci_lst


def prepare_cycle_lst(finish):
    cycle_numbers = cyclic_sequence(finish)
    cycle_lst = []
    for number in cycle_numbers:
        cycle_lst.append(number)
    return cycle_lst


def user_number(task_name):
    is_user_number_correct = False
    user_number_fib = 0
    while not is_user_number_correct:
        user_number_str = input(f'Lets generate a list of {task_name} numbers.\nEnter the number you want to extract from the list from 1: ')
        try:
            user_number_int = int(user_number_str)
            if user_number_int > 0:
                is_user_number_correct = True
                user_number_fib = user_number_int
            else:
                print('Number must be more then 0, try again')
        except TypeError:
            print('You need to enter an integer, try again')
    return user_number_fib - 1


def cyclic_sequence(finish):
    start_number = 0
    previous_number = 1
    while start_number <= finish:
        yield previous_number
        if previous_number < 3:
            next_number = previous_number + 1
        else:
            next_number = 1
        previous_number = next_number
        start_number += 1



def menu():
    choice = input('Select task to see:\n'
                   '0 - Fibonacci list\n'
                   '1 - Cyclic sequence\n'
                   '2 - pattern builder\n'
                   '3 - pattern factory method\n'
                   '4 - pattern strategy\n'
                   'Your choice: ')
    while not (choice.isdigit() and 0 <= int(choice) <= 4):
        print('Your choice is incorrect, try again')
        choice = input('Select task to see:\n'
                        '0 - Fibonacci list\n'
                        '1 - Cyclic sequence\n'
                        '2 - pattern builder\n'
                        '3 - pattern factory method\n'
                        '4 - pattern strategy\n'
                        'Your choice: ')
    choice_int = int(choice)
    match choice_int:
        case 0:
            finish_number = user_number('Fibonacci')
            fibonacci_numbers_lst = fibonacci(finish_number)
            fibonacci_str = map(str, fibonacci_numbers_lst)
            print(f' Your Fibonacci list is: {', '.join(fibonacci_str)}')
        case 1:
            cycle = prepare_cycle_lst(user_number('Cycle'))
            cycle_str = map(str, cycle)
            print(f' Your cycle list is: {', '.join(cycle_str)}')
        case 2:
            print()
        case 3:
            print()
        case 4:
            print()


menu()

