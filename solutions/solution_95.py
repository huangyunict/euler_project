def proper_divisors_sum(n: int) -> list[int]:
    result = [0, 0] + [1] * (n - 1)
    for p in range(2, n + 1):
        for q in range(p + p, n + 1, p):
            result[q] += p
    return result


def calc_loops(dp: list[int], n: int) -> list[int]:
    result = [-1] * (n + 1)
    for i in range(2, n + 1):
        if result[i] >= 0:
            continue
        nums = dict()
        k = i
        while True:
            if k == 0 or k > n or result[k] >= 0:
                loop_size = 0
                break
            if k in nums:
                loop_size = len(nums) - nums[k]
                break
            nums[k] = len(nums)
            k = dp[k]
        # Set loop size for seen numbers.
        for i in nums:
            result[i] = loop_size if nums[i] >= len(nums) - loop_size else 0
    return result


def solve_p95(n: int) -> int:
    dp = proper_divisors_sum(n)
    loops = calc_loops(dp, n)
    idx = 0
    for i in range(len(loops)):
        if loops[i] > loops[idx]:
            idx = i
    return idx


if __name__ == '__main__':
    print(solve_p95(10))  # 6
    print(solve_p95(15472))  # 12496
    print(solve_p95(1000000))  # 14316
