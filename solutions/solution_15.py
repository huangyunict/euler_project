"""Solution for Project Euler problem 15: https://projecteuler.net/problem=15."""
from assertpy import assert_that
from sympy import binomial


def solve_p15(m: int, n: int) -> int:
    """Solver for problem 15."""
    return binomial(m + n, n)


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p15(2, 2)).is_equal_to(6)
    assert_that(solve_p15(20, 20)).is_equal_to(137846528820)
    # Solution.
    print(solve_p15(20, 20))  # 137846528820
