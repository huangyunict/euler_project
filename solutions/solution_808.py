import math

import sympy
from sortedcontainers import SortedSet


def solve_p808(cnt: int) -> int:
    ll = 0
    results = SortedSet()
    while len(results) < cnt:
        ll += 1
        for prime in sympy.sieve.primerange(pow(10, ll - 1), pow(10, ll)):
            sq = prime * prime
            if sympy.ntheory.is_palindromic(sq):
                continue
            # Reverse integer.
            sqr = int(str(sq)[::-1])
            sr = math.isqrt(sqr)
            if sr * sr != sqr:
                continue
            if sympy.isprime(sr):
                results.add(sq)
                results.add(sqr)
    return sum(results[:cnt])


if __name__ == '__main__':
    print(solve_p808(2))  # 1130
    print(solve_p808(50))  # 3807504276997394
