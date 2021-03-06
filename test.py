def pizza_size(size):
    pizza_price = 1
    size_list = ['small', 'medium', 'large']
    # print(size_list)

    if size == 'small':
        pizza_price = 8
    elif size == 'medium':
        pizza_price = 12
    elif size == 'large':
        pizza_price = 18
    return pizza_price


size = 'small'
new = pizza_size(size)
print(new)
