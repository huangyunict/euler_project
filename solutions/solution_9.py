"""Solution for Project Euler problem 9: https://projecteuler.net/problem=9."""
from assertpy import assert_that


def solve_p9(n: int) -> int:
    """Solver for problem 9."""
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            c = n - a - b
            if a * a + b * b == c * c:
                return a * b * c
    return -1


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p9(12)).is_equal_to(60)
    assert_that(solve_p9(1000)).is_equal_to(31875000)
    # Solution.
    print(solve_p9(1000))  # 31875000
