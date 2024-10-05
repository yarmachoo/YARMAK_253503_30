import Task1.Notebook as Notebook
import Task1.Person as Person
import Initialization.Initialization as init

def input_name():
    name = input("Input full name: ")
    return name

def input_int(n):
    _int = init.init_int_user_input(n)
    return _int

def input_one_int():
    _int = init.input_int_check()
    return _int

def initialize():
    """Init info about person"""
    print("Input info about friend:")
    name = input_name()
    print("Input date of birth: ")
    date = input_one_int()
    print("Input month of birth (num): ")
    month = input_one_int()
    print("Input year of birth (num): ")
    year = input_one_int()
    return Person.Person(name, date, month, year)

def general_func():
    """General function that is used in main.py"""
    notebook = Notebook.Notebook()
    new_input = True
    while new_input:
        print("Do you want to input note? (1 - if yes, 0 if no)")
        answer = input_one_int()
        if answer == 1:
            notebook.add_note(initialize())
        else:
            new_input = False

    notebook.serialize_to_file('friends.txt')
    notebook.serialize_to_file_csv('friends.csv')
    print("Deserialize by csv:")
    Notebook.Notebook.deserialize_from_file_csv("friends.csv")
    print("Deserialize by pickle:")
    loaded_friends_book = Notebook.Notebook.deserialize_from_file('friends.txt')
    for friend_note in loaded_friends_book.friends:
        print(friend_note)

    print("\n")
    new_input = True
    while new_input:
        print("Do you want to input age to find friends? (1 - if yes, 0 if no)")
        answer = input_one_int()
        if answer == 1:
            age_to_find = input_one_int()
            loaded_friends_book.print_friends_by_age(age_to_find)
        else:
            new_input = False
