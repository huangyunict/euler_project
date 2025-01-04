"""Solution for Project Euler problem 16: https://projecteuler.net/problem=16."""
from assertpy import assert_that


def solve_p16(n: int) -> int:
    """Solver for problem 16."""
    return sum(int(x) for x in str(n))


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p16(pow(2, 15))).is_equal_to(26)
    assert_that(solve_p16(pow(2, 1000))).is_equal_to(1366)
    # Solution.
    print(solve_p16(pow(2, 1000)))  # 1366
