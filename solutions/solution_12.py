"""Solution for Project Euler problem 12: https://projecteuler.net/problem=12."""
from assertpy import assert_that
from sympy import divisor_count


def solve_p12(k: int) -> int:
    """Solver for problem 12."""
    i = 1
    while True:
        n = i * (i + 1) // 2
        if divisor_count(n) > k:
            return n
        i += 1


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p12(5)).is_equal_to(28)
    assert_that(solve_p12(500)).is_equal_to(76576500)
    # Solution.
    print(solve_p12(500))  # 76576500
