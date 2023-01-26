def solve_p301(n: int) -> int:
    result = 0
    for x in range(1, n + 1):
        if x ^ (2 * x) ^ (3 * x) == 0:
            result += 1
    return result


if __name__ == '__main__':
    print(solve_p301(pow(2, 30)))  # 2178309
