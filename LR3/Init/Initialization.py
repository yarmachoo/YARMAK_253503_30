import random


def generator_int(n):
    """Generator func for int elements"""
    for i in range(1, n):
        yield random.randrange(-10, 10)


def generator_float(n):
    """Generator func for float elements"""
    for i in range(1, n):
        yield round(random.uniform(-10, 10), 3)


def init_int_user_input(n):
    """Initializer func for int elements"""
    el_list = []
    while n > 0:
        el_list.append(input_int_check())
        n -= 1
    return el_list


def init_float_user_input(n):
    """Initializer func for float elements"""
    el_list = []
    while n > 0:
        el_list.append(input_float_check())
        n -= 1
    return el_list


def input_int_check():
    """Func checks input of int elements"""
    is_input_correct = False
    while is_input_correct is False:
        try:
            el = int(input("input int element:"))
            is_input_correct = True
        except ValueError:
            print("Incorrect input. Enter integer, please!")
    return el


def input_float_check():
    """Func checks input of float elements"""
    is_input_correct = False
    el = 0
    while is_input_correct is False:
        try:
            el = float(input("input float element:"))
            is_input_correct = True
        except ValueError:
            print("Incorrect input. Enter float, please!")
    return el

