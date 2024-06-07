import Task1.Task1 as Task1
import Task2.Task2 as Task2
import Task3.Task3 as Task3
import Task4.Task4 as Task4
import Task5.Task5 as Task5

# Laboratory work number 3, variant 30.
#    Performed by the student of group 253503 Yarmak Veronika.
#    Version: 1.0
#    Date of performance: May 23, 2024


if __name__ == '__main__':

    one_more_time = True

    while one_more_time:
        print("\n"
              "Which task you want to check (1, 2, 3, 4, 5)?\n"
              "If you want to exit choose 0")
        try:
            num = int(input("Answer: "))
            if num == 1:
                Task1.general_func()
            elif num == 2:
                Task2.input_integers()
            elif num == 3:
                Task3.input_string()
            elif num == 4:
                Task4.input_string()
            elif num == 5:
                Task5.input_func()
            elif num == 0:
                one_more_time = False
        except ValueError:
            print("Input is incorrect. Try again")
