from sortedcontainers import SortedSet
from sympy import sieve


def get_relatives(prime: int):
    prime_str = str(prime)
    # Replace one character.
    for i in range(len(prime_str)):
        for d in range(0 if i > 0 else 1, 10):
            t = prime_str[:i] + str(d) + prime_str[i + 1:]
            if t != prime_str:
                yield int(t)
    # Add one character to the left.
    for d in range(1, 10):
        yield int(str(d) + prime_str)
    # Delete first character.
    if len(prime_str) > 1:
        yield int(prime_str[1:])


def solve_p425(n: int) -> int:
    primes = set(sieve.primerange(2, n + 1))
    # Sorted BFS queue, so each time the minimal element in the queue is expanded.
    q = SortedSet()
    q.add(2)
    # Visited dictionary, mapping the element to the maximal value in the path.
    relatives = dict()
    relatives[2] = 1
    while len(q) > 0:
        curr = q[0]
        q.remove(curr)
        for t in get_relatives(curr):
            # Already visited.
            if t in relatives:
                continue
            if t in primes:
                # Choose the max.
                relatives[t] = max(curr, relatives[curr])
                # Add to the queue.
                q.add(t)
    # Sum up.
    result = 0
    for prime in primes:
        if prime not in relatives or relatives[prime] > prime:
            result += prime
    return result


if __name__ == '__main__':
    print(solve_p425(pow(10, 3)))  # 431
    print(solve_p425(pow(10, 4)))  # 78728
    print(solve_p425(pow(10, 7)))  # 46479497324
