import math

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
        case 3:
            car_name = input('Enter name of car: ')
            car_color = input('Enter color of car: ')
            car_type = input('Enter type of car: ')
            car_year = input('Enter year of manufacture of car: ')
            your_car = Car(name=car_name, color=car_color, type=car_type, year=car_year)
            your_car.engine_started()
            your_car.engine_stopped()
            your_car.info()

        case 4:
            sphere_radius = enter_radius('radius of sphere')
            coord_x = correct_number('x-coordinate of center')
            coord_y = correct_number('y-coordinate of center')
            coord_z = correct_number('z-coordinate of center')
            my_sphere = constructor(sphere_radius, coord_x, coord_y, coord_z)
            print(f'Volume of sphere is {my_sphere.get_volume()}')
            print(f'Square of sphere is {my_sphere.get_square()}')
            print(f'Radius of sphere is {my_sphere.get_radius()}')
            print(f'Center of sphere has coordinates {my_sphere.get_center()}')
            new_radius = enter_radius('new radius of sphere')
            my_sphere.set_radius(new_radius)
            print(f'New radius of sphere is {my_sphere.get_radius()}')
            new_coord_x = correct_number('new x-coordinate of center')
            new_coord_y = correct_number('new y-coordinate of center')
            new_coord_z = correct_number('new z-coordinate of center')
            my_sphere.set_center(new_coord_x, new_coord_y, new_coord_z)
            print(f'Center of sphere has new coordinates {my_sphere.get_center()}')
            point_coord_x = correct_number('x-coordinate of point')
            point_coord_y = correct_number('y-coordinate of point')
            point_coord_z = correct_number('z-coordinate of point')
            if my_sphere.is_point_inside(point_coord_x, point_coord_y, point_coord_z):
                print(f'Point {(point_coord_x, point_coord_y, point_coord_z)} is in sphere')
            else:
                print(f'Point {(point_coord_x, point_coord_y, point_coord_z)} NOT is in sphere')
        case 5:
            str_one = SuperStr('kgkgkgkg')
            repeat_str = 'kgkg'
            if str_one.is_repeatance(repeat_str):
                print(f'String {str_one} is created by repeating string {repeat_str}')
            else:
                print(f'String {str_one} is NOT created by repeating string {repeat_str}')

            str_two = SuperStr('mama')
            if str_two.is_palindrom():
                print(f'{str_two} is palindrome')
            else:
                print(f'{str_two} is NOT palindrome')


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


class Car:

    def __init__(self, name, color, type, year):  # Добавила name, показлось лоличным
        self.name = name
        self.color = color
        self.type = type
        self.year = year


    def engine_started(self):
        print(f'The car {self.name} is started')


    def engine_stopped(self):
        print(f'The car {self.name} turned off')


    def info(self):
        print(f'Your car name: {self.name},\n'
              f'color: {self.color}\n'
              f'type: {self.type}\n'
              f'year: {self.year}')


class Sphere:

    def __init__(self, radius, x, y, z):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z


    def get_volume(self):
        volume = 4 / 3 * math.pi * self.radius * self.radius * self.radius
        return volume


    def get_square(self):
        square = 4 * math.pi * self.radius * self.radius
        return square


    def get_radius(self):
        return self.radius



    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_center(self):
        center = (self.x, self.y, self.z)
        return center

    def set_center(self, new_x, new_y, new_z):
        self.x = new_x
        self.y = new_y
        self.z = new_z


    def is_point_inside(self, point_x, point_y, point_z):
        wide_coord_x = [self.x - self.radius, self.x + self.radius]
        wide_coord_y = [self.y - self.radius, self.y + self.radius]
        wide_coord_z = [self.z - self.radius, self.z + self.radius]
        if wide_coord_x[0] <= point_x <= wide_coord_x[1] and wide_coord_y[0] <= point_y <= wide_coord_y[1] and wide_coord_z[0] <= point_z <= wide_coord_z[1]:
            return True
        else:
            return False


class SuperStr(str):

    def is_repeatance(self, s):
        if len(self) % len(s) == 0:
            repeated_str = s * (len(str(self)) // len(s))
            return repeated_str == str(self)
        else:
            return False


    def is_palindrom(self):
        reverse_string = self[::-1]
        if reverse_string == self:
            return True
        else:
            return False


def constructor(radius=1.0, x=0.0, y=0.0, z=0.0):
    try:
        return Sphere(radius=float(radius), x=float(x), y=float(y), z=float(z))
    except ValueError:
        print('All parameters must be numbers')


def correct_number(data_type):
    choice = input(f'Enter {data_type}: ')
    is_choice_number = False
    while not is_choice_number:
        try:
            choice_number = float(choice)
            is_choice_number = True
        except ValueError:
            print('Your choice is incorrect, try again')
            choice = input(f'Enter an integer {data_type}: ')
    return float(choice)


def enter_radius(data_type):
    choice = input(f'Enter {data_type}: ')
    is_choice_number = False
    while not is_choice_number:
        try:
            choice_number = float(choice)
            if choice_number > 0:
                is_choice_number = True
            else:
                print(f'Your choice is incorrect, {data_type} must be positive')
                choice = input(f'Enter an integer {data_type}: ')
        except ValueError:
            print('Your choice is incorrect, try again')
            choice = input(f'Enter an integer {data_type}: ')
    return float(choice)


menu()
