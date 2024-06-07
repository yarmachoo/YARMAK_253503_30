# -*- coding: utf-8 -*-c
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import Task3.SequenceAnalyzer as SequenceAnalyzer
import Initialization.Initialization as init

def input_int(n):
    _int = init.init_int_user_input(n)
    return _int

def input_one_int():
    _int = init.input_int_check()
    return _int

def input_one_float():
    _float = init.input_float_check()
    return _float

def initialize():
    print("Input x from -1 to 1: ")
    x = input_one_float()
    return x
def general_func():
    """General function that is used in main.py"""
    new_input = True
    x_values = []
    while new_input:
        print("Do you want to input x elements? (1 - if yes, 0 if no)")
        answer = input_one_int()
        if answer == 1:
            x_values.append(initialize())
        else:
            new_input = False
    print("Input eps: ")
    eps = input_one_float()

    sequence_analyzer = SequenceAnalyzer.SequenceAnalyzer(x_values, eps)
    sequence_analyzer.analyze_sequence()
    sequence_analyzer.calculate_statistics()
    sequence_analyzer.plot_graphs()
    sequence_analyzer.print_table()

    # Вывод статистических данных
    print("\nStatistics:")
    print("Mean:", sequence_analyzer.mean)
    print("Median:", sequence_analyzer.median)
    print("Mode:", sequence_analyzer.mode)
    print("Variance:", sequence_analyzer.variance)
    print("Standard Deviation:", sequence_analyzer.std_dev)
