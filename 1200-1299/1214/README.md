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
4 7
```

Output:

```
7 4
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

Exact-source Java 1.8 Accepted #11327866 is 0.093 s / 436 KB. The saved 2026-11-20 comparison gives time 5/75, memory 4/75. It passes the shared time-only criterion below 1024 KB, without a separate first-place target or asterisk. Earlier optimized #11303725 at 0.109 s / 384 KB is a distinct historical pair, not the current file receipt. The simple Java remains unchanged.

- `1214_math_optimized.java`: 0.093 s / 436 KB; retained teaching base `1214_math.java`: 0.125 s / 1584 KB.

`1214_math_optimized.py`. Keep the same involution: swap the two values exactly when both are positive and their sum is odd. Zero or a negative value bypasses the swap. The printed values are bounded by 32000 in absolute value, so the sum is safe in i64. Time and arithmetic state O(1). Parse byte tokens instead of decoded line input; test oddness with a bit operation, without simulating the procedure. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1214_math.py`: time 0.078 s → 0.125 s; memory 444 KB → 204 KB.

`1214_math_optimized.rs`. Keep the same involution: swap the two values exactly when both are positive and their sum is odd. Zero or a negative value bypasses the swap. The printed values are bounded by 32000 in absolute value, so the sum is safe in i64. Time and arithmetic state O(1). Read just two signed integers, avoiding the decoded line and parsed-value vector. The mathematical transformation is unchanged. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1214_math.rs`: time 0.046 s → 0.046 s; memory 212 KB → 60 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1214_math_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328523 (Go 1.14 x64): **0.031 s / 948 KB**. Archived comparison: `1214_math.go` (Go 1.14 x64) — 0.015 s / 1068 KB (#11283657).

Go Accepted #11328523 and its qualification refer to the historical exact bytes. This review names the existing 64-bit conversion width `numericBitSize` in four strconv calls; substituting 64 back exactly restores the previous file. The algorithm, all comments and simple Go are preserved.

## Language notes

Apply the shared [rating criteria](../../RATING_CRITERIA.md) to the cached exact-source receipts. Simple C++, optimized Go/Java, simple CPython and both Rust sources qualify. Simple Go at 0.015 s / 1068 KB fails its required memory comparison, whereas optimized Go at 0.031 s / 948 KB passes with time only: the latter is not claimed faster. Simple Java misses the numerical target; meaningful simple sources remain unstarred teaching versions. Below 1024 KB only time is required; above it both metrics apply. Go uses its applicable exact-compiler reference comparison, Rust the same-language fallback. No rival, first-place or 30%-gain exception independently admits a source.

The saved 2026-11-18 PyPy comparison is historical: #11324914 at 0.125 s / 204 KB had time place 29/40 and memory place 1/40. It still misses time and keeps its marker despite lower memory. CPython base #11283658 at 0.078 s / 444 KB supplies Python fast coverage. Current paired measurements remain in the tables; old snapshots are not new live rankings or guarantees across runs.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

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
| [1214_math_optimized.java](1214_math_optimized.java) | Java 1.8 | math | O(1) bounded arithmetic and storage | AC | 0.093 s | 436 KB | 11327866 |
| [1214_math_optimized.py](1214_math_optimized.py) \* | PyPy 3.10 x64 | math | O(1) | AC | 0.125 s | 204 KB | 11324914 |
| [1214_math_optimized.rs](1214_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 60 KB | 11324868 |
| [1214_math_optimized.go](1214_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.046 s | 936 KB | 11330996 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
