# 1731. Dill

[Timus 1731](https://acm.timus.ru/problem.aspx?space=1&num=1731) · difficulty 106 · constructive

Original problem by Eugene Kurpilyansky (prepared by Sofia Tekhazheva), from the Ural Regional Team Programming Contest 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Choose the masses of n boxes of the first kind of dill and m boxes of
the second kind, all distinct positive integers up to 10⁹, such that
there is no way to give two neighbours one box of each kind with equal
total weights.

## Input

n and m (2 ≤ n, m ≤ 50).

## Output

The n masses of the first kind on one line and the m masses of the
second kind on the next. Any fitting masses are accepted.

## Examples

### Example 1

Input:

```
2 3
```

Output:

```
1 2
5 10 12
```

## Solution

Two gifts a + b and a′ + b′ share no box, and since all masses differ,
two sums with a common box differ anyway. So the condition is that all
the n·m sums a_i + b_j are distinct.

Take a_i = i for i = 1..n and b_j = (j + 1)·n + 1 for j = 0..m − 1.
Then a_i + b_j = (j + 1)·n + 1 + i, and since i runs over 1..n, the sum
tells both i and j, the way a number tells its last digit and the rest
in base n. All masses are distinct, and the largest is below 3000.
`O(n + m)`.

For the example this gives 1 2 and 3 5 7, with sums 4, 6, 8, 5, 7, 9.

Pitfalls:

- the answer always exists, so "It is a lie!" is never printed;
- the second kind must not repeat masses of the first, which is why
  it starts above n.

The checker verifies the counts, the range, the distinctness and that
all sums differ.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1731_constructive.cpp](1731_constructive.cpp) | G++ 13.2 x64 | constructive | O(n + m) | AC | 0.015 s | 380 KB |
| [1731_constructive.go](1731_constructive.go) | Go 1.14 x64 | constructive | O(n + m) | AC | 0.046 s | 1104 KB |
| [1731_constructive.java](1731_constructive.java) | Java 1.8 | constructive | O(n + m) | AC | 0.171 s | 1580 KB |
| [1731_constructive.py](1731_constructive.py) | Python 3.12 x64 | constructive | O(n + m) | AC | 0.093 s | 416 KB |
| [1731_constructive.rs](1731_constructive.rs) | Rust 1.75 x64 | constructive | O(n + m) | AC | 0.015 s | 224 KB |
