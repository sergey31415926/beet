import numpy as np
import random
import rand_engine


def create_rand_matr(n: int, a_min=0, a_max=10) -> np.array:
    # iterating by columns: P[i] - array for every party of i-th step
    rand_matr = np.empty(n, n)
    a = rand_engine.RandEngine(a_min, a_max)
    b = rand_engine.RandEngine(0, 1)
    for j in range(n):
        rand_matr[0][j] = a.get()
    for i in range(1, n):
        for j in range(n):
            rand_matr[i][j] = rand_matr[i-1][j] * b.get()
    return rand_matr


def round_matr(matr: np.array, n: int, round_n=2) -> np.array:  # for better presentation. Optional
    for i in range(n):
        for j in range(n):
            matr[i][j] = round(matr[i][j], round_n)
    return matr


