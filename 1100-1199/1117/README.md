# 1117. Walking an in-order numbered binary tree from one number to another

[Timus 1117](https://acm.timus.ru/problem.aspx?space=1&num=1117) · difficulty 281 · math

Original problem by Alexander Somov, from the USU Open Collegiate Programming Contest, October 2001, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The nodes of a perfect binary tree are numbered `1, 2, 3, …` in order:
every inner node has a number between those of its two children, all of
one subtree on the same side. A message goes from number `i` to number `j`
through every number in between, one step at a time; a step between `k`
and `k ± 1` costs as many days as there are tree nodes strictly between
them on the tree path (0 for a parent and its child). Find the total
number of days for `1 ≤ i, j ≤ 2^31 − 1`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`i j` on one line.

## Output

The number of days.

## Checking

Compare one exact integer token; formatting whitespace is ignored. The new exact Python source passed 12 repository fixtures under PyPy 3.10. Other retained native variants keep their own saved target-runtime checks and exact Accepted receipts. Compare output according to the problem checker, not by choosing one historical formatting.

## Examples

### Example 1

Input:

```
1 5
```

Output:

```
2
```

## Solution

In an in-order numbered perfect tree, the height of node `x` above the
leaves is the number of trailing zero bits `tz(x)`: the leaves are the odd
numbers, their parents `2 mod 4`, and so on. Of two consecutive numbers
one is odd, a leaf, and the even one `e` is its ancestor at height
`tz(e)`, so the step costs `tz(e) − 1` days. Each even number strictly
between `i` and `j` is used by two steps, and an even endpoint by one.

With `c(e) = tz(e) − 1 = tz(e/2)`, the sum of `c` over the even numbers up
to `n` is `Σ_{y ≤ n/2} tz(y) = m − popcount(m)` for `m = ⌊n/2⌋` (each `y`
contributes its trailing zeros, and `Σ_{t≥1} ⌊m/2^t⌋ = m − popcount(m)`).
So for `i < j` the answer is `2·(G(j) − G(i − 1)) − c(i) − c(j)`, where
`G` is that sum and `c` of an odd number is 0. `O(1)`.

Pitfalls:

- the largest answer, for `1` and `2^31 − 1`, is `2147483586`, just 61
  below the signed 32-bit limit; the solutions use 64 bits to be safe;
- the order of `i` and `j` does not matter;
- the tree size is not given, but it does not matter: the in-order numbers
  and heights are the same in every perfect tree large enough to hold
  both numbers.

The answers were checked against a walk on the actual tree (the parent of
`x` is `x ± 2^tz(x)`) summing the path lengths step by step, for 300
random pairs below 3000, and the large tests against a direct loop over
every step.

## Optimized solutions

Keep the same prefix-cost identity as the teaching files. With h=floor(x/2), start from 2*(h-popcount(h)); for even x subtract trailingZeros(x)-1. Population count and the least significant set bit replace a per-bit walk without changing the exact integer prefix. The answer remains the absolute difference of the two prefixes. The input labels fit the stated fixed-width range, so only a bounded number of bit operations is needed. Python uses existing text streams; the measured saving and slower runtime are listed separately.

- `1117_math_optimized.java`: 0.093 s / 352 KB; base `1117_math.java`: 0.109 s / 1616 KB; relative change: time -14.7%, memory -78.2%.
- `1117_math_optimized.py`: 0.109 s / 264 KB; base `1117_math.py`: 0.078 s / 436 KB; relative change: time +39.7%, memory -39.4%.

## Language notes

Saved snapshots: 1–2 November 2026. C++ targets the top 15% or the first 10 places in both time and memory; other families target first place in both. Ties share a place. Empty competitor samples establish formal coverage only.

Use the saved current-compiler profile, exclude our own author and sub-0.015 s legacy rows; non-C++ also requires submission ID ≥10770000. C++ memory comparisons use the first 1000 qualifying rows. Treat measured times below 0.015 s as 0.015 s. The ID cutoff is a fixed comparison rule, not a precise calendar filter.

- C++: preferred teaching base `1117_math.cpp`; covering source `1117_math.cpp`; time/memory places 1/1, other-author entries 42/42.

- Go: preferred teaching base `1117_math.go`; covering source `1117_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1117_math.java`; covering source `1117_math_optimized.java`; time/memory places 1/1, other-author entries 1/1.

- Python/PyPy: preferred teaching base `1117_math.py`; covering source `1117_math_optimized.py`; time/memory places 3/1, other-author entries 6/6.

- Rust: preferred teaching base `1117_math.rs`; covering source `1117_math.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1117_math.cpp](1117_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11279242 |
| [1117_math.go](1117_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1052 KB | 11279244 |
| [1117_math.java](1117_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1616 KB | 11279246 |
| [1117_math.py](1117_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 436 KB | 11279245 |
| [1117_math.rs](1117_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 224 KB | 11279248 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1117_math_optimized.java](1117_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 352 KB | 11309311 |
| [1117_math_optimized.py](1117_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.109 s | 264 KB | 11309685 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
