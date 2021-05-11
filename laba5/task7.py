# Author: Andrii Reva, sKS-18
# Date: 12.03.2020

import numpy as np


class SumElements:
    def main_method(self):
        start1 = int(input("Enter the start of diapason 1: "))
        end1 = int(input("Enter the end of diapason 1: "))
        start2 = int(input("Enter the start of diapason 2: "))
        end2 = int(input("Enter the end of diapason 2: "))
        m1 = np.random.randint(start1, end1, (5, 10))
        m2 = np.random.randint(start2, end2, (5, 10))
        print("First matrix")
        self.print_matrix(m1)
        print("Second matrix")
        self.print_matrix(m2)
        m_row = m1.sum(axis=1)
        m_row = m_row.reshape(5, 1)
        m_call = m2.sum(axis=0)
        m_call = m_call.reshape(1, 10)
        print("Matrix-row")
        self.print_matrix(m_row)
        print("Matrix-string")
        self.print_matrix(m_call)

    @staticmethod
    def print_matrix(matrix):
        print(matrix)


def main():
    sum_elements = SumElements()
    sum_elements.main_method()


main()
