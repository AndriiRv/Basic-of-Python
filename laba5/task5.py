# Author: Andrii Reva, sKS-18
# Date: 12.03.2020

import numpy as np


class SumMatrix:
    def main_method(self):
        m1 = np.random.randint(0, 5, (3, 3))
        m2 = np.random.randint(0, 5, (3, 3))
        self.print_matrix(m1)
        self.print_matrix(m2)
        result = self.sum_matrix(m1, m2)
        self.print_matrix(result)
        det_result = self.det(result)
        print("Determinant:", str(det_result))

    @staticmethod
    def print_matrix(matrix):
        print(str(matrix))

    @staticmethod
    def sum_matrix(a, b):
        result = a + b
        return result

    @staticmethod
    def det(matrix):
        det_matrix = np.linalg.det(matrix)
        return det_matrix


def main():
    sum_matrix = SumMatrix()
    sum_matrix.main_method()


main()
