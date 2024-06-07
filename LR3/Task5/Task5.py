import Init.Initialization as init
def input_func():

    """This function is the entry point in this module (task 5, variant 5). The function displays comments
                     for the user and also calls functions to execute the task."""

    print("Task 5 (5): \n"
          "Найти максимальный по модулю элемент списка\n"
          "и сумму элементов списка, расположенных между\n"
          "первым и вторым положительными элементами\n")
    amount = 0
    is_input_correct = False
    while is_input_correct == False:
        try:
            amount = int(input("input amount af elements:"))
            is_input_correct=True
        except ValueError:
            print("Incorrect input. Enter integer, please!")
    print("Do you want to use generator? (y/n):")
    if input("Input answer(y/n): ") == "y":
        float_list = [i for i in init.generator_float(amount)]
    else:
        float_list = init.init_float_user_input(amount)

    print(f"Your list of elements: \n{float_list}\n")
    print(f"Max element (start from 0) is: {find_max_element(float_list)}")

    print(f"Sum of elements located between the first and second positive elements : {next(sum_between_positive(float_list), 0)}")

def find_max_element(float_list):
    """This function searches for the index of the maximal element."""
    abs_arr = []
    for num in float_list:
        abs_arr.append(abs(num))

    return max(abs_arr)

def sum_between_positive(float_list):
    """This function sum all elements between the passed indies"""
    found_first_positive = False
    sum_between = 0
    count_positive = 0
    for num in float_list:
        if num > 0:
            count_positive += 1

    if count_positive < 2: return 0

    for num in float_list:
        if num > 0:
            if found_first_positive:
                yield sum_between
                sum_between = 0
                break
            found_first_positive = True
        elif found_first_positive:
            sum_between += num
