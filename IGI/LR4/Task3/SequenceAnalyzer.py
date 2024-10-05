# -*- coding: utf-8 -*-c
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
class SequenceAnalyzer:
    def __init__(self, x_values, eps):
        """Initialize"""
        self.x_values = x_values
        self.eps = eps
        self.results = []

    def my_arccos(self, x, eps):
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

    def analyze_sequence(self):
        """Analyse sequence"""
        for x in self.x_values:
            result, n = self.my_arccos(x, self.eps)
            math_result = math.acos(x)
            self.results.append({'x': x, 'F(x)': result, 'n': n, 'Math F(x)': math_result})

    def calculate_statistics(self):
        """Calculate mean, median, mode, variance, and standard deviation"""
        Fx_values = [result['F(x)'] for result in self.results]
        self.mean = np.mean(Fx_values)
        self.median = np.median(Fx_values)
        mode_result = stats.mode(Fx_values)
        if isinstance(mode_result, np.ndarray):
            self.mode = mode_result[0][0]
        else:
            self.mode = mode_result
        self.variance = np.var(Fx_values)
        self.std_dev = np.std(Fx_values)

    def plot_graphs(self):
        """Plot the function F(x) from the results"""
        x_values = [result['x'] for result in self.results]
        Fx_values = [result['F(x)'] for result in self.results]
        math_Fx_values = [result['Math F(x)'] for result in self.results]

        plt.plot(x_values, Fx_values, label='F(x) from series')
        plt.plot(x_values, math_Fx_values, label='Math F(x)')
        plt.xlabel('x')
        plt.ylabel('F(x)')
        plt.title('Comparison of F(x) from series and Math F(x)')
        plt.legend()
        plt.grid(True)
        plt.show()

    def print_table(self):
        """Print the table"""
        print("{:<8} {:<12} {:<10} {:<14}".format('x', 'F(x)', 'n', 'Math F(x)'))
        for result in self.results:
            print("{:<8.3f} {:<12.8f} {:<10} {:<14.8f}".format(result['x'], result['F(x)'], result['n'], result['Math F(x)']))
