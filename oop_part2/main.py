class Product:

    all_products = []

    def __init__(self):
        self.__product_name = None
        self.__shop_name = None
        self.__price = None


    def product_info(self):
        return {'product_name': self.__product_name, 'shop_name': self.__shop_name, 'price': self.__price}


    def product_info_set(self, product_name, shop_name, price):
        self.__product_name = product_name
        self.__shop_name = shop_name
        self.__price = price
        Product.all_products.append(self)


    def __str__(self):
        return (f'Product name: {self.__product_name} | '
                f'Shop name: {self.__shop_name} | '
                f'Price: {self.__price}')


    @staticmethod
    def check_price(self, price_str):
        try:
            price = float(price_str)
            if price > 0:
                return True, price
            else:
                return False
        except ValueError:
            return False


    def __add__(self, other):
        if isinstance(other, Product):
            return self.__price + other.__price
        elif isinstance(other, float):
            return self.__price + other
        else:
            raise ValueError('Unknown data type for adding')


    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)


class Warehouse:

    def __init__(self):
        self.__products = []


    def products_getter(self):
        return self.__products


    def products_setter(self, products_lst):
        self.__products = products_lst


    @staticmethod
    def int_index(index_str):
        try:
            index = int(index_str)
            return True, index
        except ValueError:
            return False


    def product_by_index(self, index):
        if 0 <= index < len(self.__products):
            return [True, self.__products[index]]
        else:
            return False


    def product_by_name(self, search_name):
        products_lst = []
        for item in self.__products:
            if item.product_info()['product_name'] == search_name:
                products_lst.append(item)
        if len(products_lst) == 0:
            return [False]
        else:
            return [True, products_lst]


    def sort_by_name(self):
        self.__products.sort(key=lambda product: product.product_info()['product_name'])


    def sort_by_shop(self):
        self.__products.sort(key=lambda product: product.product_info()['shop_name'])


    def sort_by_price(self):
        self.__products = sorted(self.__products, key=lambda product: product.product_info()['price'])


def enter_product_index():
    is_right_choice = False
    counter = 0
    stock = Warehouse()
    stock.products_setter(products_lst=Product.all_products)
    selected_product = None
    for product in stock.products_getter():
        print(f'{counter} - {product.product_info()['product_name']}')
        counter += 1
    while not is_right_choice:
        user_index = input('Choose index of product from the list: ')
        stock = Warehouse()
        stock.products_setter(products_lst=Product.all_products)
        index_int = stock.int_index(index_str=user_index)
        if not index_int == False:
            user_product = stock.product_by_index(index=index_int[1])
            if not user_product == False:
                is_right_choice = True
                selected_product = user_product[1]
            else:
                print('Value is not correct, try again: ')
        else:
            print('Value is not correct, try again: ')
    return selected_product


def enter_product_name():
    stock = Warehouse()
    stock.products_setter(products_lst=Product.all_products)
    for product in stock.products_getter():
        print(f'{product.product_info()['product_name']}')
    user_product_name = input('Enter product name from list: ')
    user_product = stock.product_by_name(search_name=user_product_name)
    if not user_product[0]:
        print('There is not product with such a name')
    else:
        print(f'Information about your product / products: ')
        for product in user_product[1]:
            print(product)


def sort_type():
    is_right_choice = False
    while not is_right_choice:
        user_option = input('Choose type of sorting of products:\n'
                            '0 - by NAME\n'
                            '1 - by NAME OF SHOP\n'
                            '2 - by PRICE: \n')
        try:
            user_option_int = int(user_option)
            if 0 <= user_option_int <= 2:
                is_right_choice = True
                stock = Warehouse()
                stock.products_setter(products_lst=Product.all_products)
                match user_option_int:
                    case 0:
                        stock.sort_by_name()
                    case 1:
                        stock.sort_by_shop()
                    case 2:
                        stock.sort_by_price()
                print('Products list after sorting:')
                for product in stock.products_getter():
                    print(product)
            else:
                print('Your number must be from 0 to 2, try again')
        except ValueError:
            print('Your choice must be a number, try again')


def menu():
    choice = input('Select what you want to do:\n'
                   '0 - find product by index\n'
                   '1 - find product by name\n'
                   '2 - sort products\n'
                   '3 - find sum of products\n'
                   '4 - close program\n'
                   'Your choice: ')
    while not (choice.isdigit() and 0 <= int(choice) <= 4):
        print('Your choice is incorrect, try again')
        choice = input('Select what you want to do:\n'
                       '0 - find product by index\n'
                       '1 - find product by name\n'
                       '2 - sort products\n'
                       '3 - find sum of products\n'
                       '4 - close program\n'
                       'Your choice: ')
    choice_int = int(choice)
    match choice_int:
        case 0:
            print(f'Your product is: \n{enter_product_index()}')
        case 1:
            enter_product_name()
        case 2:
            sort_type()
        case 3:
            products_sum = product_one_obj + product_two_obj + product_three_obj + product_four_obj
            print(f'Sum of products prices is: {products_sum}')
        case 4:
            print('Program is closed')

product_one_obj = Product()
product_one_obj.product_info_set(product_name='HP Victus 15.6 inch FHD 144Hz Gaming Laptop', shop_name='21vek', price=3457.89)


product_two_obj = Product()
product_two_obj.product_info_set(product_name='MSI Thin 15 15.6” 144Hz FHD Gaming Laptop', shop_name='Electrosila', price=8768.00)


product_three_obj = Product()
product_three_obj.product_info_set(product_name='Logitech G305 LIGHTSPEED Wireless Gaming Mouse', shop_name='5element', price=77.00)


product_four_obj = Product()
product_four_obj.product_info_set(product_name='Logitech K120 Wired Keyboard', shop_name='5element', price=120.00)

menu()