# -*- coding: utf-8 -*-
import numpy as np
class MatrixOperations:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = np.random.randint(1, 100, size=(n, m))

    def print_original_matrix(self):
        """Print matrix"""
        print("Исходная матрица:")
        print(self.matrix)

    def find_replace_max_diagonal(self):
        """Find and replace max diagonal"""
        max_in_rows = np.max(self.matrix, axis=1)
        max_indices = np.argmax(self.matrix, axis=1)
        diag_indices = np.diag_indices(min(self.n, self.m))

        for i in range(len(diag_indices[0])):
            row = diag_indices[0][i]
            col = diag_indices[1][i]
            max_row = max_indices[row]
            self.matrix[row, col], self.matrix[row, max_row] = self.matrix[row, max_row], self.matrix[row, col]

    def calculate_median(self):
        """Calculate median"""
        diag_elements = np.diagonal(self.matrix)
        median_standard = np.median(diag_elements)
        sorted_diag = np.sort(diag_elements)
        n_diag = len(sorted_diag)
        if n_diag % 2 == 0:
            median_programmed = (sorted_diag[n_diag // 2 - 1] + sorted_diag[n_diag // 2]) / 2
        else:
            median_programmed = sorted_diag[n_diag // 2]
        return median_standard, median_programmed