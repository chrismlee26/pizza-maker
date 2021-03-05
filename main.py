import random


class start:
    def __init__(self):
        # Initiate (Instance variables to hold the pizza shop)
        # shop = Shop("Shop")
        pass

    def create_store(self):
        print('Welcome to pizza shop simulator')
        store_name = input("Pizza shop name: ")
        return Shop(store_name)
        # This should go further, picking decor & oven type

    def pick_pizza_style(self):
        # pick size, crust
        pass

    def create_pizza(self):
        # sauce, add_toppings, remove_toppings
        pizza_name = input("")

    def bake_pizza(self):
        # This one just asks if you're ready.
        # operates print_receipt.
        pass

    def print_receipt(self):
        # this method prints out 1. The shop name, style, 2. the pizza, baking style and toppings 3. final price of the pizza
        pass


class Shop():
    def __init__(self, name, starting_money=10000):
        self.name = name
        self.starting_money = starting_money
        self.current_money = starting_money
        self.pizza_base = list()
        self.toppings = list()
        # self.design = decor
        # self.oven = oven
        # self.pizza_region = pizza_region

    def pick_decor(self, decor):
        self.decor = ['pick_random', 'chain', 'italian', 'takeout']
        # This stuff should probably be inside shop, THis section should be only the functionality.
        for pick_shop in range(decor):
            if decor == 'pick_random':
                random.choice(decor)
            elif decor == 'chain':
                pass
            elif decor == 'italian':
                pass
            elif decor == 'takeout':  # THis one will force pizza_style ????
                pass
            return decor  # This return goes back into 'Main.py'

        # This probably gets moved into 'Main.py'
        decor = input(
            'Pick a decor style \n[1] random \n[2] old italy \n[3] cheap take-out')

    def pick_oven(self, oven):
        oven = ['Random_Oven', 'Gas', 'Wood + Brick']
        if oven == 'Random_Oven':
            pass
        elif oven == Gas:
            pass
        elif oven == Wood:
            pass
        elif oven == Brick:
            pass

    #     oven = input('Pick an oven style \n[1]Gas \n[2]Wood \n [3]Brick')
    #     # I think these might be protected, so users pizza types get stuck w this.

    def pizza_style(self):
        pizza_type = [Slices, NYC, Chicago, Chain]
        # based on decor / oven ========= these will create overriding classes that will affect topping choices/ prices / final result.
        # by the slice (ghetto pizza)
        # nyc (margherita, toppings like basil, etc.)
        # chain (full pizzas, comes in pairs, has more deals)
        # chicago (pizza pie $50 each)

        pass


class Pizza:
    def __init__(self, size, sauce, crust):
        self.size = size  # s,m,l
        self.sauce = sauce  # white or red
        self.crust = crust
        self.pizza_price = 1


def pizza_size(self, size):
    self.pizza_price = 1
    size = ['small', 'medium', 'large']
    if size == 'small':
        pizza_price = pizza_price * 0.75
    if size == 'medium':
        pizza_price = pizza_price
    if size == 'large':
        pizza_price = pizza_price * 1.75
    # if small = X * .75
    # if medium then price = X
    # if large then price = X * 1.5

    # All 3 have return to console at end
    # "...Your {pizza_size} = XXXXXXX..."
    pass


def create_crust(self, **args):
    # choosing a crust just changes the text return
    # if whatever = x:
    pass


def pick_sauce(self, **args):
    # sauce = white then
    # toppings change to white toppings
    # sauce = red then
    # toppings change to red toppings
    pass


def add_toppings(self, **args):
    # something.append(toppings)
    pass


def remove_toppings(self, **args):
    something.remove(toppings)
    pass


def bake_pizza(self, **args):
    # Prints entire statement of pizza: size, style, type, toppings etc.
    # Check if happy. Do u need to go back??? (back to context step menu)

    # Ok Let's bake!
    pass


class Bake():
    def __init__(self, ):
        # This class just does the baking step.


def bake_pizza(self, **args):
    # Prints entire statement of pizza: size, style, type, toppings etc.
    # Check if happy. Do u need to go back??? (back to context step menu)

    # Ok Let's bake!
    pass


def pizza_return(self, **args):
    # Buzbuzz ,bbeep beep, your pizza is ready.

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
