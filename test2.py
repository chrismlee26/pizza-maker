class Pizza():
    def __init__(self, size, pizza_type):
        # super().__init__(self, pizza_price, order_num)
        self.toppings = list()
        self.pizza_price = 1
        self.crust = ['thin', 'pan', 'cheese-crust']
        self.size = ['small', 'medium', 'large']
        self.pizza_type = ['cheese', 'pepperoni',
                           'margherita', 'clam', 'custom']

    def pizza_size(self, size):
        self.pizza_price = 1
        if self.size == 'small':
            pizza_price = 8
        elif self.size == 'medium':
            pizza_price = 12
        elif self.size == 'large':
            pizza_price = 18
        return pizza_price

    def pizza_type(self, pizza_type):
        if self.pizza_type == 'custom':
        pizza = Custom_Pizza()
        elif:
            self.pizza_type = pizza_type


hawaiian = Pizza('small', 'cheese')

print(hawaiian.__dict__)
print(hawaiian.pizza_price)
