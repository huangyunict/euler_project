"""Solution for Project Euler problem 6: https://projecteuler.net/problem=6."""
from assertpy import assert_that


def solve_p6(n: int) -> int:
    """Solver for problem 6."""
    linear_sum = n * (n + 1) // 2
    square_sum = n * (n + 1) * (2 * n + 1) // 6
    return linear_sum * linear_sum - square_sum


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p6(10)).is_equal_to(2640)
    assert_that(solve_p6(100)).is_equal_to(25164150)
    # Solution.
    print(solve_p6(100))  # 25164150
