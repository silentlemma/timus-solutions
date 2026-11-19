# 1009. Counting base-K numbers without two adjacent zeros

[Timus 1009](https://acm.timus.ru/problem.aspx?space=1&num=1009) · difficulty 95 · dp, combinatorics

Original problem from the Ural State University Championship 1997.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Count the `N`-digit numbers in base `K` (the first digit is not zero) whose
digits contain no two zeros in a row. `2 ≤ K ≤ 10`, `N ≥ 2`, `N + K ≤ 18`.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N` and `K`, each on its own line.

## Output

The count.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3
10
```

Output:

```
891
```

### Example 2

Input:

```
2
2
```

Output:

```
2
```

## Solution

**Dynamic programming.** Count valid prefixes by their last digit: `zero` end
with `0`, `other` with a nonzero digit. For one digit, `zero = 0` and
`other = K - 1`. Appending a digit:

- a zero may follow only a nonzero digit: `zero' = other`;
- a nonzero digit may follow anything: `other' = (zero + other) · (K - 1)`.

After `N` digits the answer is `zero + other`. `O(N)` time.

**Combinatorics.** A number with `z` zeros has them among the `N - 1`
positions after the first, no two adjacent: `C(N - z, z)` ways; each of the
other `N - z` digits takes one of `K - 1` values. The answer is
`Σ C(N - z, z) · (K - 1)^(N - z)` over `0 ≤ z ≤ N / 2`.

Pitfalls:

- the largest answer, `1 434 392 064` (`N = 11`, `K = 7`), is close to the
  32-bit limit, and intermediate values of a careless formula may overflow:
  use 64-bit integers;
- for `K = 2` the answer is a Fibonacci number, a handy check.

## Optimized solutions

The optimized Java solution parses the two numbers byte by byte from
`System.in` instead of using `Scanner`: 0.093 s instead of 0.125 s and
336 KB instead of 1576 KB.

`1009_dp_optimized.go`. Go keeps the two-state digit DP. Portable byte input and a fixed output buffer replace fmt-based parsing and printing; only the counts for the previous prefix are retained. There are O(N) bounded-integer updates and O(1) auxiliary storage.

Compared with `1009_dp.go`: time 0.031 s → 0.015 s; memory 1104 KB → 796 KB.

`1009_dp.py`. The new Python source uses digit DP instead of the combinatorial sum. Let z and q count prefixes ending in zero and in a nonzero digit. Start with (z,q)=(0,K-1) to exclude a leading zero, then update (z,q)=(q,(z+q)(K-1)). A zero can follow only a nonzero digit, while any prefix admits K-1 nonzero extensions. This counts exactly the valid strings in O(N) updates and O(1) auxiliary integer slots. The combinatorial teaching source remains separate.

Compared with `1009_combinatorics.py`: time 0.078 s → 0.109 s; memory 404 KB → 196 KB.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: the two-state DP.
- **C++** and **Python** also have the closed sum; Python's `math.comb`
  computes the binomial coefficients exactly.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1009_combinatorics.cpp](1009_combinatorics.cpp) | G++ 13.2 x64 | combinatorics | O(N^2) | AC | 0.001 s | 128 KB | 11277725 |
| [1009_combinatorics.py](1009_combinatorics.py) | Python 3.12 x64 | combinatorics | O(N^2) | AC | 0.078 s | 404 KB | 11277735 |
| [1009_dp.cpp](1009_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB | 11277718 |
| [1009_dp.go](1009_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1104 KB | 11277734 |
| [1009_dp.java](1009_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 1576 KB | 11277739 |
| [1009_dp.rs](1009_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 216 KB | 11277743 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1009_dp_optimized.java](1009_dp_optimized.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 336 KB | 11303698 |
| [1009_dp_optimized.go](1009_dp_optimized.go) | Go 1.14 x64 | dp | O(N) | AC | 0.015 s | 796 KB | 11325041 |
| [1009_dp.py](1009_dp.py) \* | PyPy 3.10 x64 | dp | O(N) | AC | 0.109 s | 196 KB | 11324917 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
