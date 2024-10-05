import math


def general_func():
    """This function is the entry point in this module (task 1, variant 30). The function displays comments
     for the user and also calls functions to execute the task """
    print("Task 1 (30): \n"
          "В соответствии с заданием своего варианта составить программу \n"
          "для вычисления значения функции c помощью разложения функции в \n"
          "степенной ряд. Задать точность вычислений eps. \n")

    x = input_float_x()
    eps = input_float_epsilon()

    print("______________________________________________________________")
    print("|      x      |     n     |     F(x)   |  Math F(x)  |   eps   |")
    print("______________________________________________________________")
    result, n = my_arccos(x, eps)
    print(f"|    {x:.3f}    |     {n}     |  {result:.6f}  |  {math.acos(x):.6f}   |  {eps}  |")


def my_arccos(x, eps):
    """This function calculates arccos and returns two parameters: the result and the number of iterations."""
    result = 0.0
    n = -1
    expr_eps = 1.0
    expression = 0.0

    while expr_eps >= eps and n < 500:
        n += 1
        expression += (math.factorial(2*n)
                      / (pow(4, n) * pow(math.factorial(n), 2) * (2 * n + 1))
                      * pow(x, 2 * n + 1))
        expr_eps = (math.factorial(2 * n)
                      / (pow(4, n) * pow(math.factorial(n), 2) * (2 * n + 1))
                      * pow(x, 2 * n + 1))
        result = math.pi / 2 - expression

    return result, n


def input_float_epsilon():
    """Function that check input of epsilon"""
    x = 0
    is_input_correct = False
    while is_input_correct is False:
        try:
            x = float(input("input epsilon float (from 0 to 1):"))
            if 0 <= x <= 1:
                is_input_correct = True
            else: print("Incorrect input. Enter correctly, please!")
        except ValueError:
            print("Incorrect input. Enter correctly, please!")
    return x


def input_float_x():
    """Function that check input of x"""
    x = 0
    is_input_correct = False
    while is_input_correct is False:
        try:
            x = float(input("input x float (from 0 to 1):"))
            if 0 <= x <= 1:
                is_input_correct = True
            else: print("Incorrect input. Enter correctly, please!")
        except ValueError:
            print("Incorrect input. Enter correctly, please!")
    return x