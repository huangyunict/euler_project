import sympy
from sympy import continued_fraction_convergents, continued_fraction_iterator


def solve_pell(d: int) -> int:
    it = continued_fraction_convergents(
        continued_fraction_iterator(sympy.sqrt(d)))
    while True:
        r = next(it)
        if r.p * r.p - d * r.q * r.q == 1:
            return r.p


def solve_p66(max_d: int) -> int:
    result = 0
    best_x = 0
    for d in sympy.primerange(2, max_d + 1):
        x = solve_pell(d)
        if x > best_x:
            best_x = x
            result = d
    return result


if __name__ == '__main__':
    print(solve_p66(7))  # 5
    print(solve_p66(1000))  # 661
