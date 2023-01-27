def sum_digit_squares(n: int) -> int:
    result = 0
    while n > 0:
        result += (n % 10) * (n % 10)
        n //= 10
    return result


def solve_p92() -> int:
    max_number = pow(10, 7) - 1
    dp = dict()
    # Prepare cached array.
    for i in range(1, sum_digit_squares(max_number) + 1):
        seen = set()
        k = i
        while k not in seen and k not in dp:
            seen.add(k)
            k = sum_digit_squares(k)
        reached = dp.get(k) if k in dp else 89 in seen
        for m in seen:
            dp[m] = reached
    # Loop over all numbers.
    result = 0
    for i in range(1, max_number + 1):
        if i in dp:
            if dp[i]:
                result += 1
        else:
            if dp[sum_digit_squares(i)]:
                result += 1
    return result


if __name__ == '__main__':
    print(solve_p92())  # 8581146
