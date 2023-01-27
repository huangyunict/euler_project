from sympy import nextprime


def matrix_multiply_mod(a: list[int], b: list[int], mod: int) -> list[int]:
    """ Return a*b in the matrix form.

    :param a: the input 2x2 matrix represent as [a00,a01,a10,a11].
    :param b: the input 2x2 matrix represent as [b00,b01,b10,b11].
    :param mod: the modulo.
    :return: the multiplication modulo operation for matrices.
    """
    return [(a[0] * b[0] + a[1] * b[2]) % mod,
            (a[0] * b[1] + a[1] * b[3]) % mod,
            (a[2] * b[0] + a[3] * b[2]) % mod,
            (a[2] * b[1] + a[3] * b[3]) % mod]


def matrix_pow_mod(a: list[int], b: int, mod: int) -> list[int]:
    """ Return a^b % mod in the matrix form.

    :param a: the input 2x2 matrix represent as [a00,a01,a10,a11].
    :param b: the power.
    :param mod: the modulo.
    :return: the pow modulo operation for matrices.
    """
    if b == 0:
        # The identity matrix.
        return [1, 0, 0, 1]
    if b % 2 != 0:
        sub = matrix_pow_mod(a, b - 1, mod)
        return matrix_multiply_mod(a, sub, mod)
    sub = matrix_pow_mod(a, b // 2, mod)
    return matrix_multiply_mod(sub, sub, mod)


def fibonacci_mod(n: int, mod: int) -> int:
    """ Return the n-th Fibonacci number f(n)%mod.

    :param n: the index in the Fibonacci sequence.
    :param mod: the modulo.
    :return: Return the n-th Fibonacci number f(n)%mod.
    """
    matrix = matrix_pow_mod([1, 1, 1, 0], n, mod)
    return matrix[1]


def solve_p304(n: int) -> int:
    mod = 1234567891011
    result = 0
    a = nextprime(pow(10, 14))
    for i in range(n):
        result = (result + fibonacci_mod(a, mod)) % mod
        a = nextprime(a)
    return result


if __name__ == '__main__':
    print(solve_p304(100000))  # 283988410192
