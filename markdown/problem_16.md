# [Project Euler Problem 16](https://projecteuler.net/problem=16)

## 问题

**Power Digit Sum**

![题目截图](../images/problem_16.png)

## 答案

`1366`

## 解法

在支持大整数的编程语言中可以直接求解，算法部分的 Python 代码如下，完整的代码见 [solution_16.py](../solutions/solution_16.py)。

```python
def solve_p16(n: int) -> int:
    return sum(int(x) for x in str(n))
```
