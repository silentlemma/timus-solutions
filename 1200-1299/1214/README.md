# 1214. Undoing a strange procedure

[Timus 1214](https://acm.timus.ru/problem.aspx?space=1&num=1214) · difficulty 103 · math

Original problem by Anatoly Uglov, from the USU Open Collegiate Programming Contest, October 2002, Junior Session.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A procedure takes two integers `x` and `y`. If both are positive, it runs
`x + y` times a loop body that sets `y ← x² + y`, then `x ← x² + y`, then
`y ← ⌊√(x − y)⌋`, then subtracts `y` from `x` `2y` times; at the end it
prints `x` and `y`. Given what it printed, both from `−32000` to `32000`,
recover the input. No variable ever overflows.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The printed `x` and `y`.

## Output

The input `x` and `y`.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
1 1
```

Output:

```
1 1
```

## Solution

Follow one turn of the loop from `(x, y)`. First `y` becomes `x² + y`,
then `x` becomes `2x² + y`. Their difference is `x²`, so the new `y` is
`x`. Subtracting it `2x` times takes `2x²` from `2x² + y` and leaves
`y`. So each turn just swaps the two numbers, and the sum `x + y`, which
fixes the number of turns, stays the same. After `x + y` turns the
numbers are swapped exactly when the sum is odd.

So the procedure swaps its input when both numbers are positive and
their sum is odd, and changes nothing otherwise. That is its own inverse:
apply the same rule to the printed pair. `O(1)`.

Pitfalls:

- with a zero or negative number the loop does not run at all, so such a
  pair is printed unchanged;
- the sum, not the numbers themselves, decides the parity.

Running the procedure on every pair from `−3` to `15` and undoing the
result gave back the original pair each time.

## Optimized solutions

`1214_math_optimized.java`. Keep the same involution: swap exactly when both signed inputs are positive and have opposite parity. Values stay within ±32000, so int magnitudes are safe. Read through a 64-byte buffer; serialize y then x backwards into a 32-byte answer buffer, including signs, space and newline. This removes the general long formatter and separate digit array. Write and flush the complete answer before System.exit(0). Constant arithmetic/state for this bounded input. The teaching implementation remains. The new 0.093 s/436 KB pair uses more memory than the old 0.109 s/384 KB pair; strict admission comes from rank, not a claimed 30% resource gain.

Exact-source Java 1.8 Accepted #11327866: 0.093 s / 436 KB. Saved 2026-11-20 compiler-cohort comparison: time 5/75, memory 4/75. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11303725 was 0.109 s / 384 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1214_math_optimized.java`: 0.093 s / 436 KB; retained teaching base `1214_math.java`: 0.125 s / 1584 KB.

`1214_math_optimized.py`. Keep the same involution: swap the two values exactly when both are positive and their sum is odd. Zero or a negative value bypasses the swap. The printed values are bounded by 32000 in absolute value, so the sum is safe in i64. Time and arithmetic state O(1). Parse byte tokens instead of decoded line input; test oddness with a bit operation, without simulating the procedure. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1214_math.py`: time 0.078 s → 0.125 s; memory 444 KB → 204 KB.

`1214_math_optimized.rs`. Keep the same involution: swap the two values exactly when both are positive and their sum is odd. Zero or a negative value bypasses the swap. The printed values are bounded by 32000 in absolute value, so the sum is safe in i64. Time and arithmetic state O(1). Read just two signed integers, avoiding the decoded line and parsed-value vector. The mathematical transformation is unchanged. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1214_math.rs`: time 0.046 s → 0.046 s; memory 212 KB → 60 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1214_math_optimized.py`: time place 29/40, memory place 1/40 in this comparable sample.

`1214_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1214_math.cpp](1214_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11283656 |
| [1214_math.go](1214_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1068 KB | 11283657 |
| [1214_math.java](1214_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1584 KB | 11283659 |
| [1214_math.py](1214_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 444 KB | 11283658 |
| [1214_math.rs](1214_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 212 KB | 11283660 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1214_math_optimized.java](1214_math_optimized.java) \* | Java 1.8 | math | O(1) bounded arithmetic and storage | AC | 0.093 s | 436 KB | 11327866 |
| [1214_math_optimized.py](1214_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 204 KB | 11324914 |
| [1214_math_optimized.rs](1214_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 60 KB | 11324868 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
