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
    # Loop over columns.
    dp = [0] * rows
    for c in range(cols):
        ndp = [-1] * rows
        # Starting from row r in previous column.
        for r in range(rows):
            # Move up.
            up_cost = dp[r]
            for nr in range(r, -1, -1):
                up_cost += mat[nr][c]
                if ndp[nr] < 0 or up_cost < ndp[nr]:
                    ndp[nr] = up_cost
            # Move down.
            down_cost = dp[r]
            for nr in range(r, rows):
                down_cost += mat[nr][c]
                if ndp[nr] < 0 or down_cost < ndp[nr]:
                    ndp[nr] = down_cost
        # Swap.
        dp, ndp = ndp, dp
    return min(dp)


def solve_p82(file_name: str) -> int:
    return min_path_sum(load_matrix(file_name))


if __name__ == '__main__':
    print(solve_sample())  # 994
    print(solve_p82('../resources/p082_matrix.txt'))  # 260324
