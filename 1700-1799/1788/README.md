# 1788. On the Benefits of Umbrellas

[Timus 1788](https://acm.timus.ru/problem.aspx?space=1&num=1788) · difficulty 162 · greedy

Original problem by Sofia Tekhazheva (prepared by Denis Dublennykh), from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n girls without umbrellas and m boys with umbrellas leave a party in
the rain. Each boy may walk one girl under his umbrella. A girl who
gets wet is upset by gᵢ. A boy who walks nobody is upset by bⱼ·k, where
k is the number of boys who do walk a girl. Paired girls and boys are
not upset. Find the smallest total upset.

## Input

n and m (1 ≤ n, m ≤ 100), then g₁, …, gₙ, then b₁, …, bₘ, all from 1
to 1000.

## Output

The smallest total upset.

## Examples

### Example 1

Input:

```
2 4
1 100
10 8 6 4
```

Output:

```
19
```

## Solution

Fix the number of pairs k. Then it is best to keep dry the k girls with
the largest gᵢ, and to let the k boys with the largest bⱼ do the
walking, since everyone left alone costs their own value (times k for
the boys). So the total is the sum of the n − k smallest gᵢ plus k
times the sum of the m − k smallest bⱼ. Sort both lists and try every
k from 0 to min(n, m). `O((n + m)²)`.

In the example no pairs cost 101, and two pairs leave the boys with 6
and 4 at 2·10 = 20. One pair, with the girl who would be upset by 100,
leaves the girl with 1 and the boys with 8, 6 and 4 at 1·18, 19 in all.

Pitfalls:

- the boys' cost grows with k, so more pairs are not always better;
- k = 0 must be tried too: then no boy is upset at all;
- intermediate totals can reach 2,550,000 (test 06, k = 49 or 50), even
  when the answer is zero; the largest possible optimal answer is 99,000.
  Both fit in 32-bit integers.

The answers agree with an independent accepted implementation on 150
random groups: any groups, small ones, and sensitive girls with calm
boys.

## Optimized solutions

The optimized C++ solution reads and prints with `scanf` and `printf`
instead of `iostream`, whose runtime is not needed for at most 202
numbers; the sorting and the sums are the same:
{1788_greedy_optimized.cpp}.

The optimized Java solution reads the input in 4 KB blocks and parses
the numbers by hand instead of `Scanner`, whose regular-expression
machinery costs time and memory to load; the sorting and the sums are
the same: {1788_greedy_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1788_greedy_optimized.cpp`: time reduction +0.00%; memory reduction
  +57.43%; base: `1788_greedy.cpp`.

- `1788_greedy_optimized.java`: time reduction +25.60%; memory reduction
  +78.62%; base: `1788_greedy.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1788_greedy.go](1788_greedy.go).
- [1788_greedy.rs](1788_greedy.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1788_greedy.cpp](1788_greedy.cpp) | G++ 13.2 x64 | greedy | O((n + m)^2) | AC | 0.015 s | 404 KB | 11304222 |
| [1788_greedy.go](1788_greedy.go) | Go 1.14 x64 | greedy | O((n + m)^2) | AC | 0.031 s | 1100 KB | 11289825 |
| [1788_greedy.java](1788_greedy.java) | Java 1.8 | greedy | O((n + m)^2) | AC | 0.125 s | 1852 KB | 11304227 |
| [1788_greedy.py](1788_greedy.py) | Python 3.12 x64 | greedy | O((n + m)^2) | AC | 0.093 s | 448 KB | 11304230 |
| [1788_greedy.rs](1788_greedy.rs) | Rust 1.75 x64 | greedy | O((n + m)^2) | AC | 0.046 s | 232 KB | 11304233 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1788_greedy_optimized.cpp](1788_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O((n + m)^2) | AC | 0.015 s | 172 KB | 11307198 |
| [1788_greedy_optimized.java](1788_greedy_optimized.java) | Java 1.8 | greedy | O((n + m)^2) | AC | 0.093 s | 396 KB | 11307199 |
