import numpy as np
import random


# def rand_interval_a_b() -> tuple:  # can be used by another type of matrix
#     a_min = random.uniform(0, 5)  # real number from begin to end
#     a_max = random.uniform(a_min, 10)
#     b_min = random.random()  # real number from 0.0 to 1.0
#     b_max = random.uniform(b_min, 1)
#     return a_min, a_max, b_min, b_max

class RandInterval(object):
    def __int__(self, begin: float, end: float):
        self.begin = begin
        self.end = end

    def get(self):
        rand_min = random.uniform(self.begin, self.end)
        rand_max = random.uniform(rand_min, self.end)
        return rand_min, rand_max


def create_rand_matr(n: int, a_min=0, a_max=10) -> np.array:
    # round(number, n) - округление до n знаков после запятой
    # iterating by columns: P[i] - array for every party of i-th step
    rand_matr = np.empty(n, n)
    a = RandInterval(a_min, a_max)
    b = RandInterval(0, 1)
    for j in range(n):
        rand_matr[0][j] = random.uniform(a.get())
    for i in range(1, n):
        for j in range(n):
            rand_matr[i][j] = rand_matr[i-1][j] * random.uniform(b.get())
    return rand_matr


def round_matr(matr: np.array, n: int, round_n=2) -> np.array:  # for better presentation. Optional
    for i in range(n):
        for j in range(n):
            matr[i][j] = round(matr[i][j], round_n)
    return matr



