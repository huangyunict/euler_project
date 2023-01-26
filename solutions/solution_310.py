def get_all_squares(n: int) -> list[int]:
    """ Return all positive square numbers that are less than or equal to n.

    :param n: the upper bound (inclusive).
    :return: all square numbers that are less than or equal to n.
    """
    result = list()
    k = 1
    while k * k <= n:
        result.append(k * k)
        k += 1
    return result


def map_square_nim(n: int) -> list[int]:
    """ Map square nim #k to basic nim *k for all 0<=k<=n.

    :param n: the length of square nim heap.
    :return: the list of mapped the length of basic nim heap.
    """
    squares = get_all_squares(n)
    result = [0]
    for k in range(1, n + 1):
        # Calculate sub nim set.
        sub_nim_set = set()
        for sq in squares:
            if sq > k:
                break
            sub_nim_set.add(result[k - sq])
        # Find minimum excluded value in sub nim set.
        for mex in range(k + 1):
            if mex not in sub_nim_set:
                result.append(mex)
                break
    return result


def solve_p310_naive(n: int) -> int:
    nim_values = map_square_nim(n)
    # Get the count of mapped basic nim values.
    nim_counts = dict()
    for nim in nim_values:
        nim_counts[nim] = nim_counts.get(nim, 0) + 1
    # Loop and count.
    result = 0
    for a in range(n + 1):
        for b in range(a, n + 1):
            x = nim_values[a] ^ nim_values[b]
            result += nim_counts.get(x, 0)
            # Remove mapped basic nim value of b from nim counts.
            nim_counts[nim_values[b]] -= 1
        # Add back removed mapped basic nim values of b.
        for b in range(a, n + 1):
            nim_counts[nim_values[b]] += 1
        # Remove mapped basic nim of a from nim counts.
        nim_counts[nim_values[a]] -= 1
    return result


def solve_p310(n: int) -> int:
    nim_values = map_square_nim(n)
    # Get the count of mapped basic nim values.
    nim_counts = dict()
    for nim in nim_values:
        nim_counts[nim] = nim_counts.get(nim, 0) + 1
    # Loop and count.
    result = 0
    for a in range(n + 1):
        # Calculate zero count of given `a`, which corresponds to the count of `a<=b=c<=n`.
        zero_count = (n + 1 - a) if nim_values[a] == 0 else 0
        # Calculate current count of given `a`, and `a<=b<=n,a<=c<=n`.
        curr_count = 0
        for b_nim, b_cnt in nim_counts.items():
            x = nim_values[a] ^ b_nim
            curr_count += b_cnt * nim_counts.get(x, 0)
        # Adjust current count from condition `a<=b<=n,a<=c<=n` to `a<=b<=c<=n`.
        assert (curr_count + zero_count) % 2 == 0
        result += (curr_count + zero_count) // 2
        # Remove mapped basic nim of a from nim counts for the next round.
        nim_counts[nim_values[a]] -= 1
    return result


if __name__ == '__main__':
    print(solve_p310_naive(29))  # 1160
    print(solve_p310(29))  # 1160
    print(solve_p310(100000))  # 2586528661783
