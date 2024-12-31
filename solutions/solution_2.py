from assertpy import assert_that


def solve_p2_naive(n: int) -> int:
    a = 0
    b = 1
    result = 0
    while b < n:
        if b % 2 == 0:
            result += b
        a, b = b, a + b
    return result

def solve_p2(n: int) -> int:
    a = 0
    b = 2
    result = a
    while b < n:
        result += b
        a, b = b, a + 4 * b
    return result


if __name__ == "__main__":
    # Verify.
    assert_that(solve_p2_naive(100)).is_equal_to(44)
    assert_that(solve_p2(100)).is_equal_to(44)
    assert_that(solve_p2_naive(4000000)).is_equal_to(4613732)
    assert_that(solve_p2(4000000)).is_equal_to(4613732)
    # Solution.
    print(solve_p2(4000000))  # 4613732
