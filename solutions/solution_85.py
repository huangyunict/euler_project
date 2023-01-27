def count_rectangles(m: int, n: int) -> int:
    return m * (m + 1) * n * (n + 1) // 4


def solve_p85(rectangle_count: int) -> int:
    n = 1
    best_diff = -1
    best_m = 1
    best_n = 1
    while True:
        m = n
        while True:
            cnt = count_rectangles(m, n)
            diff = abs(cnt - rectangle_count)
            if best_diff < 0 or diff < best_diff:
                best_diff = diff
                best_m = m
                best_n = n
            if cnt > rectangle_count:
                break
            m += 1
        if count_rectangles(n, n) > rectangle_count:
            break
        n += 1
    return best_m * best_n


if __name__ == '__main__':
    print(solve_p85(18))  # 6
    print(solve_p85(2000000))  # 2772
