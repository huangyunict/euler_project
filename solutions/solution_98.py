from assertpy import assert_that
import math


def load_words(file_name: str) -> list[str]:
    result = list()
    with open(file_name, 'r') as fp:
        for line in fp.readlines():
            result.extend(
                [x.replace('"', '') for x in line.strip().split(',')])
    result = [x for x in result]
    return result


def get_pattern(s: str) -> str:
    mc = dict()
    for c in s:
        mc[c] = mc.get(c, 0) + 1
    return '_'.join([str(x) for x in sorted(mc.values())])


def get_chart_digit_map(word: str, square: str) -> dict[str, str]:
    d = dict()  # map from character to digit
    assert len(word) == len(square)
    for i in range(len(word)):
        si = square[i]
        wi = word[i]
        if wi not in d:
            d[wi] = si
        else:
            if d.get(wi) != si:
                return dict()
    return d


def check_squares(words: list[str], char_digit_map: dict[str, str]) -> bool:
    cnt = 0
    for word in words:
        # Replace word to number.
        digits = list()
        for c in word:
            assert c in char_digit_map
            digits.append(char_digit_map[c])
        # Check leading zeros.
        if digits[0] == '0':
            continue
        # Check squares.
        num = int(''.join(digits))
        if math.isqrt(num) * math.isqrt(num) == num:
            cnt += 1
        if cnt >= 2:
            return True
    return False


def largest_square(words: list[str]) -> int:
    max_word_len = max([len(x) for x in words])
    max_root_len = (max_word_len + 1) // 2
    # Patterns of input words: pattern -> anagram -> words.
    word_map = dict()
    for word in words:
        pattern = get_pattern(word)
        if pattern not in word_map:
            word_map[pattern] = dict()
        anagram = ''.join(sorted(word))
        if anagram not in word_map[pattern]:
            word_map[pattern][anagram] = list()
        word_map[pattern][anagram].append(word)
    # Loop square numbers larger to litter and check squares.
    for r in range(pow(10, max_root_len) - 1, 0, -1):
        sq_str = str(r * r)
        pattern = get_pattern(sq_str)
        if pattern not in word_map:
            continue
        for anagram in word_map[pattern]:
            if len(word_map[pattern][anagram]) < 2:
                continue
            for i in range(len(word_map[pattern][anagram])):
                word = word_map[pattern][anagram][i]
                char_digit_map = get_chart_digit_map(word, sq_str)
                if len(char_digit_map) == 0:
                    continue
                if check_squares(word_map[pattern][anagram], char_digit_map):
                    return int(sq_str)
    return -1


def solve_p98(file_name: str) -> int:
    return largest_square(load_words(file_name))


if __name__ == '__main__':
    # Verify.
    assert_that(largest_square(['CARE', 'RACE'])).is_equal_to(9216)
    assert_that(largest_square(['BROAD', 'BOARD'])).is_equal_to(18769)
    # Solution.
    print(solve_p98('resources/p98_words.txt'))  # 18769
