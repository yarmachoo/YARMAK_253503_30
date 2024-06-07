# -*- coding: utf-8 -*-
import Task5.MatrixOperations as MatrixOperations
import Initialization.Initialization as init
def input_int(n):
    _int = init.init_int_user_input(n)
    return _int

def input_one_int():
    _int = init.input_int_check()
    return _int

def general_func():
    """General function that is used in main.py"""
    print("Input amount of columns:")
    n = input_one_int()
    print("Input amount of rows:")
    m = input_one_int()

    matrix_ops = MatrixOperations.MatrixOperations(n, m)
    matrix_ops.print_original_matrix()
    matrix_ops.find_replace_max_diagonal()
    matrix_ops.print_original_matrix()

    median_standard, median_programmed = matrix_ops.calculate_median()
    print("Медиана с использованием стандартной функции:", median_standard)
    print("Медиана через программирование формулы:", median_programmed)
