# 1120. The longest run of consecutive positive integers with a given sum

[Timus 1120](https://acm.timus.ru/problem.aspx?space=1&num=1120) · difficulty 87 · math

Original problem by Leonid Volkov, from the USU Open Collegiate Programming Contest, October 2001, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `1 ≤ S ≤ 10^9`, find positive integers `A` and `N` with
`S = A + (A + 1) + … + (A + N − 1)` and `N` as large as possible.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`S`.

## Output

`A N`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
14
```

Output:

```
2 4
```

## Solution

The run sums to `N·A + N(N − 1)/2`, so for a given `N` the start is
`A = (S − N(N − 1)/2) / N`, which must be a positive integer. `A ≥ 1`
means `N(N + 1)/2 ≤ S`, so `N` is at most about `√(2S) ≈ 44721`. Try `N`
downwards from that bound and stop at the first one that divides; `N = 1`
always works. `O(√S)`.

Pitfalls:

- a square root may round up: start from `⌊√(2S)⌋` and lower `N` while
  `N(N + 1)/2 > S`;
- `N(N + 1)/2` for `N ≈ 44721` is about `10^9` and fits in 32 bits, but the
  C++, Go, Java and Rust solutions use 64-bit integers; Python uses
  arbitrary-precision integers;
- a power of two has no odd divisor greater than 1, so only `N = 1` works
  (test 08).

The answers were checked against trying every start and length for
`S ≤ 3000`, and for larger `S` against the divisor view: a run of length
`N` exists exactly when `N` divides `2S` and `2S/N − N + 1` is positive
and even.

## Optimized solutions

`1120_number_theory.py`. Factor the odd part of S and enumerate its divisors rather than scanning every possible progression length. Each odd divisor gives the two candidate lengths d and 2S/d; require length(length+1)≤2S for a positive starting value, then maximize length. Use trial division with 2 removed, a short recursive divisor generator, and exact integer arithmetic. Disable optional PyPy JIT for the short factor scan and flush before direct exit. Conservative O(√S+τ(S)) arithmetic work and O(log S) factor/recursion state; preserve the simpler length scan.

Compared with `1120_math.py`: time 0.078 s → 0.109 s; memory 444 KB → 308 KB.

The optimized Java solution parses the number byte by byte from
`System.in` instead of using `Scanner` and updates the remainder for the
next shorter length in O(1): 368 KB instead of 1640 KB, with the same
time.

`1120_math_optimized.rs`. Find the largest length satisfying N(N+1)/2<=S by integer binary search; then test lengths downwards until S-N(N-1)/2 is divisible by N. This removes floating-point square root without changing the descending search. Under S<=10^9 all binary-search products fit i64. Time O(log S+√S)=O(√S), auxiliary space O(1). The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1120_math.rs`: time 0.046 s → 0.031 s; memory 220 KB → 56 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1120_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1120_math.cpp](1120_math.cpp) | G++ 13.2 x64 | math | O(√S) | AC | 0.015 s | 128 KB | 11279266 |
| [1120_math.go](1120_math.go) | Go 1.14 x64 | math | O(√S) | AC | 0.031 s | 1064 KB | 11279268 |
| [1120_math.java](1120_math.java) | Java 1.8 | math | O(√S) | AC | 0.109 s | 1640 KB | 11279273 |
| [1120_math.py](1120_math.py) | Python 3.12 x64 | math | O(√S) | AC | 0.078 s | 444 KB | 11279271 |
| [1120_math.rs](1120_math.rs) | Rust 1.75 x64 | math | O(√S) | AC | 0.046 s | 220 KB | 11279275 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1120_math_optimized.java](1120_math_optimized.java) | Java 1.8 | math | O(√S) | AC | 0.093 s | 368 KB | 11303709 |
| [1120_math_optimized.rs](1120_math_optimized.rs) \* | Rust 1.75 x64 | math | O(√S) | AC | 0.031 s | 56 KB | 11324861 |
| [1120_number_theory.py](1120_number_theory.py) \* | PyPy 3.10 x64 | number_theory | O(√S+τ(S)) arithmetic work; O(log S) state | AC | 0.109 s | 308 KB | 11325855 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
