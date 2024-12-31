# [Project Euler Problem 2](https://projecteuler.net/problem=2)

## 问题

**Even Fibonacci Numbers**

![题目截图](../images/problem_2.png)

## 答案

`4613732`

## 解法 1

直接写程序求解，从小到大生成 Fibonacci 数列，直到超过给定的上限，并在生成的过程中对偶数求和。

算法部分的 Python 代码如下，完整的代码见 [solution_2.py](../solutions/solution_2.py)。

```python
def solve_p2_naive(n: int) -> int:
    a = 0
    b = 1
    result = 0
    while b < n:
        if b % 2 == 0:
            result += b
        a, b = b, a + b
    return result
```

## 解法 2

记题目中的 Fibonacci 数列为 `F`。
容易证明 `F(3k+2)` 是偶数，即 `F(2)=2,F(5)=8,F(8)=34,F(11)=144,...` 是偶数。

令这个新数列为 `G` ，即 `G(k)=F(3k+2)`。
我们尝试写出 `G` 的递推公式。

根据定义，有如下方程组：

```
G(k+2) = F(3k+8)
G(k+1) = F(3k+5)
G(k) = F(3k+2)
F(3k+8) = F(3k+7) + F(3k+6)
F(3k+7) = F(3k+6) + F(3k+5)
F(3k+6) = F(3k+5) + F(3k+4)
F(3k+5) = F(3k+4) + F(3k+3)
F(3k+4) = F(3k+3) + F(3k+2)
```

消去所有的 `F` 项，可以得到：`G(k+2) = 4*G(k+1) + G(k)`。
根据这个公式，可以写程序求解。

算法部分的 Python 代码如下，完整的代码见 [solution_2.py](../solutions/solution_2.py)。

```python
def solve_p2(n: int) -> int:
    a = 0
    b = 2
    result = a
    while b < n:
        result += b
        a, b = b, a + 4 * b
    return result
```
