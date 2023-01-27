def calc_rep_unit(b: int, k: int) -> int:
    assert (pow(b,k)-1)%(b-1) == 0
    return (pow(b, k) - 1) // (b - 1)


def solve_p346(n: int) -> int:
    rep_units = set()
    rep_units.add(1)
    early_exit = False
    for b in range(2, n):
        k = 3
        while True:
            m = calc_rep_unit(b, k)
            if m >= n:
                if k == 3:
                    early_exit = True
                break
            rep_units.add(m)
            k += 1
        if early_exit:
            break
    return sum(rep_units)


if __name__ == '__main__':
    print(solve_p346(50))  # 171
    print(solve_p346(1000))  # 15864
    print(solve_p346(pow(10, 12)))  # 336108797689259276
