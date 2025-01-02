"""Solution for Project Euler problem 10: https://projecteuler.net/problem=10."""
from assertpy import assert_that
from sympy import sieve


def solve_p10(n: int) -> int:
    """Solver for problem 10."""
    return sum(i for i in sieve.primerange(1, n + 1))


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p10(10)).is_equal_to(17)
    assert_that(solve_p10(2000000)).is_equal_to(142913828922)
    # Solution.
    print(solve_p10(2000000))  # 142913828922
