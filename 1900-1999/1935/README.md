# 1935. Minimum Sheets with Reorderable Clearances

[Timus 1935](https://acm.timus.ru/problem.aspx?space=1&num=1935) · difficulty 80 · greedy

Original problem from Open Ural FU Championship 2012 | by Tatiana Sharypova (prepared by Oleg Dolgorukov).

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Place n thin objects between the sheets of a book, in any order.
Object i requires at least a_i sheets between itself and each neighboring
object or cover. The same gap must satisfy both adjacent objects.
Find the minimum total number of sheets. Limits: 1 second, 64 MB.

## Input

The first line contains n, 1≤n≤100. The next line contains n integers
a_i, 1≤a_i≤100. The input order does not restrict placement order.

## Output

One integer: the minimum sufficient sheet count.

## Checking

Outputs are compared token by token.

## Examples

```
3
5 10 3
```

```
28
```

## Solution

The answer is the sum of all requirements plus the largest one, S + M.

It cannot be less: take an object with the largest requirement M. Each
object to its left needs its own gap on its left side, each object to
its right needs its own gap on its right side, and the largest object
needs both of its gaps. These are n + 1 different gaps, and together
they hold at least S + M sheets.

It is enough: sort the requirements a₁ ≤ … ≤ aₙ and put the objects in
this order with a₁ sheets before the first, a_(i+1) sheets between
objects i and i + 1, and aₙ after the last. Every gap holds what the
larger of its neighbours needs, and the total is S + M. `O(n)`; the
program does not need to sort.

Pitfalls:

- neighbours share a gap: it needs the larger requirement, not the sum;
- the order of the input does not matter: 100, 1, 100 needs 301 sheets,
  not 400;
- one object needs 2a₁ sheets.

## Optimized solutions

The optimized C++ solution reads with `scanf` instead of `iostream` and
takes the sum and the maximum while reading, without storing the
requirements: 124 KB instead of 428 KB.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1935_greedy.cpp](1935_greedy.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 428 KB | 11291786 |
| [1935_greedy.go](1935_greedy.go) | Go 1.14 x64 | greedy | O(n) | AC | 0.015 s | 1092 KB | 11291790 |
| [1935_greedy.java](1935_greedy.java) | Java 1.8 | greedy | O(n) | AC | 0.109 s | 1720 KB | 11303361 |
| [1935_greedy.py](1935_greedy.py) | Python 3.12 x64 | greedy | O(n) | AC | 0.078 s | 332 KB | 11291793 |
| [1935_greedy.rs](1935_greedy.rs) | Rust 1.75 x64 | greedy | O(n) | AC | 0.015 s | 236 KB | 11291800 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1935_greedy_optimized.cpp](1935_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(n) | AC | 0.015 s | 124 KB | 11303651 |
