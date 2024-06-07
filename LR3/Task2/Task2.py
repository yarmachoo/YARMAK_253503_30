import Init.Initialization as init


def input_integers():
    """This function is the entry point in this module (task 3, variant 30). The function displays comments
         for the user and also calls functions to execute the task."""
    print("Task 2 (30): \n"
          "Организовать цикл, который принимает целые числа с\n"
          "клавиатуры и подсчитывает количество четных чисел. \n"
          "Окончание цикла – ввод числа, большего 99\n")
    count = enter_integers()

    print(f"Amount of even integer: {count}")


def enter_integers():
    """This function accepts numbers less than 99 and returns their number."""
    entered_integer = 0
    count = 0
    while entered_integer <= 99:
        entered_integer = init.input_int_check()
        if entered_integer % 2 == 0:
            if entered_integer <= 99: count += 1
    return count
