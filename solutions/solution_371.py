import numpy as np


def build_status_vector_map(n: int) -> dict:
    """ Build status vector map, which maps status string to matrix index.

    :param n: the given number, must be even.
    :return: the map from status string to matrix index.
    """
    idx_map = dict()
    idx_map['w'] = 0
    for k in range(0, n // 2):
        idx_map['{}f'.format(k)] = len(idx_map)
    for k in range(0, n // 2):
        idx_map['{}t'.format(k)] = len(idx_map)
    return idx_map


def build_transfer_matrix(n: int, idx_map: dict) -> np.ndarray:
    """ Build probability transfer matrix such that: M(i,j)=p(i|j).

    :param n: the given number, must be even.
    :param idx_map: the map from status string to matrix index.
    :return: the probability transfer matrix.
    """
    matrix = np.zeros((n + 1, n + 1))
    for k in range(0, n // 2):
        from_idx = idx_map.get('{}f'.format(k))
        # From `kf` to `kf`.
        to_idx = idx_map.get('{}f'.format(k))
        matrix[to_idx, from_idx] = (k + 1) / n
        # From `kf` to `kt`.
        to_idx = idx_map.get('{}t'.format(k))
        matrix[to_idx, from_idx] = 1 / n
        # From `kf` to `w`.
        to_idx = idx_map.get('w')
        matrix[to_idx, from_idx] = k / n
        # From `kf` to `(k+1)f`.
        if k + 1 < n // 2:
            to_idx = idx_map.get('{}f'.format(k + 1))
            matrix[to_idx, from_idx] = (n - 2 * k - 2) / n
    for k in range(0, n // 2):
        from_idx = idx_map.get('{}t'.format(k))
        # From `kt` to `kt`.
        to_idx = idx_map.get('{}t'.format(k))
        matrix[to_idx, from_idx] = (k + 1) / n
        # From `kt` to `w`
        to_idx = idx_map.get('w')
        matrix[to_idx, from_idx] = (k + 1) / n
        # From `kt` to `(k+1)t`.
        if k + 1 < n // 2:
            to_idx = idx_map.get('{}t'.format(k + 1))
            matrix[to_idx, from_idx] = (n - 2 * k - 2) / n
    return matrix


def solve_p371(n: int) -> float:
    # Build status vector map, which maps status string to matrix index.
    idx_map = build_status_vector_map(n)
    # Build transfer matrix.
    matrix = build_transfer_matrix(n, idx_map)
    # Probability vector
    probs = np.zeros((n + 1))
    probs[1] = 1.0
    # Multiple matrix to vector.
    c = 0
    result = 0.0
    while True:
        c += 1
        probs = matrix.dot(probs)
        win_prob = probs[0]
        inc = c * win_prob
        result += inc
        if c >= 2 and inc < 1e-10:
            break
    return result


if __name__ == '__main__':
    print("{:.8f}".format(solve_p371(6)))  # 4.60666667
    print("{:.8f}".format(solve_p371(1000)))  # 40.66368097
