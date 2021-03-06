import random


# Start Class: This is where the pizza maker starts and stores all the methods for user input options
class Start():
    # Instantiated Attributes
    def __init__(self, pizza_name, order_num=None, pizza_price=0):
        self.pizza_name = pizza_name
        if order_num is None:
            order_num = random.randint(1000, 9999)
        self.order_num = order_num
        self.pizza_price = pizza_price

    # Start pizza making app
    def Start_Pizza(self):
        pizza_start = None
        # pizza_name = Pizza(name, size, sauce, crust)  # <------- wtf!!!!
        # pizza_size <---------

        while pizza_start != '4':
            pizza_start = int(input(
                'What Pizza type do you want?\n[1] Full Pizza\n[2] Slice \n[3] Custom Pizza\n[4] Random'))
            if pizza_start == '1':
                # Operate pizza class which has random pizzas to choose Class Pizza
                self.create_pizza()
                pizza_name.append(self.create_pizza)
                pass
            elif pizza_start == '2':
                # Operate slice class (same as pizza) Class Slice
                pass
            elif pizza_start == '3':
                # Operate Pizza method that links to Custom_Pizza Class
                pass
            elif pizza_start == '4':
                pass

            # return

    def create_pizza(self):
        # [1]
        # if statements that allow choices
        # instantiates classes to create next steps
        pass

    def pizza_size(self):
        # if statements that allow choices
        # instantiates classes to create next steps
        pass

    def create_slice(self):
        # if statements that allow choices
        # instantiates classes to create next steps
        # [2]
        pass

    def create_custom(self):
        # if statements that allow choices
        # instantiates classes to create next steps
        # [3]
        pass

    def random_pizza(self):
        # Random goes straight to print_receipt. Could be anything from pizza list
        # [4]
        pass


class Pizza():
    def __init__(self, size, sauce, crust):
        super().__init__(self, pizza_price, order_num)
        self.toppings = list()
        self.sauce = sauce  # white or red
        self.crust = ['thin', 'pan', 'cheese-crust']
        self.pizza_price = 1
        self.size = ['small', 'medium', 'large']

        # Should be a list of pizzas in here to choose from
        self.pizza_list = ['cheese', 'pepperoni', 'margherita', ]

    def pizza_size(self, size):
        self.pizza_price = 1
        self.size = ['small', 'medium', 'large']
        if self.size == 'small':
            pizza_price = 8
        elif self.size == 'medium':
            pizza_price = 12
        elif self.size == 'large':
            pizza_price = 18
        return pizza_price

# Slice inherits from pizza, ------> all same as pizza except return /8 <--------


class Slice(Pizza):
    def __init__(self):
        self.pizza_price = 1
        self.size = 'large'
        # price from pizza class goes here, but this one /8
        return pizza_price / 8


class Custom_Pizza():  # ---------> inherits from <------
    def __init__(self, size, sauce, crust):
        self.size = size
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

        pass

    def add_toppings(self, toppings):  # **kwargs <--------
        for topping in self.toppings:
            self.pizza_price.length * random.randint(2, 4)

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
            f'Buzz, Buzz, Beep, Boop. Your Pizza is ready:\n{pizza_name}\nYou ordered a {pizza_size} pizza with {crust} crust {sauce} and {toppings}.\nYour total is: {pizza_price}')


#      if __name__ == "__main__":
