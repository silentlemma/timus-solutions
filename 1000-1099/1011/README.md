# 1011. The smallest population with a share strictly between two percentages

[Timus 1011](https://acm.timus.ru/problem.aspx?space=1&num=1011) · difficulty 248 · math, number_theory

Original problem from the Ural State University Championship 1997.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given two percentages `P` and `Q` (`0.01 ≤ P, Q ≤ 99.99`, at most two digits
after the decimal point, `P < Q`), find the smallest positive integer `n` for
which some integer `c` satisfies `P% < c / n < Q%`, both inequalities strict.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`P` and `Q`, separated by a space or a line break. They may be written as
integers (`13`) or with one or two decimals (`14.1`, `12.50`).

## Output

The smallest `n`.

## Checking

Compare the exact answer tokens; whitespace formatting is immaterial.

- `1011_number_theory_optimized.cpp` (G++ 13.2 x64): 14 repository cases; 115 additional source-bound comparisons.

- `1011_number_theory.go` (Go 1.14 x64): 14 repository cases; 14 additional source-bound comparisons.

- `1011_number_theory.java` (Java 1.8): 14 repository cases; 115 additional source-bound comparisons.

- `1011_number_theory_optimized.py` (PyPy 3.10 x64): 14 repository cases.

## Examples

### Example 1

Input:

```
10 12
```

Output:

```
9
```

### Example 2

Input:

```
12.5
12.6
```

Output:

```
127
```

## Solution

First, avoid floating point. Both bounds have at most two decimals, so
`p = 100·P` and `q = 100·Q` are integers (hundredths of a percent), and the
condition becomes `p·n < 10000·c < q·n`.

**Scan over n.** For a given `n` the smallest `c` above the lower bound is
`c = ⌊p·n / 10000⌋ + 1`; `n` works exactly when this `c` is still below the
upper bound, `10000·c < q·n`. Try `n = 1, 2, ...`. The interval has width at
least `1/10000`, so some `n ≤ 10000` always works (the largest answer is
5001); the scan is instant.

**Stern–Brocot tree.** The answer is the smallest denominator of a fraction
strictly inside `(p/10000, q/10000)`. Descend the Stern–Brocot tree from
the bounds `0/1` and `1/0`: take the mediant `(a + c)/(b + d)` of the current
bounds; if it is at or below the interval it becomes the new left bound, at
or above it the new right bound, otherwise it is the answer. The first
fraction of the tree that falls inside an interval is the one with the
smallest denominator.

Pitfalls:

- reading the bounds as floating-point numbers: `14.1` is not exact in
  binary, and a comparison with `c / n` at the boundary can go either way;
- both inequalities are strict: with `P = 12.5`, `1/8` is not inside;
- `n = 1` never works, since `0 < P` and `Q < 100`.

## Optimized solutions

Keep the denominator scan and the readable one-step Stern–Brocot sources. The fast tree versions retain adjacent fractions a/b and c/d outside the open percentage interval. Their mediant is the simplest fraction between them. If it is still outside, an exact integer quotient skips the maximal run of mediants on that side; every skipped fraction remains outside. The first inside mediant therefore has the smallest denominator. Parse percentages as integer hundredths and compare cross-products with WHOLE=10000, including equality in the rejected endpoints. Quotient jumps follow continued-fraction descent, using O(log WHOLE) steps and constant numerical state. Go uses portable bounded syscall buffers; Python uses existing text streams under its explicitly recorded PyPy runtime.

- `1011_number_theory_optimized.cpp`: 0.015 s / 104 KB; base `1011_math.cpp`: 0.015 s / 352 KB; relative change: time -0.0%, memory -70.5%.
- `1011_number_theory.go`: 0.031 s / 312 KB; base `1011_math.go`: 0.015 s / 1088 KB; relative change: time +106.7%, memory -71.3%.
- `1011_number_theory.java`: 0.125 s / 332 KB; base `1011_math.java`: 0.125 s / 1580 KB; relative change: time -0.0%, memory -79.0%.
- `1011_number_theory_optimized.py`: 0.156 s / 292 KB; base `1011_number_theory.py`: 0.109 s / 468 KB; relative change: time +43.1%, memory -37.6%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1011_math.cpp`; covering source `1011_number_theory_optimized.cpp`; time/memory places 1/3, other-author entries 155/155.

- Go: preferred teaching base `1011_math.go`; covering source `1011_number_theory.go`; time/memory places 2/1, other-author entries 1/1.

- Java: preferred teaching base `1011_math.java`; covering source `1011_number_theory.java`; time/memory places 2/1, other-author entries 5/5.

- Python/PyPy: preferred teaching base `1011_number_theory.py`; covering source `1011_number_theory_optimized.py`; time/memory places 25/2, other-author entries 25/25.

- Rust: preferred teaching base `1011_math.rs`; covering source `1011_math.rs`; time/memory places 1/1, other-author entries 1/1.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1011_math.cpp](1011_math.cpp) | G++ 13.2 x64 | math | O(answer) | AC | 0.015 s | 352 KB | 11278050 |
| [1011_math.go](1011_math.go) | Go 1.14 x64 | math | O(answer) | AC | 0.015 s | 1088 KB | 11278054 |
| [1011_math.java](1011_math.java) | Java 1.8 | math | O(answer) | AC | 0.125 s | 1580 KB | 11278060 |
| [1011_number_theory.py](1011_number_theory.py) | Python 3.12 x64 | number_theory | O(answer) tree steps | AC | 0.109 s | 468 KB | 11278057 |
| [1011_math.rs](1011_math.rs) | Rust 1.75 x64 | math | O(answer) | AC | 0.015 s | 228 KB | 11278063 |

### Other Accepted approaches

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1011_number_theory.cpp](1011_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(answer) tree steps | AC | 0.015 s | 352 KB | 11278050 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1011_number_theory_optimized.cpp](1011_number_theory_optimized.cpp) | G++ 13.2 x64 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.015 s | 104 KB | 11308795 |
| [1011_number_theory.go](1011_number_theory.go) \* | Go 1.14 x64 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.031 s | 312 KB | 11309756 |
| [1011_number_theory.java](1011_number_theory.java) \* | Java 1.8 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.125 s | 332 KB | 11308797 |
| [1011_number_theory_optimized.py](1011_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(log WHOLE) quotient steps; O(1) numeric state | AC | 0.156 s | 292 KB | 11309727 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
