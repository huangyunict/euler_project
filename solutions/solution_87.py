import math
import sympy


def solve_p87(n: int) -> int:
    primes = list(sympy.primerange(1, int(math.isqrt(n)) + 1))
    valid = set()
    for p4 in primes:
        power4 = pow(p4, 4)
        if power4 >= n:
            break
        for p3 in primes:
            power3 = pow(p3, 3)
            if power4 + power3 >= n:
                break
            for p2 in primes:
                power2 = pow(p2, 2)
                if power4 + power3 + power2 >= n:
                    break
                valid.add(power4 + power3 + power2)
    return len(valid)


if __name__ == '__main__':
    print(solve_p87(50))  # 4
    print(solve_p87(50000000))  # 1097343
