# Author: Andrii Reva, sKS-18
# Date: 12.03.2020

import numpy as np


class Expression:
    def main_method(self):
        m1 = np.random.randint(0, 5, (3, 3))
        m2 = np.random.randint(0, 5, (3, 3))
        self.PrintMatrix(m1)
        self.PrintMatrix(m2)
        result = self.expression_matrix(self, m1, m2)
        self.PrintMatrix(result)
        det_result = self.det(result)
        print("Determinant:", str(det_result))

    @staticmethod
    def PrintMatrix(matrix):
        print(str(matrix))

    @staticmethod
    def expression_matrix(self, a, b):
        a = 3 * a
        self.print_matrix(a)
        b = 5 * b
        self.print_matrix(b)
        result = a + b
        return result

    @staticmethod
    def det(matrix):
        det_matrix = np.linalg.det(matrix)
        return det_matrix


def main():
    expression = Expression()
    expression.main_method()


main()
