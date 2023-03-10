import numpy as np


def greedy_alg(matr: np.array) -> np.float64:
    n = matr.len()
    greedy_sum = np.float64(0)
    # на случай если по столбцам
    for i in range(n):
        max_in_column = matr[i][0]
        for j in range(1, n):
            if matr[i][j] > max_in_column:
                max_in_column = matr[i][0]
        greedy_sum += max_in_column
    return greedy_sum
    # на случай если по строкам
    # for j in range(0,n):
    #     max_in_column=matr[0][j]
    #     for i in range(1,n):
    #         if matr[i][j] > max_in_column:
    #             max_in_column = matr[i][0]
    #     greedy_sum += max_in_column
    # return greedy_sum
