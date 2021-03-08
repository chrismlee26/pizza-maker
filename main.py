import random
# Start Class: This is where the pizza maker starts and stores all the methods for user input options


class Start():
    # Instantiated Attributes
    def __init__(self, pizza_price=0, order_num=None):
        #self.pizza_name = pizza_name
        self.order_num = random.randint(1000, 9999)
        self.order_num = order_num

    # Start pizza making app
    def start_pizza(self):
        pizza_start = None
        while pizza_start != '3':  # <-- 4? Or something else
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
                custom_pizza.sauce()
                custom_pizza.add_toppings()
                bake = Bake(custom_pizza, self.order_num)
                bake.bake_pizza()
            elif pizza_start == '3':
                break
            break
            # return


class Pizza():  # This class is the parent class for pizzas
    def __init__(self):
        self.toppings = list()
        self.size_options = {'small': 8, 'medium': 12, 'large': 18}
        self.pizza_type = ['cheese', 'hawaiian']
        self.pizza_price = 1
        self.size = None
        self.crust = None

    def pizza_size(self):
        size_input = input(
            'What size do you want?\n[1] Small \n[2] Medium \n[3] Large\n')
        if size_input == '1':
            self.size = 'small'
        elif size_input == '2':
            self.size = 'medium'
        elif size_input == '3':
            self.size = 'large'
        # Assigning the price of the pizza base don the size
        self.pizza_price = self.size_options[self.size]
        return self.size

    def create_crust(self):
        crust_input = input(
            'What crust type?\n[1] Thin \n[2] Pan \n[3] Cheese\n')  # should this be self.?
        if crust_input == '1':
            self.crust = 'thin'
        elif crust_input == '2':
            self.crust = 'pan'
        elif crust_input == '3':
            self.crust = 'cheese-crust'
        return self.crust

    def choose_type(self):
        type_input = input(
            'What type of pizza do you want?\n[1] cheese \n[2] hawaiian\n')
        if type_input == 'cheese':
            self.pizza_type = 'cheese'
        else:
            self.pizza_type = 'hawaiian'
        return self.pizza_type

# Inherits from Pizza with new methods for customization


class Custom_Pizza(Pizza):
    def __init__(self):
        super.__init__(self, pizza_size)
        self.pizza_size = pizza_size
        # self.sauce = sauce  # white or red
        # self.crust = crust
        self.pizza_price = 1
        self.toppings = []
    # user can pick sauce

    def pick_sauce(self):
        sauce_input = input(
            'Red or white sauce?\n[1] Red \n[2] White\n')  # should this be self.?
        if crust_input == 1:
            self.sauce = 'Red'
        elif crust_input == 2:
            self.sauce = 'White'
        return self.sauce

    # user can add any toppings here and price is calculated at random
    def add_toppings(self):
        toppings_input = None
        self.toppings = []
        while toppings_input != 'end':
            toppings_input = input(
                'Input any toppings you want to add: (Type \'end\' to continue)')
            self.toppings.append(input)
        self.pizza_price += self.toppings.length * random.randint(2, 4)
        return self.toppings

    # user can remove toppings here from the topping list.
    # def remove_toppings(self, toppings):
    #     self.toppings = toppings
    #     self.toppings.remove(topping)
    #     return self.toppings
# All pizza classes go here
# Bake Class prints returns


class Bake():
    def __init__(self, pizza, order_num):
        # Attributes and returns from other classes
        self.pizza = pizza
        self.order_num = order_num

    def bake_pizza(self):
        # Prints entire statement of pizza: size, style, type, toppings etc.
        # Pull all the returns from other classes into here
        # for loop to read off toppings if applicable
        # otherwise just prints pizza_type
        # order_number missing
        # How to get price :S
        print(
            f'Buzz, Buzz, Beep, Boop. Your Pizza is ready:\nYou ordered a {self.pizza.size} {self.pizza.pizza_type} pizza with {self.pizza.crust} crust.\nYour total is: {self.pizza.pizza_price} and uour order number is {self.order_num}')


# How to add params inside the classes?!?!??!?!?!
if __name__ == "__main__":
    start1 = Start()
    start1.start_pizza()
    # pizza1 = Pizza()
    # pizza_slice1 = Slice()
    # pizza_custom1 = Custom_Pizza()
    # bake1 = Bake()
