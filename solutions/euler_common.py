import numpy as np


def matrix_pow_mod(a: np.matrix, n: int, m: int) -> np.matrix:
    """ Return a^n % m in the matrix form.

    :param a: the input square matrix.
    :param n: the power.
    :param m: the modulo.
    :return: the pow modulo operation for matrices.
    """
    b = a % m
    result = np.matrix(np.identity(a.shape[0]), dtype=int)
    while n > 0:
        if n & 1 == 1:
            result = result * b % m
        b = b * b % m
        n = n >> 1
    return result
