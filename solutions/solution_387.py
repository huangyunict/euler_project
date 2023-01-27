from sympy import isprime


def calc(num: int, digits_sum: int, max_num: int) -> int:
    result = 0
    if num >= max_num:
        return result
    # Check right truncatable Harshad numbers.
    if num % digits_sum != 0:
        return result
    # Check strong right truncatable Harshad numbers.
    if isprime(num // digits_sum):
        for last in [1, 3, 7, 9]:
            next_num = num * 10 + last
            # Check strong, right truncatable Harshad primes.
            if next_num < max_num and isprime(next_num):
                result += next_num
    # Extend right truncatable Harshad numbers.
    for last in range(10):
        result += calc(num * 10 + last, digits_sum + last, max_num)
    return result


def solve_p387(max_num: int) -> int:
    result = 0
    for seed in range(1, 10):
        result += calc(seed, seed, max_num)
    return result


if __name__ == '__main__':
    print(solve_p387(10000))  # 90619
    print(solve_p387(pow(10, 14)))  # 696067597313468
