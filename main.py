import random
# Start Class: This is where the pizza maker starts and stores all the methods for user input options


class Start():
    # Instantiated Attributes
    def __init__(self, pizza_price=0, order_num=None):
        # self.pizza_name = pizza_name
        self.order_num = random.randint(1000, 9999)

    # Start pizza making app
    def start_pizza(self):
        pizza_start = None
        while pizza_start != '3':
            pizza_start = input(
                'What Pizza type do you want?\n[1] Full Pizza \n[2] Custom Pizza\n[3] End Program\n')
            if pizza_start == '1':
                # Operate pizza class methods
                pizza = Pizza()
                pizza.pizza_size()
                pizza.create_crust()
                pizza.choose_type()
                bake = Bake(pizza, self.order_num)
                bake.bake_pizza()
            elif pizza_start == '2':
                # Operate Custom_Pizza methods
                custom_pizza = Custom_Pizza()
                custom_pizza.pizza_size()
                custom_pizza.create_crust()
                custom_pizza.choose_type()
                custom_pizza.pick_sauce()
                custom_pizza.add_toppings()
                bake = Bake(custom_pizza, self.order_num,
                            custom_pizza.toppings)
                bake.bake_pizza()
            elif pizza_start == '3':
                break
            break


# Inherits from Pizza with new methods for customization of a pizza


class Custom_Pizza(Pizza):
    def __init__(self):
        self.pizza_price = 1
        self.toppings = []
        self.size = None
        self.size_options = {'small': 8, 'medium': 12, 'large': 18}
        self.crust = None
        self.sauce = None

    # Asks user to pick a sauce type
    def pick_sauce(self):
        sauce_input = input(
            'Red or white sauce?\n[1] Red \n[2] White\n')
        if sauce_input == 1:
            self.sauce = 'Red'
        elif sauce_input == 2:
            self.sauce = 'White'
        return self.sauce

    # user can add any toppings here, which are appended to a topping list and price is calculated based on the list length multiplied by a random value between 1 and 3.
    def add_toppings(self):
        toppings_input = None
        self.toppings = []
        while toppings_input != 'end':
            toppings_input = input(
                'Input any toppings you want to add: (Type \'end\' to continue)')
            self.toppings.append(toppings_input)
        self.toppings.remove('end')
        self.pizza_price += len(self.toppings) * random.randint(1, 3)
        return self.toppings

    # user can remove toppings here from the topping list.
    # def remove_toppings(self, toppings):
    # removed remove function for now :(


# Bake Class prints returns, takes Start as it's Parent
class Bake(Start):
    def __init__(self, pizza, order_num, toppings=None):
        # Attributes and returns from other classes
        self.pizza = pizza
        self.toppings = toppings
        super().__init__(order_num)
        self.order_num = order_num

    def bake_pizza(self):
        print((
            f'Buzz, Buzz, Beep, Boop. Your Pizza is ready:\nYou ordered a {self.pizza.size} {self.pizza.pizza_type} {self.toppings} toppings pizza with {self.pizza.crust} crust.\nYour total is: ${self.pizza.pizza_price:.2f} and your order number is #{self.order_num}').replace('[', '').replace(']', ''))


if __name__ == "__main__":
    start1 = Start()
    start1.start_pizza()
