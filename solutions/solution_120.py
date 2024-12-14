from assertpy import assert_that


def calc_r_max(a: int) -> int:
    r_max = 2
    for n in range(1, a*2+2, 2):
        r = (2 * n * a) % (a * a)
        r_max = max(r_max, r)
    return r_max


def solve_p120():
    result = 0
    for a in range(3, 1001):
        result += calc_r_max(a)
    return result


if __name__ == "__main__":
    # Verify.
    assert_that(calc_r_max(7)).is_equal_to(42)
    # Solution.
    print(solve_p120())  # 333082500
