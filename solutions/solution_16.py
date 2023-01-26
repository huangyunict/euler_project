def solve_p16(n: int) -> int:
    result = 0
    while n > 0:
        result += n % 10
        n //= 10
    return result


if __name__ == '__main__':
    print(solve_p16(pow(2, 15)))  # 26
    print(solve_p16(pow(2, 1000)))  # 1366
