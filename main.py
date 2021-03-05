import random


class Pizza():
    def __init__(self, size, sauce, crust):
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
        pass


class Custom_Pizza():
    def __init__(self, size, sauce, crust):
        self.size = size  # s,m,l
        self.sauce = sauce  # white or red
        self.crust = crust
        self.pizza_price = 1

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
    def __init__(self, ):

    def bake_pizza(self, **args):
        # Prints entire statement of pizza: size, style, type, toppings etc.
        # Check if happy. Do u need to go back??? (back to context step menu)

        # Ok Let's bake!
        pass

    def pizza_return(self, **args):
        # Buzz buzz ,beep boop, your pizza is ready.

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
