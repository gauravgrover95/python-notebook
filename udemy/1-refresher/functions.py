"""
Functions
"""

# Intro
print('Hello and welcome to functions!')
print()

# Function Definitions
def my_function():
    print("Inside my function")

def print_name(name):
    print(f'Hello {name}')

def print_fullname(first_name, last_name):
    print(f'Hello {first_name} {last_name}')

def print_color():
    color = 'Red'
    print(color)

def print_nums(high, low):
    print('high', high)
    print('low', low)

def multiply_nums(a, b):
    return a * b

def print_list(list_nums):
    for x in list_nums:
        print(x)

def add_tax(cost_item):
    tax_rate = .03
    return cost_item * tax_rate

def buy_item(cost):
    return cost + add_tax(cost)


# Function Calls

# Names
my_function()
print_name('Gaurav')
print_fullname('Gaurav', 'Grover')
print()

# Colors
color = 'Blue'
print(color)
print_color()
print()


# Nums
print_nums(10, 3)
print()
print_nums(3, 10)
print()
print_nums(low=3, high=10)
print()


# Multiply
sol = multiply_nums(10, 6)
print(sol)
print()

# Lists
numbers = [1, 2, 3, 4, 5]
print_list(numbers)
print()

# function calling another function
net_cost = buy_item(100)
print('net_cost', round(net_cost))