from assertpy import assert_that


def solve_p1(n: int) -> int:
    return sum([x for x in range(0, n) if x % 3 == 0 or x % 5 == 0])


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p1(10)).is_equal_to(23)
    # Solution.
    print(solve_p1(1000))  # 233168
