
# this is the first class that we will instantiate
# Pick a decor - Classic, Modern, Take-Out
#
import random


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
        self.decor = ['pick_random', 'italian', 'takeout']
        # This stuff should probably be inside shop, THis section should be only the functionality.
        for pick_shop in range(decor):
            if decor == 'pick_random':
                random.choice(decor)  # Check which one this is lol
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

        oven = input('Pick an oven style \n[1]Gas \n[2]Wood \n [3]Brick')
        # I think these might be protected, so users pizza types get stuck w this.

    def pizza_style(self):
        # based on decor / oven ========= these will create overriding classes that will affect topping choices/ prices / final result.
        # by the slice (ghetto pizza)
        # nyc (margherita, toppings like basil, etc.)
        # chain (full pizzas, comes in pairs, has more deals)
        # chicago (pizza pie $50 each)
        pizza_style = [Slices, NYC, Chicago, Chain, **args]

        pass
