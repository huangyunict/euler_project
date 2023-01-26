import itertools


def solve_p24_naive(n: int) -> int:
    l = list(itertools.permutations(list(range(0, 10))))[n - 1]
    return int(''.join(str(x) for x in l))


def solve_p24(n: int) -> int:
    result = 0
    rest = n - 1
    # Number of permutations: 0!, 1!, ..., 9!
    perm = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    digits = list(range(0, 10))
    for i in range(1, 11):
        t = rest // perm[10 - i]
        rest %= perm[10 - i]
        result *= 10
        result += digits[t]
        del digits[t]
    return result


if __name__ == '__main__':
    print(solve_p24_naive(1000000))  # 2783915460
    print(solve_p24(1000000))  # 2783915460
