import alg
# import ui
import numpy as np
# from scipy.optimize import linear_sum_assignment

while True:
    """ Get matrix """
    n = 3
    m = np.array([
        [3, 3, 3],
        [1, 3, 2],
        [3, 2, 0]])
    # m = np.random.randint(4, size=(n, n), 
    #                       dtype=np.uint8)

    """ Show matrix """
    print(m)

    """ Execute Hungarian algorithm """
    res = [0, 1, 2] # Indexes of rows
    # res = linear_sum_assignment(m)[1]

    """ Show result """
    print('Indexes of rows:') 
    print(res)

    print('Total cost:')
    sum = 0
    for i in range(n):
        sum += m[i][res[i]]
    print(sum)

    if input('Run again or print smth to exit:') != "":
        break
    

