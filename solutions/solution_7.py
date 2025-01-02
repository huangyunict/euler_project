"""Solution for Project Euler problem 7: https://projecteuler.net/problem=7."""
from assertpy import assert_that
from sympy import prime


def solve_p7(n: int) -> int:
    """Solver for problem 7."""
    return prime(n)


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p7(6)).is_equal_to(13)
    assert_that(solve_p7(10001)).is_equal_to(104743)
    # Solution.
    print(solve_p7(10001))  # 104743
