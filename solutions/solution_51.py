from assertpy import assert_that
import sympy


def enumerate_help(num: str, idx: int, ds: str, prefix: str, dp: dict) -> None:
    if idx == len(num):
        if '*' in prefix:
            if prefix not in dp:
                dp[prefix] = list()
            dp[prefix].append(num)
        return
    if num[idx] == ds:
        enumerate_help(num, idx + 1, ds, prefix + '*', dp)
    enumerate_help(num, idx + 1, ds, prefix + num[idx], dp)


def enumerate_patterns(num: str, dp: dict) -> None:
    # All masked indices must have the same digit.
    for ds in [str(x) for x in range(10)]:
        enumerate_help(num, 0, ds, '', dp)


def solve_p51(n: int) -> int:
    ll = 1
    while True:
        patterns = dict()
        for p in sympy.primerange(pow(10, ll - 1), pow(10, ll)):
            enumerate_patterns(str(p), patterns)
        result = None
        for k, v in patterns.items():
            if len(v) >= n:
                result = v[0] if result is None else min(result, v[0])
        if result is not None:
            return int(result)
        ll += 1


if __name__ == '__main__':
    # Verify.
    assert_that(solve_p51(6)).is_equal_to(13)
    assert_that(solve_p51(7)).is_equal_to(56003)
    # Solution.
    print(solve_p51(8))  # 121313
