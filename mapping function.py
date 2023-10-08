# Mapping Functions:
# Problem: Given a list of integers, create a new list that contains the squares of each integer
# using the map function.
# Example Input: [1, 2, 3, 4, 5]
# Example Output: [1, 4, 9, 16, 25]
# Filtering with Functions:

# ex_input = [1, 2, 3, 4, 5]
# def squares(*args):
#     out = []
#     for i in args:
#         out.append(i**2)
#     return out
#
# print(squares(1, 2, 3, 4, 5))

a = [1, 2, 3, 4, 5]
def sqr(i):
    return i*i
b = map(sqr, a)
print(list(b))


# Problem: Given a list of numbers, filter out the even numbers using the filter function.
# Example Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Example Output: [2, 4, 6, 8, 10]
# Calculating Totals with Reduce:
# Problem: Use the reduce function to find the product of all elements in a list of numbers.
# Example Input: [2, 3, 4, 5]
# Example Output: 120
# Custom Sorting:
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = [2, 3, 4, 5]


def is_multiple_of_3(num):
    return num % 3 == 0


# Create a list of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: is_multiple_of_3(x), numbers))

# Print the result
print(result)



# Problem: Sort a list of strings by their lengths using the sorted function and a custom sorting
# function.
# Example Input: ["apple", "banana", "cherry", "date", "elderberry"]
# Example Output: ["date", "apple", "cherry", "banana", "elderberry"]
# Higher-Order Function Composition:
# Problem: Create a function compose that takes two functions, f and g, and returns a new
# function that is the composition of f(g(x)).
# Example Usage: composed = compose(f, g) should allow composed(x) to be equivalent to
# f(g(x)).
# Higher-Order Functions with Strings:
# Problem: Write a function that takes a list of strings and returns a new list with each string
# reversed, using the map function.
# Example Input: ["hello", "world", "python"]
# Example Output: ["olleh", "dlrow", "nohtyp"]
# Functional Filtering:
# Problem: Implement a function that filters a list of words based on a given condition (e.g., words
# containing a specific letter) using the filter function.
# Example Input: ["apple", "banana", "cherry", "date", "elderberry"] and the condition to filter words
# containing the letter "a."
# Example Output: ["apple", "banana", "date"]
# Recursive Map:
#
# Problem: Create a recursive function recursive_map that takes a function and a list and returns
# a new list where the function is applied to each element.
# Example Usage: recursive_map(square, [1, 2, 3, 4]) should return [1, 4, 9, 16].
# Word Counting with Reduce:
# Problem: Use the reduce function to count the total number of characters in a list of words.
# Example Input: ["apple", "banana", "cherry"]
# Example Output: 15
# Advanced Sorting:
# Problem: Sort a list of dictionaries by a specific key using the sorted function and a custom key
# function.
# Example Input: [{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }, { "name": "Charlie",
# "age": 35 }] and the key to sort by age.
# Example Output: [{ "name": "Bob", "age": 25 }, { "name": "Alice", "age": 30 }, { "name": "Charlie",
# "age": 35 }]