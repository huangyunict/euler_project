# [Project Euler Problem 10](https://projecteuler.net/problem=10)

## 问题

**Summation of primes**

![题目截图](../images/problem_10.png)

## 答案

`142913828922`

## 解法

直接写程序用筛法暴力求解，算法部分的 Python 代码如下，完整的代码见 [solution_10.py](../solutions/solution_10.py)。
这里直接调用 `sympy.sieve.primerange()` 来生成质数数组。

```python
from sympy import sieve


def solve_p10(n: int) -> int:
    return sum([i for i in sieve.primerange(1, n+1)])
```
