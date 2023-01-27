from math import gcd, isqrt


def solve_p504(m: int) -> int:
    result = 0
    all_range = list(range(1, m + 1))
    for a in all_range:
        for b in all_range:
            for c in all_range:
                for d in all_range:
                    cnt = (a * b + b * c + c * d + d * a - gcd(a, b) - gcd(b, c) - gcd(c, d) - gcd(d, a) + 2) // 2
                    root = isqrt(cnt)
                    if root * root == cnt:
                        result += 1
    return result


if __name__ == '__main__':
    print(solve_p504(4))  # 42
    print(solve_p504(100))  # 694687
