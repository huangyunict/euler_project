def load_matrix(file_name: str) -> list[list[int]]:
    result = list()
    with open(file_name, 'r') as fp:
        for line in fp.readlines():
            result.append([int(x) for x in line.strip().split(',')])
    return result


def solve_sample() -> int:
    mat = [[131, 673, 234, 103, 18],
           [201, 96, 342, 965, 150],
           [630, 803, 746, 422, 111],
           [537, 699, 497, 121, 956],
           [805, 732, 524, 37, 331]]
    return min_path_sum(mat)


def min_path_sum(mat: list[list[int]]) -> int:
    rows = len(mat)
    cols = len(mat[0])
    # First row.
    dp = [0] * cols
    dp[0] = mat[0][0]
    for c in range(1, cols):
        dp[c] = dp[c - 1] + mat[0][c]
    # Other rows.
    for r in range(1, rows):
        ndp = [dp[0] + mat[r][0]]
        for c in range(1, cols):
            ndp.append(mat[r][c] + min(ndp[-1], dp[c]))
        dp, ndp = ndp, dp
    return dp[-1]


def solve_p81(file_name: str) -> int:
    return min_path_sum(load_matrix(file_name))


if __name__ == '__main__':
    print(solve_sample())  # 2427
    print(solve_p81('../resources/p081_matrix.txt'))  # 427337
