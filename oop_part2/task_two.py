class BeeElephant:

    def __init__(self):
        self.__bee = None
        self.__elephant = None


    def info_setter(self):
        return {'bee': self.__bee, 'elephant': self.__elephant}

    def __str__(self):
        return f'Bee: {self.__bee}, Elephant: {self.__elephant}'

    def info_getter(self, bee, elephant):
        if isinstance(bee, int):
            self.__bee = bee
        else:
            raise TypeError('Bee must be integer')
        if isinstance(elephant, int):
            self.__elephant = elephant
        else:
            raise TypeError('Elephant must be integer')


    def fly(self):
        if self.__bee >= self.__elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.__elephant >= self.__bee:
            return 'to-to-doo-doo'
        else:
            return 'wzzzz'


    def eat(self, meal, value):
        if isinstance(value, int):
            if value >= 0:
                if meal == 'nectar':
                    if self.__elephant - value >= 0:
                        self.__elephant -= value
                    else:
                        self.__elephant = 0
                    if self.__bee + value <= 100:
                        self.__bee += value
                    else:
                        self.__bee = 100
                elif meal == 'grass':
                    if self.__bee - value >= 0:
                        self.__bee -= value
                    else:
                        self.__bee = 0
                    if self.__elephant + value <= 100:
                        self.__elephant += value
                    else:
                        self.__elephant = 100
                else:
                    raise ValueError('Meal must be nectar or grass')
            else:
                raise ValueError('Value must be positive number')
        else:
            raise TypeError('Value must be an integer')

    @staticmethod
    def check_numbers(number_str):
        try:
            number = int(number_str)
            if 0 <= number <= 100:
                return [True, number]
            else:
                return [False]
        except ValueError:
            return [False]

    @staticmethod
    def right_user_data(animal_type):
        is_right_data = False
        user_int = 0
        while not is_right_data:
            user_str = input(f'Enter an integer from 0 to 100 for {animal_type}: ')
            user_str_checked = BeeElephant.check_numbers(user_str)
            if not user_str_checked[0] == False:
                user_int = user_str_checked[1]
                is_right_data = True
            else:
                print('Your data is incorrect. Please, try again')
        return user_int

    @staticmethod
    def nectar_or_grass_input():
        is_right_choice = False
        user_choice = ''
        while not is_right_choice:
            user_str = input('Lets try to feed bee or elephant. Enter:\n'
                             '0 - to choose Nectar to feed a BEE\n'
                             '1 - to choose Grass to feed an ELEPHANT\n'
                             'Your choice: ')
            try:
                user_int = int(user_str)
                if user_int == 0:
                    user_choice = 'nectar'
                    is_right_choice = True
                elif user_int == 1:
                    user_choice = 'grass'
                    is_right_choice = True
                else:
                    print('Number must be 0 or 1. Please, try again')
            except Exception:
                print('Your data must be an integer, try again')
        return user_choice

bee_elephant_obj = BeeElephant()

user_bee_int = bee_elephant_obj.right_user_data('BEE')
user_elephant_int = bee_elephant_obj.right_user_data('ELEPHANT')

bee_elephant_obj.info_getter(bee=user_bee_int, elephant=user_elephant_int)

print(f'Great! Your data:\n {bee_elephant_obj}')

if bee_elephant_obj.fly():
    print('Part BEE is NOT less than part ELEPHANT')
else:
    print('Part BEE is less than part ELEPHANT')

print(bee_elephant_obj.trumpet())

user_meal = bee_elephant_obj.nectar_or_grass_input()
user_value = bee_elephant_obj.right_user_data(user_meal)

bee_elephant_obj.eat(meal=user_meal, value=user_value)

print(f'Data after feeding: {bee_elephant_obj}')

