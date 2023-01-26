import sympy
from sortedcontainers import SortedDict


def solve_p500(n: int) -> int:
    mod = 500500507
    primes = list()
    prime_counts = list()
    # Open set that contains the value mapped to the prime index.
    sd = SortedDict()
    sd[2] = 0
    primes.append(2)
    prime_counts.append(0)
    for i in range(n):
        v, idx = sd.popitem(index=0)
        prime_counts[idx] += 1
        sd[v * v] = idx
        if idx + 1 == len(primes):
            primes.append(sympy.nextprime(primes[-1]))
            prime_counts.append(0)
            sd[primes[-1]] = len(primes) - 1
    # Calculate: result=\product_i prime[i]*(2^prime_counts[i]-1)
    result = 1
    for i in range(len(primes)):
        result = result * pow(primes[i], pow(2, prime_counts[i]) - 1, mod) % mod
    return result


if __name__ == '__main__':
    print(solve_p500(4))  # 120
    print(solve_p500(500500))  # 35407281
