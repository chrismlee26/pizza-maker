import random


# Start Class: This is where the pizza maker starts and stores all the methods for user input options
class Start():
    # Instantiated Attributes
    def __init__(self, pizza_name, pizza_price=0, order_num=None):
        self.pizza_name = pizza_name
        self.order_num = random.randint(1000, 9999)
        self.order_num = order_num
        self.pizza_price = pizza_price

    # Start pizza making app
    def Start_Pizza(self):
        # pizza_start = None
        while pizza_start != '4':
            pizza_start = int(input(
                'What Pizza type do you want?\n[1] Full Pizza\n[2] Slice \n[3] Custom Pizza\n[4] Random'))
            if pizza_start == '1':
                # Operate pizza class which has random pizzas to choose Class Pizza
                self.create_pizza()
                pizza_name.append(self.create_pizza)  # <--- super lost :S
            elif pizza_start == '2':
                # Operate slice class (same as pizza) Class Slice
                slice_start = Slice()  # <--- am i supposed to be calling a class here :S:S:S:S:S:s
            elif pizza_start == '3':
                # Operate Pizza method that links to Custom_Pizza Class
                custom_start = Custom_Pizza()
            elif pizza_start == '4':
                pass

            # return


class Pizza():  # This class is the parent class for pizzas
    def __init__(self, size, pizza_type):
        super().__init__(self, pizza_price, order_num)
        self.toppings = list()
        self.crust = ['thin', 'pan', 'cheese-crust']
        self.size = {'small': 8, 'medium': 12, 'large': 18}
        self.pizza_type = ['cheese', 'pepperoni',
                           'margherita', 'clam', 'custom']

    def pizza_size(self, size):
        self.pizza_price = 1
        size_input = input(
            'What size do you want?\n[1] Small \n[2] Medium \n[3] Large')  # should this be self.?
        if size_input == 1:
            self.size == 'small'
        elif size_input == 2:
            self.size == 'medium'
        elif size_input == 3:
            self.size == 'large'
        return self.size.get(self.size)  # Is this right?!?!?!

    def create_crust(self):
        crust_input = input(
            'What crust type?\n[1] Thin \n[2] Pan \n[3] Cheese')  # should this be self.?
        if crust_input == 1:
            self.crust == 'thin'
        elif crust_input == 2:
            self.crust == 'pan'
        elif crust_input == 3:
            self.crust == 'cheese-crust'
        return self.crust

    def pizza_type(self, pizza_type):
        if self.pizza_type == 'custom':
        pizza2 = Custom_Pizza()
        elif:
            self.pizza_type = pizza_type


class Slice(Pizza):  # Slice inherits from pizza
    def __init__(self):
        self.pizza_price = 1
        self.size = 'large'
        # price from pizza class goes here, but this one /8
        return pizza_price / 8


class Custom_Pizza(Pizza):  # Inherits from Pizza
    def __init__(self, size, sauce, crust):
        self.size = size
        self.sauce = sauce  # white or red
        self.crust = crust
        self.pizza_price = 1

    # user can pick sauce
    def pick_sauce(self):
        sauce_input = input(
            'Red or white sauce?\n[1] Red \n[2] White')  # should this be self.?
        if crust_input == 1:
            self.sauce == 'Red'
        elif crust_input == 2:
            self.sauce == 'White'
        return self.sauce

    # user can add any toppings here and price is calculated at random
    def add_toppings(self, toppings):  # **kwargs? <--------
        for topping in self.toppings:
            self.pizza_price.length * random.randint(2, 4)
        self.toppings = toppings
        self.toppings.append(topping)
        return self.toppings

    # user can remove toppings here from the topping list.
    def remove_toppings(self, toppings):
        self.toppings = toppings
        self.toppings.remove(topping)
        return self.toppings

    def calc_price(self, toppings):
        for topping in self.toppings:
            self.pizza_price.length * random.randint(2, 4)
        return pizza_price  # <------- uhhhhhhhhh

# All pizza classes go here
# Bake Class prints returns


class Bake():
    def __init__(self):
        # Attributes and returns from other classes
        super().__init__(self, pizza_price, order_num)  # <- is this correct?

    def bake_pizza(self):
        # Prints entire statement of pizza: size, style, type, toppings etc.
        bake_pizza = input('Are you sure?\n[1] Yes\n[2]Go back')
        # yes -> pizza_return()
        if bake_pizza == 1:
            pizza_return()
            print('Ok Let\'s bake!')
        # no -> go back to Start_Pizza()
        if bake_pizza == 2:
            Start_Pizza()
            # Check if happy. Do u need to go back??? (back to context step menu)

    def pizza_return(self, **args):
        # Pull all the returns from other classes into here
        # for loop to read off toppings if applicable
        # otherwise just prints pizza_type
        # order_number missing
        # How to get price :S

        if pizza_type != 'custom':
            print(
                f'Buzz, Buzz, Beep, Boop. Your Pizza is ready:\n{pizza_name}\nYou ordered a {pizza_size} {pizza_type} pizza with {crust} crust.\nYour total is: {pizza_price}')
        if pizza_type == 'custom':
            print(
                f'Buzz, Buzz, Beep, Boop. Your Pizza is ready:\n{pizza_name}\nYou ordered a {pizza_size} {toppings} {sauce} sauce pizza with {crust} crust .\nYour total is: {pizza_price}')


# How to add params inside the classes?!?!??!?!?!
if __name__ == "__main__":
start1 = Start()
pizza1 = Pizza()

pizza_slice1 = Slice()
pizza_custom1 = Custom_Pizza()

bake1 = Bake()
