"""Solution for Project Euler problem 5: https://projecteuler.net/problem=5."""
import math
from assertpy import assert_that


def solve_p5(n: int) -> int:
    """Solver for problem 5."""
    return math.lcm(*list(range(1, n + 1)))


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p5(10)).is_equal_to(2520)
    assert_that(solve_p5(20)).is_equal_to(232792560)
    # Solution.
    print(solve_p5(20))  # 232792560
