import copy
from abc import ABC, abstractmethod
from operator import truediv


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
        except ValueError:
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


def get_pizza_size():
    is_right_choice = False
    user_choice = ''
    while not is_right_choice:
        user_choice_str = input(f'What size of pizza do you want?\n'
                                '0 - Small\n'
                                '1 - Medium\n'
                                '2 - Large\n'
                                '3 - Extra large\n'
                                'Your answer: ')
        try:
            user_choice_int = int(user_choice_str)
            if user_choice_int == 0:
                user_choice = 'Small'
                is_right_choice = True
            elif user_choice_int == 1:
                user_choice = 'Medium'
                is_right_choice = True
            elif user_choice_int == 2:
                user_choice = 'Large'
                is_right_choice = True
            elif user_choice_int == 3:
                user_choice = 'Extra large'
                is_right_choice = True
            else:
                print('Your choice must be a number from 0 to 3, try again')
        except ValueError:
            print('Your choice must be a number, try again')
    return user_choice


def animal_choice():
    is_right_choice = False
    user_choice = ''
    while not is_right_choice:
        user_choice_str = input(f'What animal do you choose?\n'
                                '0 - Cat\n'
                                '1 - Dog\n'
                                'Yor choice: ')
        if user_choice_str == '0':
            user_choice = 'Cat'
            is_right_choice = True
        elif user_choice_str == '1':
            user_choice = 'Dog'
            is_right_choice = True
        else:
            print('Unknown animal')
    return user_choice


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
            director = PizzaDirector()
            builder = PizzaBuilder()
            director.set_pizza_builder(builder)
            director.make_pizza()
            my_pizza = builder.get_pizza()
            print(f'Your pizza:\n{my_pizza}')
        case 3:
            animal_creator = AnimalFactory()
            animal_name = animal_choice()
            animal = animal_creator.create_animal(animal_name)
            print(f'{animal_name} says {animal.speak()}')
        case 4:
            option = Calculator()
            result = option.calculate()
            print(f'Your result: {result}')


def check_choice():
    is_right_choice = False
    user_choice = []
    while not is_right_choice:
        user_choice_str = input(f'Do you want to add to your pizza? Use "," to split values\n'
                                '0 - Cheese\n'
                                '1 - Pepperoni\n'
                                '2 - Mushrooms\n'
                                '3 - Onions\n'
                                '4 - Bacon\n'
                                'Your answer: ')
        user_choice_str.replace(' ', '')
        user_lst = user_choice_str.split(',')
        right_values_counter = 0
        for ingredient in user_lst:
            try:
                ingredient_int = int(ingredient)
                if 0 <= ingredient_int <= 4:
                    right_values_counter += 1
                    user_choice.append(ingredient_int)
                else:
                    print(f'{ingredient} is not a number from 0 to 4')
            except ValueError:
                print(f'{ingredient} is not a number')
        if right_values_counter == len(user_lst):
            is_right_choice = True
    return user_choice


class Pizza:

    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        pizza_ingredients = []
        if self.cheese:
            pizza_ingredients.append('cheese')
        if self.pepperoni:
            pizza_ingredients.append('pepperoni')
        if self.mushrooms:
            pizza_ingredients.append('mushrooms')
        if self.onions:
            pizza_ingredients.append('onions')
        if self.bacon:
            pizza_ingredients.append('bacon')
        return (f'Size: {self.size}\n'
                f'Ingredients: {', '.join(pizza_ingredients)}')


class PizzaBuilder:

    def __init__(self):
        self.pizza = Pizza()


    def set_size(self):
        self.pizza.size = get_pizza_size()


    def add_cheese(self):
        self.pizza.cheese = True


    def add_pepperoni(self):
        self.pizza.pepperoni = True


    def add_mushrooms(self):
        self.pizza.mushrooms = True


    def add_onions(self):
        self.pizza.onions = True


    def add_bacon(self):
        self.pizza.bacon = True


    def get_pizza(self):
        return self.pizza


class PizzaDirector:

    def __init__(self):
        self.builder = None


    def set_pizza_builder(self, builder):
        self.builder = builder


    def make_pizza(self):
        if not self.builder:
            raise ValueError('We do not have builder')
        self.builder.set_size()
        ingredients_lst = check_choice()
        for ingredient in ingredients_lst:
            match ingredient:
                case 0:
                    self.builder.add_cheese()
                case 1:
                    self.builder.add_pepperoni()
                case 2:
                    self.builder.add_mushrooms()
                case 3:
                    self.builder.add_onions()
                case 4:
                    self.builder.add_bacon()

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Cat(Animal):

    def speak(self):
        return 'Mew'


class Dog(Animal):

    def speak(self):
        return 'Woof'


class AnimalFactory:

    @classmethod
    def create_animal(cls, animal_type):
        animals = {
            'cat': Cat(),
            'dog': Dog()
        }
        try:
            return animals[animal_type.lower()]
        except KeyError:
            print('We do not have such an animal')


class Calculator:

    def __init__(self):
        self.strategy = None
        self.strategy_obj = None


    def set_strategy(self):
        right_strategy = False
        while not right_strategy:
            user_strategy = input('Chose operation to do:\n'
                                  '0 - Addition\n'
                                  '1 - Substraction\n'
                                  '2 - Multiplication\n'
                                  '3 - Division\n'
                                  'Your choice: ')
            try:
                user_strategy_int = int(user_strategy)
                if 0 <= user_strategy_int <= 3:
                    self.strategy = int(user_strategy)
                    right_strategy = True
                    match self.strategy:
                        case 0:
                            self.strategy_obj = Addition()
                        case 1:
                            self.strategy_obj = Substraction()
                        case 2:
                            self.strategy_obj = Multiplication()
                        case 3:
                            self.strategy_obj = Division()
                else:
                    print('Yor choice must be from 0 to 3')
            except ValueError:
                print('Your choice must be an integer')


    @staticmethod
    def set_user_numbers(number_variant):
        is_right_number = False
        user_number_float = 0
        while not is_right_number:
            user_number_str = input(f'Enter your {number_variant}: ')
            try:
                user_number_float = float(user_number_str)
                is_right_number = True
            except ValueError:
                print('Your number must have type INT or FLOAT, please, try again')
        return user_number_float


    def calculate(self):
        self.set_strategy()
        number_a = self.set_user_numbers('Number A')
        number_b = self.set_user_numbers('Number B')
        return self.strategy_obj.execute(number_a, number_b)


class Addition:

    @staticmethod
    def execute(number_a, number_b):
        return number_a + number_b


class Substraction:

    @staticmethod
    def execute(number_a, number_b):
        return number_a - number_b


class Multiplication:

    @staticmethod
    def execute(number_a, number_b):
        return number_a * number_b


class Division:

    @staticmethod
    def execute(number_a, number_b):
        return number_a / number_b


menu()


