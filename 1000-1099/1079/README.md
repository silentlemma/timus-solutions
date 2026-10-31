# 1079. The largest term of Stern's sequence up to n

[Timus 1079](https://acm.timus.ru/problem.aspx?space=1&num=1079) · difficulty 112 · dp

Original problem by Emil Kelevedzhiev, from the Informatics Tournament of the Winter Mathematical Festival, Varna 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The sequence is `a₀ = 0`, `a₁ = 1`, `a₂ᵢ = aᵢ` and
`a₂ᵢ₊₁ = aᵢ + aᵢ₊₁` for `i ≥ 1`. For each given `n`
(`1 ≤ n ≤ 99 999`) print the largest of `a₀, a₁, …, aₙ`.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

Up to ten lines with `n`, then a line with 0.

## Output

The maximum for each `n`, one per line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
5
10
0
```

Output:

```
3
4
```

## Solution

Every term refers only to terms with smaller indices, so one pass from 2
to 99 999 fills the whole table, and a running maximum
`best[i] = max(best[i − 1], aᵢ)` answers every query at once. `O(N)` for
the table, `O(1)` per query.

This is Stern's diatomic sequence. Some records are Fibonacci numbers,
reached at integer indices `n = (2^k ± 1)/3`; the largest value up to 99 999 is 2584,
so 32-bit integers are plenty.

Pitfalls:

- the queries come in any order and end with 0, which is not a query;
- the recurrence for odd indices uses `aᵢ₊₁`, which is still smaller than
  `2i + 1`, so the order of the pass is right.

The answers were checked against the definition computed by a memoised
recursion and a plain scan for every query.

## Optimized solutions

The optimized C++ solution keeps the terms only up to index 50 000,
since the formula for an index up to 99 999 looks no further than that,
and stores the terms and the running maxima in 16-bit integers, which is
enough because no term up to 99 999 exceeds 2584:
{1079_dp_optimized.cpp}.

The optimized Go solution keeps the terms only up to index 50 000, since
the formula for an index up to 99 999 looks no further than that, stores
the terms and the running maxima in `uint16`, which is enough because no
term up to 99 999 exceeds 2584, and reads the queries byte by byte
instead of `fmt.Fscan`: {1079_dp_optimized.go}.

The optimized Java solution keeps the terms only up to index 50 000,
since the formula for an index up to 99 999 looks no further than that,
stores the terms and the running maxima in 16-bit `char` arrays, which
is enough because no term up to 99 999 exceeds 2584, and parses the
queries by hand from a `BufferedInputStream` instead of `Scanner`:
{1079_dp_optimized.java}.

The optimized Python solution keeps the terms only up to index 50 000,
since the formula for an index up to 99 999 looks no further than that,
and stores the terms and the running maxima in `array` objects of 16-bit
integers instead of lists of Python integers; 16 bits are enough because
no term up to 99 999 exceeds 2584: {1079_dp_optimized.py}.

The optimized Rust solution keeps the terms only up to index 50 000,
since the formula for an index up to 99 999 looks no further than that,
and stores the terms and the running maxima as `u16` instead of `u32`;
16 bits are enough because no term up to 99 999 exceeds 2584:
{1079_dp_optimized.rs}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1079_dp_optimized.cpp`: time reduction -106.67%; memory reduction
  +56.67%; base: `1079_dp.cpp`.

- `1079_dp_optimized.go`: time reduction +0.00%; memory reduction
  +55.72%; base: `1079_dp.go`.

- `1079_dp_optimized.java`: time reduction +12.80%; memory reduction
  +69.20%; base: `1079_dp.java`.

- `1079_dp_optimized.py`: time reduction -12.00%; memory reduction
  +76.46%; base: `1079_dp.py`.

- `1079_dp_optimized.rs`: time reduction -106.67%; memory reduction
  +48.21%; base: `1079_dp.rs`.

## Language notes

- All languages build both tables before reading the queries.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1079_dp.cpp](1079_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 960 KB | 11278996 |
| [1079_dp.go](1079_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 2764 KB | 11278997 |
| [1079_dp.java](1079_dp.java) | Java 1.8 | dp | O(N) | AC | 0.125 s | 2364 KB | 11278999 |
| [1079_dp.py](1079_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.125 s | 3280 KB | 11278998 |
| [1079_dp.rs](1079_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 1004 KB | 11279000 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1079_dp_optimized.cpp](1079_dp_optimized.cpp) \* | G++ 13.2 x64 | dp | O(N) | AC | 0.031 s | 416 KB | 11304025 |
| [1079_dp_optimized.go](1079_dp_optimized.go) \* | Go 1.14 x64 | dp | O(N) | AC | 0.031 s | 1224 KB | 11304026 |
| [1079_dp_optimized.java](1079_dp_optimized.java) \* | Java 1.8 | dp | O(N) | AC | 0.109 s | 728 KB | 11304027 |
| [1079_dp_optimized.py](1079_dp_optimized.py) \* | Python 3.12 x64 | dp | O(N) | AC | 0.140 s | 772 KB | 11304028 |
| [1079_dp_optimized.rs](1079_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 520 KB | 11304337 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
