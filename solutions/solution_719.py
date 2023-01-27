from math import isqrt


def check_split_sum(expected_sum: int, square_str: str) -> bool:
    """Check if integer square_str (as a string) can be split into 2 or more parts added up to expected_sum.

    :param expected_sum: expected sum of parts.
    :param square_str: integer represented as a string.
    :return: True if it is able to find a split, False otherwise.
    """
    assert expected_sum >= 0
    if len(square_str) == 0:
        return expected_sum == 0
    for next_pos in range(1, 1 + len(square_str)):
        next_sum = expected_sum - int(square_str[:next_pos])
        if next_sum < 0:
            break
        if check_split_sum(next_sum, square_str[next_pos:]):
            return True
    return False


def solve_p719(n: int) -> int:
    max_sqrt = isqrt(n + 1)
    result = 0
    # Single digit numbers (sqrt(1)...sqrt(9)) cannot be split into two parts.
    for root in range(4, 1 + max_sqrt):
        square = root * root
        # Optimize for mod 9.
        if root % 9 != square % 9:
            continue
        # Check split sum recursively.
        if check_split_sum(root, str(square)):
            result += square
    return result


if __name__ == '__main__':
    print(solve_p719(pow(10, 4)))  # 41333
    print(solve_p719(pow(10, 12)))  # 128088830547982
