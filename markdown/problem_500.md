# [Project Euler Problem 500](https://projecteuler.net/problem=500)

## 问题

**Problem 500!!!**

![题目截图](../images/problem_500.png)

## 答案

`35407281`

## 解法

如果正整数`n`的质因子分解是`n=p_1^a_1*p_2^a_2*...`，那么`n`的因子个数是`(a_1+1)*(a_2+1)*...`。
题目要求的因子数是`2`的整数幂，也就是说对于任何一个质因子的指数`a_k`来说，要求`(a_k+1)`是`2`的整数幂。

因为需要最终的结果最小，因此可以维护一个可能的扩展集合，每次扩展最小的。
例如：假设当前的数字是 `2^3 * 3^1 * 5^1` ，
那么下一次在其他质因子次数不变的情况下，可能扩展其中之一到`2^7`,`3^3`,`5^3`,`7^1`之一。

算法部分的 Python 代码如下，完整的代码见 [solution_500.py](../solutions/solution_500.py)。

```python
import sympy
from sortedcontainers import SortedDict


def solve_p500(n: int) -> int:
    mod = 500500507
    primes = list()
    prime_counts = list()
    # Open set that contains the value mapped to the prime index.
    sd = SortedDict()
    sd[2] = 0
    primes.append(2)
    prime_counts.append(0)
    for i in range(n):
        v, idx = sd.popitem(index=0)
        prime_counts[idx] += 1
        sd[v * v] = idx
        if idx + 1 == len(primes):
            primes.append(sympy.nextprime(primes[-1]))
            prime_counts.append(0)
            sd[primes[-1]] = len(primes) - 1
    # Calculate: result=\product_i prime[i]*(2^prime_counts[i]-1)
    result = 1
    for i in range(len(primes)):
        result = result * pow(primes[i], pow(2, prime_counts[i]) - 1, mod) % mod
    return result
```
