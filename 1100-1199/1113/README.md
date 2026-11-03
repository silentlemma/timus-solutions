# 1113. The least fuel for a one-way trip with fuel depots

[Timus 1113](https://acm.timus.ru/problem.aspx?space=1&num=1113) · difficulty 265 · math

Original problem from the Bulgarian National Olympiad in Informatics, Day 2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A vehicle must cross `N` km of desert, burning one litre per kilometre.
It carries at most `M` litres, with `M < N ≤ 5M` and `N < 32000`. The
start has unlimited fuel, and the vehicle may leave any amount of fuel at
any point on the way and pick it up later. Find the least total amount
of fuel, in litres, needed to reach the target, rounded up to an integer.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N M` on one line.

## Output

The least amount of fuel, rounded up.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
1000 500
```

Output:

```
3837
```

## Solution

This is the one-way jeep problem. Work backwards from the target. The
last `M` km take one full load. To bring two loads to the start of that
stretch, a stretch of `M/3` km before it is crossed three times (there,
back, there), costing exactly one extra load; in general a stretch of
`M/(2k − 1)` km carries `k` loads at the price of one more. So add
stretches `M, M/3, M/5, …` until they reach the start; if `k` loads are
needed and the stretches before the last one cover `s` km, the fuel is
`(k − 1)·M + (N − s)·(2k − 1)`. With `5M ≥ N`, the exact maximum is
`k = 3092`: for `H_j = Σ_{i=1}^j 1/(2i − 1)`, we have
`H_3091 < 5 ≤ H_3092`. There are `O(k)` iterations, but big-integer
arithmetic takes `O(kB)` time and `O(B)` auxiliary space, where `B` is
the maximum big-integer length in machine words. Under the input bounds,
the other operand in each multiplication, division or gcd fits in one
machine word, so each operation takes `O(B)` word operations.

Pitfalls:

- the rounding up must be exact: the fuel is often an integer, and the
  floating-point sum of `M/(2i − 1)` lands just above it, adding one
  litre too many (for example `N = 59, M = 35` gives exactly 143, but a
  plain `double` computation prints 144);
- the stretches shrink only like the odd harmonic series, so `N = 5M`
  needs 3092 of them, not at most 3000 ([test 08](tests/08.in): `5 1`);
  the exact fraction grows to thousands of digits, so counting only
  iterations understates the arithmetic cost.

The answers were checked against a separate formulation with exact
fractions: the distance reachable with `F` litres,
`M · Σ_{i≤q} 1/(2i − 1) + (F − qM)/(2q + 1)` with `q = ⌊F/M⌋`, and a
binary search for the least integer `F` reaching `N`; the 12 hand-made
trips and 150 random ones, many with capacities divisible by
`3 · 5 · 7 · 9`, agreed.

## Optimized solutions

The backward odd-harmonic fuel construction is unchanged. Fixed-point lower and upper bounds usually determine the exact integer result without building a large rational after every term. The interval width is bounded explicitly; only an ambiguous interval invokes exact rational arithmetic. Check the adjacent possible stages and retain the maximum required fuel. This uses neither an epsilon nor a precomputed answer table, so rounding cannot turn an insufficient amount into a valid answer.

Here k is the number of fuel stages. Exact-arithmetic steps are not constant-cost bit operations: the rare rational fallback depends on numerator and denominator lengths.

- `1113_math_optimized.cpp`: 0.015 s / 168 KB; base `1113_math.cpp`: 0.031 s / 616 KB; relative change: time -51.6%, memory -72.7%.
- `1113_math_optimized.go`: 0.015 s / 1044 KB; base `1113_math.go`: 0.046 s / 3364 KB; relative change: time -67.4%, memory -69.0%.
- `1113_math_optimized.java`: 0.078 s / 368 KB; base `1113_math.java`: 0.125 s / 6344 KB; relative change: time -37.6%, memory -94.2%.
- `1113_math_optimized.py`: 0.062 s / 480 KB; base `1113_math.py`: 0.125 s / 908 KB; relative change: time -50.4%, memory -47.1%.
- `1113_math_optimized.rs`: 0.015 s / 224 KB; base `1113_math.rs`: 0.062 s / 536 KB; relative change: time -75.8%, memory -58.2%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1113_math.cpp`; covering source `1113_math_optimized.cpp`; time/memory places 1/4, other-author entries 25/25.

- Go: preferred teaching base `1113_math.go`; covering source `1113_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1113_math.java`; covering source `1113_math_optimized.java`; time/memory places 1/1, other-author entries 2/2.

- Python/PyPy: preferred teaching base `1113_math.py`; covering source `1113_math_optimized.py`; time/memory places 1/7, other-author entries 22/22.

- Rust: preferred teaching base `1113_math.rs`; covering source `1113_math.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1113_math.cpp](1113_math.cpp) | G++ 13.2 x64 | math | O(kB), k ≤ 3092 | AC | 0.031 s | 616 KB | 11279217 |
| [1113_math.go](1113_math.go) | Go 1.14 x64 | math | O(kB), k ≤ 3092 | AC | 0.046 s | 3364 KB | 11279218 |
| [1113_math.java](1113_math.java) | Java 1.8 | math | O(kB), k ≤ 3092 | AC | 0.125 s | 6344 KB | 11279220 |
| [1113_math.py](1113_math.py) | Python 3.12 x64 | math | O(kB), k ≤ 3092 | AC | 0.125 s | 908 KB | 11279219 |
| [1113_math.rs](1113_math.rs) | Rust 1.75 x64 | math | O(kB), k ≤ 3092 | AC | 0.062 s | 536 KB | 11279221 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1113_math_optimized.cpp](1113_math_optimized.cpp) | G++ 13.2 x64 | math | O(k) exact-arithmetic steps | AC | 0.015 s | 168 KB | 11309282 |
| [1113_math_optimized.go](1113_math_optimized.go) | Go 1.14 x64 | math | O(k) exact-arithmetic steps | AC | 0.015 s | 1044 KB | 11309284 |
| [1113_math_optimized.java](1113_math_optimized.java) | Java 1.8 | math | O(k) exact-arithmetic steps | AC | 0.078 s | 368 KB | 11309283 |
| [1113_math_optimized.py](1113_math_optimized.py) \* | Python 3.12 x64 | math | O(k) exact-arithmetic steps | AC | 0.062 s | 480 KB | 11309281 |
| [1113_math_optimized.rs](1113_math_optimized.rs) | Rust 1.75 x64 | math | O(k) exact-arithmetic steps | AC | 0.015 s | 224 KB | 11309285 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
