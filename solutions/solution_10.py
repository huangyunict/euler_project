from sympy import sieve


def solve_p10(n: int) -> int:
    return sum([i for i in sieve.primerange(1, n + 1)])


if __name__ == '__main__':
    print(solve_p10(10))  # 17
    print(solve_p10(2000000))  # 142913828922
