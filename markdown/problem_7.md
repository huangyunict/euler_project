# [Project Euler Problem 7](https://projecteuler.net/problem=7)

## 问题

**10001st Prime**

![题目截图](../images/problem_7.png)

## 答案

`104743`

## 解法

直接写程序用筛法求解，这里直接调用 `sympy.prime()` 函数来得到第`n`个质数。
算法部分的 Python 代码如下，完整的代码见 [solution_7.py](../solutions/solution_7.py)。

```python
from sympy import prime


def solve_p7(n: int) -> int:
    return prime(n)
```
