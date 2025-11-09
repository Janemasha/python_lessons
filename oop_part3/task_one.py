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

def user_number():
    is_user_number_correct = False
    user_number_fib = 0
    while not is_user_number_correct:
        user_number_str = input('Lets generate a list of Fibonacci numbers.\nEnter the number you want to extract from the list from 1: ')
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

finish_number = user_number()
fibonacci_numbers_lst = fibonacci(finish_number)
fibonacci_str = map(str, fibonacci_numbers_lst)
print(f' Your Fibonacci list is: {', '.join(fibonacci_str)}')