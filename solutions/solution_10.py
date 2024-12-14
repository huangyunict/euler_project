from assertpy import assert_that
from sympy import sieve


def solve_p10(n: int) -> int:
    return sum([i for i in sieve.primerange(1, n + 1)])


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p10(10)).is_equal_to(17)
    # Solution.
    print(solve_p10(2000000))  # 142913828922
