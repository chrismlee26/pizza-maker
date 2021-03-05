import random


class Start():
    def __init__(self, pizza_name, order_num=None, pizza_price=0):
        self.pizza_name = pizza_name
        if order_num is None:
            order_num = random.randint(1000, 9999)
        self.order_num = order_num
        self.price = price

    def Start_Pizza(self):
        pizza_start = none
        pizza_name = Pizza(name, size, sauce, crust)  # <------- wtf!!!!
        while pizza_start != '4':
            pizza_start = int(input(
                'What Pizza do you want?\n[1] Full Pizza\n[2] Slice \n[3] Custom Pizza\n[4] Random'))
            if pizza_start == '1':
                # Operate pizza class which has random pizzas to choose Class Pizza
                pass
            elif pizza_start == '2':
                # Operate slice class (same as pizza) Class Slice
                pass
            elif pizza_start == '3':
                # Operate Pizza method that links to Custom_Pizza Class
                pass
            elif pizza_start == '4':
                pass
                # Return pizza

    def create_pizza(self):
        # [1]
        pass

    def create_slice(self):
        # [2]
        pass

    def create_custom(self):
        # [3]
        pass

    def random_pizza(self):
        # [4]
        pass


class Pizza():
    def __init__(self, size, sauce, crust):
        super().__init__(self, pizza_price, order_num)
        self.size = size  # s,m,l
        self.sauce = sauce  # white or red
        self.crust = crust
        self.pizza_price = 1

    def pizza_style(self):
        # Chain - All, NYC - All, Chicago (Full Only), Slices - Slice Only
        pizza_type = ['Chain', 'NYC', 'Chicago', 'Slices']

    def pizza_size(self, size):
        self.pizza_price = 1
        size = ['small', 'medium', 'large']
        if size == 'small':
            pizza_price = pizza_price * 0.75
        if size == 'medium':
            pizza_price = pizza_price
        if size == 'large':
            pizza_price = pizza_price * 1.75
        pass
        pass


class Slice(Pizza):
    def __init__(self,):

        # price from pizza class goes here, but this one /8
        super().__init__(self, pizza_price, order_num)
        pass


class Custom_Pizza():
    def __init__(self, size, sauce, crust):
        self.size = size  # s,m,l
        self.sauce = sauce  # white or red
        self.crust = crust
        self.pizza_price = 1
        super().__init__(self, pizza_price, order_num)

    def create_crust(self, crust):
        self.crust = crust
        # choosing a crust just changes the text return
        # if whatever = x:
        self.crust
        pass

    def pick_sauce(self, sauce):
        self.sauce.append(sauce)
        pass

    def add_toppings(self, toppings):
        self.toppings = toppings
        self.toppings.append(topping)
        pass

    def remove_toppings(self, toppings):
        self.toppings = toppings
        self.toppings.remove(topping)
        pass


class Bake():
    def __init__(self, **args):
        super().__init__(self, pizza_price, order_num)

    def bake_pizza(self, **args):
        # Prints entire statement of pizza: size, style, type, toppings etc.
        bake_pizza = input('Are you sure?\n[1] Yes\n[2]Go back')
        # yes -> pizza_return
        # no -> go back to stage 1
        # Check if happy. Do u need to go back??? (back to context step menu)

        # Ok Let's bake!
        pass

    def pizza_return(self, **args):
        # Buzz buzz ,beep boop, your pizza is ready.
        print(
            f'Buzz, Buzz, Beep, Boop. Your Pizza is ready\n{pizza_name}\nYou ordered a {pizza_type} with {crust}crust {sauce} and {toppings}.\n Please pay {pizza_price}')

        # This class introduces the game, initializes everything
        # welcome to pizza restaurant simulator
        # This is how it works , etcetc.

        # At least 4 classes are defined
        # Each class has at least 2 attributes with __init__()
        # Each class has at least 2 methods that use and or modify class attributes

        # All classes are used to instantiate example objects

        # Rationale about which attributes ad methods are made private, protected, or public is provided in code comments
        # or verbally in presentation

        # At least one class demonstrates composition (being composed of other objects)

        # A diagram is provided that shows an overview of all the classes that make up the system design
        # Diagram shows relationships between classes

        # At least one class inherits from another class
        # The Subclass overrides at least one superclass method

        # 5-10 Minute Demo
