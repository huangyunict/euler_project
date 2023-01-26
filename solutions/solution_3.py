from sympy import primefactors


def solve_p3(n: int) -> int:
    return primefactors(n)[-1]


if __name__ == '__main__':
    print(solve_p3(13195))  # 29
    print(solve_p3(600851475143))  # 6857
