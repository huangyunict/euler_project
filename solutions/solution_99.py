import math


def solve_p99(file_name: str) -> int:
    with open(file_name, 'r') as fp:
        line_num = 0
        best_line_num = 1
        best_value = 0.0
        for line in fp.readlines():
            a, e = (int(x) for x in line.strip().split(','))
            line_num += 1
            curr = e * math.log(a)
            if curr > best_value:
                best_value = curr
                best_line_num = line_num
    return best_line_num


if __name__ == '__main__':
    # Solution.
    print(solve_p99('../resources/p099_base_exp.txt'))  # 709
