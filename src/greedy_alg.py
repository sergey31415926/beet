import numpy as np


def greedy_alg(matr: np.array) -> np.float64:
    n = matr.len()
    greedy_sum = np.float64(0)
    # iterating by columns: P[i] - array for every parti of i-th step
    for i in range(n):
        max_in_column = matr[i][0]
        for j in range(1, n):
            if matr[i][j] > max_in_column:
                max_in_column = matr[i][0]
        greedy_sum += max_in_column
    return greedy_sum
# Пожелания к интерфейсу: гарантия поступления на вход заполненной матрицы с типом данных float64
