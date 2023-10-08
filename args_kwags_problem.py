import random


# Problem 1: Calculate the Area (Positional Arguments)
# Write a Python function `calculate_area` that calculates the area of a rectangle. The function
# should accept two positional arguments: `length` and `width`. Return the area.

def calculate_area(length, width):
    return length * width


print('calculate_area: ', calculate_area(4, 5))


# -------------------------------------------------------------------------------------------------
# Problem 2: Format Greetings (Keyword Arguments)
# Create a function `format_greeting` that takes two keyword arguments: `name` (a string) and
# `greeting` (a string, with a default value of "Hello"). The function should return a formatted
# greeting message, such as "Hello, John!"
def format_greeting(name='', greeting="Hello"):
    return f'"{greeting}, {name}!"'


print(format_greeting(name='John'))


def format_greeting2(name, greeting="Hello"):
    return f'"{greeting}, {name}!"'


print(format_greeting('Johny'))

a = [1, 2, 3]


def sum(a, b, c):
    s = 0
    print()
    for i in (a, b, c):  # อันนี้มันจะรับแบบ fix จำนวน จับ a[] ยัดค่าใน a,b,c ถ้า a[] มี 4 มันจะ error
        s += i
    return s


print('sum', sum(*a))


def get_name():
    return random.choice(['BT', 'supak'])


def greeting(f_get_name):
    name = f_get_name()
    return f'hello {name}'


print(greeting(get_name))


# The reason why we pass get_name and not get_name() to the greeting() function is because we want to pass the function object itself, not the result of calling the function.

def greet(*args, **kwargs):
    print(f"Hello {args[0]}!")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


greet("Alice")
# Output: Hello Alice!

greet(get_name(), age=30, country="USA")


# Output:
# Hello BT/supak!
# age: 30
# country: USA

# -------------------------------------------------------------------------------------------------
# Problem 3: Calculate Volume (Positional Arguments)
# Write a function `calculate_volume` that calculates the volume of a rectangular prism. It should
# accept three positional arguments: `length`, `width`, and `height`. Return the volume.
def calculate_volume(length, width, height):
    return length * width * height


print('calculate_volume: ', calculate_volume(10, 5, 2))


# -------------------------------------------------------------------------------------------------
# Problem 4: Generate a URL (Keyword Arguments)
# Create a function `generate_url` that takes three keyword arguments: `protocol` (default value:
# "http"), `domain`, and `path` (default value: "/"). The function should return a URL in the format
# "protocol://domain/path".
def generate_url(protocol="http", domain="", path="/"):
    return f'{protocol}://{domain}{path}'


print('generate_url: ', generate_url(protocol='https', domain='google.com'))


# -------------------------------------------------------------------------------------------------
# Problem 5: Calculate Total Cost (Positional and Keyword Arguments)
# Write a function `calculate_total_cost` that calculates the total cost of purchasing items. It should
# accept a positional argument `base_price`, a variable number of positional arguments for item
# prices, and a keyword argument `discount` (default value: 0). Apply the discount to the sum of
# item prices and return the final cost.
def calculate_total_cost(base_price, *prices, discount=0):
    for price in prices:
        base_price += price * (100 - discount) / 100
    return base_price


print('calculate_total_cost: ', calculate_total_cost(1, 5, 6))

# -------------------------------------------------------------------------------------------------
# Problem 6: Join Strings (Positional Arguments)
# Create a function `join_strings` that accepts a keyword argument `separator` (default value: ", ")
# and a variable number of positional arguments (strings). The function should concatenate the
# strings with the separator and return the result.

a = [1, 2, 3]


def join_strings(*number, separator=","):
    return separator.join(str(i) for i in number)


print('join_strings: ', join_strings(*a, separator='+'))


# -------------------------------------------------------------------------------------------------
# Problem 7: Create a Dictionary (Keyword Arguments)
# Define a function `create_dict` that creates a dictionary with keyword arguments. The function
# should accept keyword arguments for keys and values and return a dictionary with those
# key-value pairs.
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


my_dict = {"name": "Alice", "age": 25}
my_function(**my_dict)

list_a = [1, 2, 3]
list_b = ['apple', 'banana', 'orange']


def create_dict(list_a=None, list_b=None):
    print(list_a, '|', list_b)
    if list_b is None:
        list_b = []
    if list_a is None:
        list_a = []
    dict = {}
    for i in range(len(list_b)):
        dict[list_b[i]] = list_a[i]
    return dict


print('create_dict: ', create_dict(list_a, list_b))


# -------------------------------------------------------------------------------------------------
# Problem 8: Calculate BMI (Positional Arguments)
# Create a function `calculate_bmi` that calculates the Body Mass Index (BMI) of a person. The
# function should accept two positional arguments: `weight` (in kilograms) and `height` (in meters). Return the BMI.

def calculate_bmi(weight, height):
    return weight / (height ** 2)


print('calculate_bmi: ', calculate_bmi(60, 1.61))


# -------------------------------------------------------------------------------------------------
# Problem 9: Calculate Interest (Positional Arguments)
# Write a function `calculate_interest` that calculates the simple interest on a principal amount. It
# should accept three positional arguments: `principal`, `rate`, and `time` (in years). Return the
# interest amount.
def calculate_interest(principal, rate, time):
    return principal * rate * time


print('calculate_interest: ', calculate_interest(1000, 0.05, 5))

# -------------------------------------------------------------------------------------------------
# Problem 10: Join Strings with Uppercase Option (Positional Arguments and Keyword Arguments)
# Extend the `join_strings` function from problem 6 to accept a keyword argument `uppercase`
# (default value: False). If `uppercase` is True, convert all strings to uppercase before joining;
# otherwise, join them as-is. The function should return the concatenated string.

a = ['bt', 'Supak', 'tong']


def join_strings10(*string, separator=",", uppercase=False):
    return separator.join(str(i).upper() if uppercase == True else str(i) for i in string)


print('join_strings10 : ', join_strings10(*a, separator='+', uppercase=True))
