def get_partitions_dp(n: int, k: int, dp: dict) -> int:
    if n == 0:
        return 1
    if n < k:
        return get_partitions_dp(n, n, dp)
    if (n, k) in dp:
        return dp.get((n, k))
    result = 0
    for first in range(1, min(n, k) + 1):
        result += get_partitions_dp(n - first, first, dp)
    dp[(n, k)] = result
    return result


def solve_p76_dp(n: int) -> int:
    dp = dict()
    return get_partitions_dp(n, n, dp) - 1


def pentagonal(n: int) -> int:
    """ Return generalized pentagonal numbers, n could be negative.

    :param n: the input parameter.
    :return: the generalized pentagonal number.
    """
    return (3 * n * n - n) // 2


def get_partitions(n: int, dp: dict) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in dp:
        return dp.get(n)
    result = 0
    for k in range(-n - 1, n + 1):
        # Skip k=0.
        if k == 0:
            continue
        g = pentagonal(k)
        result += (-1 if k % 2 == 0 else 1) * get_partitions(n - g, dp)
    dp[n] = result
    return result


def solve_p76(n: int) -> int:
    dp = dict()
    return get_partitions(n, dp) - 1


if __name__ == '__main__':
    print(solve_p76_dp(5))  # 6
    print(solve_p76_dp(100))  # 190569291
    print(solve_p76(5))  # 6
    print(solve_p76(100))  # 190569291
