import numpy as np

from euler_common import matrix_pow_mod


def solve_p458(n: int) -> int:
    mod = pow(10, 9)
    mat = np.matrix(
        [[1, 1, 1, 1, 1, 1],
         [6, 1, 1, 1, 1, 1],
         [0, 5, 1, 1, 1, 1],
         [0, 0, 4, 1, 1, 1],
         [0, 0, 0, 3, 1, 1],
         [0, 0, 0, 0, 2, 1]], dtype=np.uint64)
    x = np.matrix([7, 0, 0, 0, 0, 0], dtype=np.uint64).transpose()
    result = sum(matrix_pow_mod(mat, n - 1, mod) * x) % mod
    return result.item((0, 0))


if __name__ == '__main__':
    print(solve_p458(1))  # 7
    print(solve_p458(2))  # 49
    print(solve_p458(3))  # 343
    print(solve_p458(4))  # 2401
    print(solve_p458(5))  # 16807
    print(solve_p458(6))  # 117649
    print(solve_p458(7))  # 818503
    print(solve_p458(pow(10, 12)))  # 423341841
