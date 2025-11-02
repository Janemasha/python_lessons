def menu():
    choice = input('Enter task number from 1 to 5: ')
    while not (choice.isdigit() and 1 <= int(choice) <= 5):
        print('Your choice is incorrect, try again')
        choice = input('Enter task number from 1 to 5: ')
    choice_int = int(choice)
    match choice_int:

        case 1:
            soda_taste = Soda()
            soda_taste.taste = input('Enter taste of soda: ')
            print(soda_taste)

        case 2:
            calc = Math()
            action = calc.enter_action()
            number_a = calc.enter_number('A')
            number_b = calc.enter_number('B')

            match action:
                case 0:
                    calc.addition(number_a=number_a, number_b=number_b)
                case 1:
                    calc.substraction(number_a=number_a, number_b=number_b)
                case 2:
                    calc.multiplication(number_a=number_a, number_b=number_b)
                case 3:
                    calc.division(number_a=number_a, number_b=number_b)


class Soda:

    def __init__(self, taste='regular'):
        self.taste = taste

    def __str__(self):
        if self.taste == '':
            return f'You have regular soda'
        else:
            return f'You have {self.taste} soda'


class Math:

    def addition(self, number_a, number_b):
        print(f'{number_a} + {number_b} = {number_a + number_b}')

    def substraction(self, number_a, number_b):
        print(f'{number_a} - {number_b} = {number_a - number_b}')

    def multiplication(self, number_a, number_b):
        print(f'{number_a} * {number_b} = {number_a * number_b}')

    def division(self, number_a, number_b):
        try:
            print(f'{number_a} / {number_b} = {number_a / number_b}')
        except ZeroDivisionError:
            print('You can not divide by zero')

    def enter_number(self, order):
        choice = input(f'Enter an integer {order}: ')
        while not (choice.isdigit()):
            print('Your choice is incorrect, try again')
            choice = input(f'Enter an integer {order}: ')
        return int(choice)

    def enter_action(self):
        choice = input('Select action:\n'
                       '0 - addition\n'
                       '1 - subtraction\n'
                       '2 - multiplication\n'
                       '3 - division\n'
                       'Your choice: ')
        while not (choice.isdigit()):
            print('Your choice is incorrect, try again')
            choice = input('Enter an integer: ')
        return int(choice)


menu()