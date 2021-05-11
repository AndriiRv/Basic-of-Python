# Author: Andrii Reva, sKS-18
# Date: 12.03.2020

import numpy as np


class Determinant:
    def main_method(self):
        matrix = np.random.randint(0, 5, (3, 3))
        self.print_matrix(matrix)
        det_matrix = self.det(matrix)
        print("Determinant:", str(det_matrix))
        self.check_det(det_matrix, matrix)

    @staticmethod
    def print_matrix(matrix):
        print(str(matrix))

    @staticmethod
    def det(matrix):
        det_matrix = 0
        det_matrix += matrix[0, 0] * matrix[1, 1] * matrix[2, 2]
        det_matrix += matrix[2, 0] * matrix[0, 1] * matrix[1, 2]
        det_matrix += matrix[1, 0] * matrix[0, 2] * matrix[2, 1]
        det_matrix -= matrix[2, 0] * matrix[1, 1] * matrix[0, 2]
        det_matrix -= matrix[1, 0] * matrix[0, 1] * matrix[2, 2]
        det_matrix -= matrix[0, 0] * matrix[2, 1] * matrix[1, 2]
        return det_matrix

    @staticmethod
    def check_det(det, matrix):
        library_value = np.linalg.det(matrix)
        print("Library value of determinant = ", str(library_value))
        if abs(det - library_value) <= 0.0000001:
            print("Determinant is right")
        else:
            print("Determinant is wrong")


def main():
    det_matrix = Determinant()
    det_matrix.main_method()


main()
