def solve_p9(n: int) -> int:
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            c = n - a - b
            if a * a + b * b == c * c:
                return a * b * c
    return -1


if __name__ == '__main__':
    print(solve_p9(1000))  # 31875000
