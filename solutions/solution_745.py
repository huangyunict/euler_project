import math


def solve_p745(n: int) -> int:
    mod = 1000000007
    max_k = math.isqrt(n)
    # Array c[k] is the number of integers with `k*k` as the max perfect square factor.
    c = [0] * (1 + max_k)
    # Last index of a non-one value.
    last_index = -1
    for k in range(max_k, 0, -1):
        c[k] = n // (k * k) % mod
        i = 2
        while k * i <= max_k:
            # Small optimization.
            if 0 < last_index < k * i:
                c[k] = (c[k] + mod - (max_k//k - i + 1)) % mod
                break
            c[k] = (c[k] + mod - c[k * i]) % mod
            i += 1
        if last_index < 0 and c[k] != 1:
            last_index = k
    # Calculate result.
    result = 0
    for i in range(1, len(c)):
        result = (result + c[i] * i * i) % mod
    return result


if __name__ == '__main__':
    print(solve_p745(10))  # 24
    print(solve_p745(100))  # 767
    print(solve_p745(pow(10, 14)))  # 94586478
