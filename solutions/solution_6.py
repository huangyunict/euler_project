def solve_p6(n: int) -> int:
    linear_sum = n * (n + 1) // 2
    square_sum = n * (n + 1) * (2 * n + 1) // 6
    return linear_sum * linear_sum - square_sum


if __name__ == '__main__':
    print(solve_p6(10))  # 2640
    print(solve_p6(100))  # 25164150
