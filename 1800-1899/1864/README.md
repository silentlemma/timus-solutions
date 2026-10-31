# 1864. Get-Together at Den's

[Timus 1864](https://acm.timus.ru/problem.aspx?space=1&num=1864) · difficulty 177 · math

Original problem: folklore (prepared by Daniil Ayzenshteyn), from the Open Ural FU Championship, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n friends came to Den's place; friend i bought aᵢ litres of juice, and
everybody, Den included, drank the same amount. Den then pays
100 roubles for the juice drunk by people who had not bought it, shared
fairly among the friends who bought more than they drank. How many
roubles does each friend get, rounded down?

## Input

n (2 ≤ n ≤ 100), then a₁, …, aₙ (0 ≤ aᵢ ≤ 100) with a positive sum.

## Output

The roubles of every friend, rounded down.

## Examples

### Example 1

Input:

```
3
10 10 10
```

Output:

```
33 33 33
```

### Example 2

Input:

```
2
10 0
```

Output:

```
100 0
```

## Solution

With S litres in all, each of the n + 1 people drinks S/(n + 1), so
friend i bought aᵢ − S/(n + 1) litres for others when that is positive,
and nothing for others otherwise. The money is shared in proportion to
these amounts. Multiplying all of them by n + 1 keeps everything in
integers: eᵢ = max(0, aᵢ(n + 1) − S), and friend i gets
⌊100·eᵢ / Σ e⌋. The sum is never 0: the friends together bought S and
drank only nS/(n + 1). `O(n)`; Python takes `O(n²)`.

In the first example everybody drank 7.5 litres, and each friend paid
2.5 litres for Den, so the money is split in three: 33 each after
rounding.

Pitfalls:

- Den drinks too, so the share is S/(n + 1), not S/n;
- the friends who bought less than they drank get nothing;
- exact integers avoid any doubt about rounding down.

The shares agree with an independent accepted implementation on two
hundred random gatherings.

## Optimized solutions

The optimized C++ solution computes the same shares, but keeps the
purchases and the surpluses in two fixed arrays of 100 numbers, enough
since `n ≤ 100`, instead of two vectors allocated on the heap:
{1864_math_optimized.cpp}.

The optimized Java solution computes the same shares, but reads the
numbers with `BufferedReader` and `StringTokenizer` instead of
`Scanner`, whose regular expressions take time and memory to set up:
{1864_math_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1864_math_optimized.cpp`: time reduction +0.00%; memory reduction
  +45.83%; base: `1864_math.cpp`.

- `1864_math_optimized.java`: time reduction +0.00%; memory reduction
  +69.77%; base: `1864_math.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1864_math.go](1864_math.go).
- [1864_math.rs](1864_math.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1864_math.cpp](1864_math.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 192 KB | 11304246 |
| [1864_math.go](1864_math.go) | Go 1.14 x64 | math | O(n) | AC | 0.031 s | 1116 KB | 11290890 |
| [1864_math.java](1864_math.java) | Java 1.8 | math | O(n) | AC | 0.125 s | 1720 KB | 11290894 |
| [1864_math.py](1864_math.py) | Python 3.12 x64 | math | O(n²) | AC | 0.093 s | 412 KB | 11290893 |
| [1864_math.rs](1864_math.rs) | Rust 1.75 x64 | math | O(n) | AC | 0.031 s | 236 KB | 11304247 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1864_math_optimized.cpp](1864_math_optimized.cpp) | G++ 13.2 x64 | math | O(n) | AC | 0.015 s | 104 KB | 11307321 |
| [1864_math_optimized.java](1864_math_optimized.java) \* | Java 1.8 | math | O(n) | AC | 0.125 s | 520 KB | 11307325 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
