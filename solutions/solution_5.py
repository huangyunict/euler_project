from sympy import lcm


def solve_p5(n: int) -> int:
    return lcm(range(1, n + 1))


if __name__ == '__main__':
    print(solve_p5(10))  # 2520
    print(solve_p5(20))  # 232792560
