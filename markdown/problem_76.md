# [Project Euler Problem 76](https://projecteuler.net/problem=76)

## 问题

**Counting summations**

![题目截图](../images/problem_76.png)

## 答案

`190569291`

## 作弊解法

将一个正整数表示成不大于其自身的一个或几个正整数的无序和的过程叫做拆分(partition)。
定义拆分函数(partition function)对于给定`n`，返回对应的拆分的数目`p(n)`。

查找[维基百科](https://en.wikipedia.org/wiki/Partition_function_(number_theory))页面，上面给出了例子`p(100)=190569292`。
去除只包括自身的一种拆分，立即可以得到本题答案`190569291`。

## 递归解法

令`f(n,k)`为对给定`n`进行拆分且拆分出来的允许的最大项为`k`的数目，显然`p(n)=f(n,n)`。

- 初始条件：`f(0,k)=0`。
- 递归公式：`f(n,k)=f(n-1,1)+f(n-2,2)+...+f(n-k,k)`。

算法部分的 Python 代码如下，完整的代码见 [solution_76.py](../solutions/solution_76.py)。

```python
def get_partitions_dp(n: int, k: int, dp: dict) -> int:
    if n == 0:
        return 1
    if n < k:
        return get_partitions_dp(n, n, dp)
    if (n, k) in dp:
        return dp.get((n, k))
    result = 0
    for first in range(1, min(n, k) + 1):
        sub = get_partitions_dp(n - first, first, dp)
        result += sub
    dp[(n, k)] = result
    return result


def solve_p76_dp(n: int) -> int:
    dp = dict()
    return get_partitions_dp(n, n, dp) - 1
```

## 欧拉生成函数解法

根据生成函数和欧拉的[五边形数定理](https://en.wikipedia.org/wiki/Pentagonal_number_theorem)，
有如下递归公式成立：`p(n)=p(n-1)+p(n-2)-p(n-5)-p(n-7)+p(n-12)+p(n-15)-p(n-22)...`，
其中上述的每一项是`(-1)^{k+1}p(n-k(3k-1)/2)`。
通过这个公式，可以快速递归求拆分函数的值。

算法部分的 Python 代码如下，完整的代码见 [solution_76.py](../solutions/solution_76.py)。

```python
def pentagonal(n: int) -> int:
    """ Return generalized pentagonal numbers, n could be negative.

    :param n: the input parameter.
    :return: the generalized pentagonal number.
    """
    return (3 * n * n - n) // 2


def get_partitions(n: int, dp: dict) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in dp:
        return dp.get(n)
    result = 0
    for k in range(-n - 1, n + 1):
        # Skip k=0.
        if k == 0:
            continue
        g = pentagonal(k)
        result += (-1 if k % 2 == 0 else 1) * get_partitions(n - g, dp)
    dp[n] = result
    return result


def solve_p76(n: int) -> int:
    dp = dict()
    get_partitions(n, dp)
    return dp[n] - 1
```
