# 1431. Diplomas

[Timus 1431](https://acm.timus.ru/problem.aspx?space=1&num=1431) · difficulty 362 · greedy

Original problem by Stanislav Vasiliev, from the Seventh Ural State University Open Personal Contest, February 25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are N types of diplomas (N ≤ 18), from 1 to 30 of each. All
diplomas of a type hang in one row. A row holds one type, or two types
that strictly alternate, and every row must be symmetric about the
centre of the wall. Find the smallest number of rows.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the number of diplomas of each type.

## Output

The smallest number of rows.

## Examples

### Example 1

Input:

```
6
8 15 13 8 14 8
```

Output:

```
5
```

## Solution

A row of one type is always fine. Two types that strictly alternate
form ABAB…, and such a row reads the same backwards only when it starts
and ends with the same type, A B A … B A, so the counts differ by
exactly one. The answer is N minus the largest number of disjoint pairs
of types whose counts differ by one.

The pairs join neighbouring values of a chain 1, 2, …, 30. Going up the
chain, the types of count c not yet paired can only pair with count
c + 1 now, so pairing as many of them as possible right away is never
worse. `O(N + 30)`.

Pitfalls:

- equal counts cannot share a row: an alternating row of even length is
  not symmetric (test 06);
- in 1, 2, 3, 4 the pairs are 1–2 and 3–4, not 2–3 (test 07);
- several types may have the same count (tests 08, 12).

## Optimized solutions

Go and Rust store the frequencies of counts one through 30 in byte arrays. At each count, match as many types as possible with the unmatched types at the preceding count. Each match removes one required row. Carry only the unmatched remainder forward, so no sorted list or matching graph is needed. Both use fixed byte buffers for input and decimal output. Go accesses the standard input and output handles directly, and Rust uses the C runtime.

The accepted Rust 1.75 x64 run takes 0.031 s versus 0.015 s for the base and uses 56 KB versus 220 KB.

The accepted base implementations [1431_greedy.cpp](1431_greedy.cpp), [1431_greedy.java](1431_greedy.java), [1431_greedy.py](1431_greedy.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1431_greedy.cpp](1431_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + 30) | AC | 0.015 s | 128 KB | 11286206 |
| [1431_greedy.go](1431_greedy.go) | Go 1.14 x64 | greedy | O(N + 30) | AC | 0.015 s | 1076 KB | 11286207 |
| [1431_greedy.java](1431_greedy.java) \* | Java 1.8 | greedy | O(N + 30) | AC | 0.156 s | 1644 KB | 11286209 |
| [1431_greedy.py](1431_greedy.py) \* | Python 3.12 x64 | greedy | O(N + 30) | AC | 0.078 s | 420 KB | 11286208 |
| [1431_greedy.rs](1431_greedy.rs) | Rust 1.75 x64 | greedy | O(N + 30) | AC | 0.015 s | 220 KB | 11286210 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1431_greedy_optimized.go](1431_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(N + 30) | AC | 0.015 s | 348 KB | 11311231 |
| [1431_greedy_optimized.rs](1431_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N + 30) | AC | 0.031 s | 56 KB | 11311246 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
