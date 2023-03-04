from euler_common import multinomial_mod_prime, mod_prime_inv


def solve_p743(k: int, n: int, mod: int) -> int:
    assert n % k == 0
    result = 0
    # Initialize: x=z=k//2, y=k%2.
    c = multinomial_mod_prime(k, [k // 2, k % 2, k // 2], mod)
    result = (result + c * pow(2, k % 2 * n // k, mod)) % mod
    # Iterative.
    for y in range(k % 2 + 2, k + 1, 2):
        x = z = (k - y) // 2
        # Calculate `c = k! / (x! y! z!)` incrementally.
        # C(k;x,y,z)=k!/(x! y! z!)= (x+1)*(z+1)/((y-1)*y) * C(k;x+1,y-2,z+1).
        # We have to cancel out powers of mod before calculate the modulo inverse.
        a = (x + 1) * (z + 1)
        b = y * (y - 1)
        while a % mod == 0 and b % mod == 0:
            a //= mod
            b //= mod
        c = c * a * mod_prime_inv(b, mod) % mod
        result = (result + c * pow(2, y * n // k, mod)) % mod
    return result


if __name__ == '__main__':
    print(solve_p743(1, 1, 1000000007))  # 2
    print(solve_p743(1, 2, 1000000007))  # 4
    print(solve_p743(3, 3, 1000000007))  # 20
    print(solve_p743(3, 3, 17))  # 3
    print(solve_p743(3, 9, 1000000007))  # 560
    print(solve_p743(4, 20, 1000000007))  # 1060870
    print(solve_p743(4, 20, 67))  # 59
    print(solve_p743(pow(10, 8), pow(10, 16), 1000000007))  # 259158998
