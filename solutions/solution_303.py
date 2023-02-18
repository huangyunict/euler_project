import math


def calc_f_naive(n: int) -> int:
    # Check for 9999...
    d = round(math.log10(n + 1))
    if pow(10, d) == n + 1:
        return int('1' * d + '2222' * d)
    # Enumerate all numbers with digits in {0,1,2}.
    dp = [0]
    b = 1
    while True:
        ndp = list(dp)
        for d in range(1, 3):
            for k in dp:
                v = d * b + k
                if v > 0 and v % n == 0:
                    return v
                ndp.append(v)
        b = b * 10
        dp, ndp = ndp, dp


def solve_p303_naive(n: int) -> int:
    result = 0
    for i in range(1, n + 1):
        f = calc_f_naive(i)
        assert f % i == 0
        result += f // i
    return result


def calc_f(n: int) -> int:
    dp = dict()  # map reminder to smaller number
    b = 1
    dp[0] = 0
    while True:
        for k in dp:
            assert dp[k] % n == k
        ndp = dict(dp)
        for d in range(1, 3):
            for k in dp:
                v = d * b + dp[k]
                if v > 0 and v % n == 0:
                    return v
                if v % n not in ndp:
                    ndp[v % n] = d * b + dp[k]
        b = b * 10
        dp, ndp = ndp, dp


def solve_p303(n: int) -> int:
    result = 0
    for i in range(1, n + 1):
        f = calc_f(i)
        assert f % i == 0
        result += f // i
    return result


if __name__ == '__main__':
    print(calc_f(2))  # 2
    print(calc_f(3))  # 12
    print(calc_f(7))  # 21
    print(calc_f(42))  # 210
    print(calc_f(89))  # 1121222
    print(calc_f_naive(9))  # 12222
    print(calc_f(9))  # 12222
    print(calc_f_naive(99))  # 1122222222
    print(calc_f(99))  # 1122222222
    print(calc_f_naive(999))  # 111222222222222
    print(calc_f(999))  # 111222222222222
    print(calc_f_naive(9999))  # 11112222222222222222
    print(calc_f(9999))  # 11112222222222222222
    print(solve_p303_naive(100))  # 11363107
    print(solve_p303(100))  # 11363107
    print(solve_p303_naive(10000))  # 1111981904675169
    print(solve_p303(10000))  # 1111981904675169
