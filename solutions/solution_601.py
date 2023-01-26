import math


def calc_p(s: int, n: int) -> int:
    """Calculate the common multiples of (1,2,3,...,s), and find those cannot be divides by (s+1)

    :param s: given s.
    :param n: given n, n>=2.
    :return: return P(s,n), i.e. numbers of integers 1<k<n, such that k % lcm(1,2,...s)==0 and k % (s+1)!=0.
    """
    lcm1 = math.lcm(*range(1, s + 1))
    cnt1 = (n - 1) // lcm1 - 1 // lcm1
    lcm2 = math.lcm(lcm1, s + 1)
    cnt2 = (n - 1) // lcm2 - 1 // lcm2
    return cnt1 - cnt2


def solve_p601():
    return sum([calc_p(i, 4 ** i) for i in range(1, 32)])


if __name__ == "__main__":
    print(calc_p(3, 14))  # 1
    print(calc_p(6, pow(10, 6)))  # 14286
    print(solve_p601())  # 1617243
