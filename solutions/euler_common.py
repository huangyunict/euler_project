import numpy as np


def matrix_pow_mod(a: np.matrix,
                   n: int,
                   mod: int,
                   dtype=np.uint64) -> np.matrix:
    """ Return a^n % mod in the matrix form.

    :param a: the input square matrix.
    :param n: the power.
    :param mod: the modulo.
    :param dtype: the numpy data type. 'np.unit64' for better performance while 'object' for arbitrary long integers.
    :return: the pow modulo operation for matrices.
    """
    b = a % mod
    result = np.matrix(np.identity(a.shape[0]), dtype=dtype)
    while n > 0:
        if n & 1 == 1:
            result = result * b % mod
        b = b * b % mod
        n = n >> 1
    return result


def mod_prime_inv(x: int, mod_prime: int) -> int:
    """ Return the modulo inverse `r` such that `(x*r)%m=1`.

    :param x: the input value.
    :param mod_prime: the modulo, must be a prime number.
    :return: the modulo inverse `r` such that `(x*r)%m=1`.
    """
    return pow(x, mod_prime - 2, mod_prime)


def binomial_mod_prime(n: int, k: int, mod_prime: int) -> int:
    """ Return the binomial coefficient with modulo: C(n,k)%m. Modified from:
        https://fishi.devtail.io/weblog/2015/06/25/computing-large-binomial-coefficients-modulo-prime-non-prime/

    :param n: n>=0, the total number of objects to choose from.
    :param k: 0<=k<=n, the number of chosen objects.
    :param mod_prime: m>=2, the modulo, must be a prime number.
    :return: the binomial coefficient with modulo: C(n,k)%m.
    """

    # Function to get degree of p in n! (exponent of p in the factorization of n!).
    def fact_exp(n, p):
        e = 0
        u = p
        t = n
        while u <= t:
            e += t // u
            u *= p
        return e

    # Shortcuts.
    if k > n:
        return 0
    if k > n // 2:
        return binomial_mod_prime(n, n - k, mod_prime)
    # Check if degrees work out.
    num_degree = fact_exp(n, mod_prime) - fact_exp(n - k, mod_prime)
    den_degree = fact_exp(k, mod_prime)
    if num_degree > den_degree:
        return 0
    # Calculate numerator and cancel out occurrences of p.
    num = 1
    for i in range(n, n - k, -1):
        cur = i
        while cur % mod_prime == 0:
            cur //= mod_prime
        num = (num * cur) % mod_prime
    # Calculate denominator and cancel out occurrences of p.
    den = 1
    for i in range(1, k + 1):
        cur = i
        while cur % mod_prime == 0:
            cur //= mod_prime
        den = (den * cur) % mod_prime
    # Result
    return (num * mod_prime_inv(den, mod_prime)) % mod_prime


def multinomial_mod_prime(n: int, ks: list[int], mod_prime: int) -> int:
    """ Return the multinomial coefficient: n! / (ks[0]! ks[1]! ...). The sum of list ks could be less than n, and the
        last missing value is treated as it passed in ks. For example,
        multinomial_mod_prime(10,[1,3],*) == multinomial_mod_prime(10,[1,3,6],*).

    :param n: n>=0, the total number of objects to choose from.
    :param ks: 0<=ks[*]<=n, sum(ks)<=n, the numbers of chosen objects.
    :param mod_prime: m>=2, the modulo, must be a prime number.
    :return: the multinomial coefficient: n! / (ks[0]! ks[1]! ...).
    """
    result = 1
    for k in ks:
        result = result * binomial_mod_prime(n, k, mod_prime) % mod_prime
        n -= k
        assert n >= 0
    return result


if __name__ == '__main__':
    assert binomial_mod_prime(950, 100, 1000000007) == 640644226
    assert multinomial_mod_prime(950, [100], 1000000007) == 640644226
    assert multinomial_mod_prime(950, [100, 850], 1000000007) == 640644226
    assert multinomial_mod_prime(11, [1, 4, 4, 2], 1000000007) == 34650
    assert multinomial_mod_prime(11, [1, 4, 4], 1000000007) == 34650
    assert multinomial_mod_prime(11, [1, 4, 4], 17) == 34650 % 17
    assert multinomial_mod_prime(3, [0, 3, 0], 1000000007) == 1
