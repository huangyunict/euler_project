"""Solution for Project Euler problem 14: https://projecteuler.net/problem=14."""
from assertpy import assert_that


def solve_p14(max_n: int) -> int:
    """Solver for problem 14."""
    # Value dp[k] stores the chain length given number k.
    dp = {1: 1}
    for i in range(1, max_n):
        curr = []
        k = i
        while k not in dp:
            curr.append(k)
            if k % 2 == 0:
                k //= 2
            else:
                k = 3 * k + 1
        # Current chain length.
        r = dp[k]
        while len(curr) > 0:
            r += 1
            dp[curr.pop()] = r
    # Get the number with max chain length.
    return max(dp, key=dp.get)


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p14(1000000)).is_equal_to(837799)
    # Solution.
    print(solve_p14(1000000))  # 837799
