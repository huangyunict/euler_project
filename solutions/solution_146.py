from sympy import isprime


def is_valid(sq: int) -> bool:
    prime_diffs = [1, 3, 7, 9, 13, 27]
    composite_diffs = [11, 17, 19, 21, 23]
    for d in prime_diffs:
        if not isprime(sq + d):
            return False
    for d in composite_diffs:
        if isprime(sq + d):
            return False
    return True


def solve_p146(upper_bound: int) -> int:
    result = 0
    for k in range(1, upper_bound // 10 + 1):
        if k % 3 == 0 or k % 7 == 0 or k % 13 == 0:
            continue
        sq = k * k * 100
        if is_valid(sq):
            result += k * 10
    return result


if __name__ == '__main__':
    print(solve_p146(11))  # 10
    print(solve_p146(1000000))  # 1242490
    print(solve_p146(150000000))  # 676333270
