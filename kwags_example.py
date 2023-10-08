from random import random, randint
# without mutable handle:
# def process_list(list_to_process=[]):
#     list_to_process.append(randint(1, 10))
#     return list_to_process


def process_list(list_to_process=[]):
    if not list_to_process:
        list_to_process = []
    list_to_process.append(randint(1, 10))
    return list_to_process


print(process_list())
print(process_list())
print(process_list())
print(process_list())
