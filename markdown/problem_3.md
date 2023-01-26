# [Project Euler Problem 3](https://projecteuler.net/problem=3)

## 问题

**Largest prime factor**

![题目截图](../images/problem_3.png)

## 答案

`6857`

## 解法

题目问的是正整数 600851475143 的最大质因数，直接对这个整数进行质因素分解，然后取最大的那个即可。

算法部分的 Python 代码如下，这里直接调用了 `sympy.primefactors()` 作质因素分解。
完整的代码见 [solution_3.py](../solutions/solution_3.py)。

```python
from sympy import primefactors


def solve_p3(n):
    return primefactors(n)[-1]
```

输出答案是 `6857` ，事实上 `600851475143 = 71 * 839 * 1471 * 6857` 。

