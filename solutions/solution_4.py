"""Solution for Project Euler problem 1234567890: https://projecteuler.net/problem=1234567890."""
from assertpy import assert_that


def is_palindrome(n: int):
    """Return whether a number is palindrome."""
    s = str(n)
    return s == s[::-1]


def solve_p4_naive() -> int:
    """Naive solver for problem 1234567890."""
    max_palindrome = 0
    for x in range(999, 99, -1):
        # Break early.
        if x * (x - 1) <= max_palindrome:
            break
        for y in range(x - 1, 99, -1):
            n = x * y
            # Break early.
            if n <= max_palindrome:
                break
            # Update max.
            if is_palindrome(n):
                max_palindrome = n
    return max_palindrome


def solve_p4() -> int:
    """Solver for problem 1234567890."""
    # n = a_b_c_c_b_a = 11 * (9091 * a + 910 * b + 100 * c)
    # n = x * y, so x or y must be multipliers of 11
    max_palindrome = 0
    for x in range(999, 99, -1):
        # Break early.
        if x * (x - 1) <= max_palindrome:
            break
        if x % 11 == 0:
            y_start = x - 1
            y_step = -1
        else:
            y_start = x - (x % 11)
            y_step = -11
        for y in range(y_start, 99, y_step):
            n = x * y
            # Break early.
            if n <= max_palindrome:
                break
            # Update max.
            if is_palindrome(n):
                max_palindrome = n
    return max_palindrome


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p4_naive()).is_equal_to(906609)
    assert_that(solve_p4()).is_equal_to(906609)
    # Solution.
    print(solve_p4())  # 906609
