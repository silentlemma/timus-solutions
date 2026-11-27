# 1110. All residues whose N-th power gives a remainder Y

[Timus 1110](https://acm.timus.ru/problem.aspx?space=1&num=1110) · difficulty 53 · bruteforce

Original problem from the Bulgarian National Olympiad in Informatics, Day 1.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `N`, `M` and `Y` (`0 < N < 999`, `1 < M < 999`, `0 < Y < 999`),
find every integer `X` in `[0, M − 1]` with `X^N mod M = Y`.

The three input values N, M and Y are integers.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

`N M Y` on one line.

## Output

All such `X` in increasing order, separated by spaces, or `-1` if there
are none.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
2 6 4
```

Output:

```
2 4
```

## Solution

There are fewer than a thousand candidates, so try each `X` and compute
`X^N mod M` by repeated squaring, reducing modulo `M` after every
multiplication. `O(M log N)`.

During repeated squaring, result*b^e remains congruent to the original
X^N modulo M. Multiplying result for an odd exponent and then squaring
b while halving e preserves this invariant; e=0 gives the exact
remainder. Every X in 0..M-1 is tested exactly once, so the retained
values are precisely all roots, already ordered. The empty result
therefore justifies -1. The N=1 case takes constant work per candidate.

The power routine uses O(1) arithmetic words. Simple C++ stores O(M)
root integers; Go/Rust store root strings and the joined answer, while
Java stores the answer builder. Simple Python stores root integers and
formatted output. If P is output bytes, these retained answers cost
O(M+P); here each root has at most three digits, so this is O(M).
Full retained input adds I bytes in Python/Rust and optimized Go.
Optimized C++ emits roots directly with O(1) state; Java uses O(M)
flags/output bytes; Python and Go optimized still retain root strings
and their joined answer. Fixed library I/O buffers are additional.

Pitfalls:

- `Y` may be `M` or larger; a remainder never is, so the answer is then
  `-1`;
- `X^N` itself is astronomically large: reduce at every step, and keep
  the products below `M²`, which fits in 32 bits;
- with `N = 1` the answer is `Y` alone whenever `Y < M`.

The answers were checked against plain repeated multiplication, `N`
multiplications for every `X`.

## Optimized solutions

`1110_bruteforce_optimized.java`. Java keeps exhaustive modular root search with repeated squaring, but pairs x with M-x: their Nth powers are equal for even N and opposite modulo M for odd N. One exponentiation therefore checks both residues; zero is handled separately, and Y>=M has no roots. A boolean array records the roots, then a bounded raw byte buffer emits them in increasing order, or -1. Since M<999, each root has at most three decimal digits and a 4*M byte answer buffer suffices. Time O(M log N), auxiliary space O(M). The direct integer parser remains; no answer table or new number-theoretic solver is introduced.

Exact-source Java 1.8 Accepted #11327344: 0.078 s / 304 KB. Saved 2026-11-20 compiler-cohort comparison: time 1/228, memory 1/228. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The applicable time criterion passes; no separate language target exists, and the row is unstarred. The previously documented optimized run #11303558 was 0.109 s / 412 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1110_bruteforce_optimized.java`: 0.078 s / 304 KB; retained teaching base `1110_bruteforce.java`: 0.109 s / 1568 KB.

`1110_bruteforce_optimized.py`. Both Python sources already use
three-argument pow and one joined answer. The optimized source stores
root strings directly instead of an integer list converted at printing,
reads through stdin.buffer, writes without a final newline, explicitly
flushes and calls os._exit(0). Root tests and ascending order are
unchanged; an empty list still emits -1. This changes output/runtime
handling, not the exhaustive modular algorithm.

Exact-source CPython 3.12 Accepted #11327010: 0.062 s / 656 KB. Comparison saved 2026-11-20 on the current language-family compiler cohort: time rank 4/147, memory rank 118/147. Below 1024 KB, strict admission uses time only.

- `1110_bruteforce_optimized.py`: 0.062 s / 656 KB; retained teaching base `1110_bruteforce.py` (Python 3.12 x64): 0.078 s / 352 KB; time change -20.5%; memory change +86.4%.

The optimized C++ solution prints every root as soon as it is found
instead of collecting the roots in a vector: 128 KB instead of 196 KB,
with the same time.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1110_bruteforce_optimized.go`. Keep the archived algorithm and its boundary rules. Replace fmt scanning and printing with decimal/token conversion and a reused output buffer. Input is read into a byte buffer, trading full-input storage for less general-purpose I/O overhead.

Accepted #11328498 (Go 1.14 x64): **0.031 s / 944 KB**. Archived comparison: `1110_bruteforce.go` (Go 1.14 x64) — 0.015 s / 1104 KB (#11279203).

The current 1110_bruteforce_optimized.go revision only names unchanged
64-bit numeric conversions and the 64-byte initial output capacity. The algorithm, simple version and substantive comments are preserved.

## Language notes

- Python uses the built-in three-argument `pow`; the other languages
  carry a small power function.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1110_bruteforce.cpp](1110_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(M log N) | AC | 0.015 s | 196 KB | 11279202 |
| [1110_bruteforce.go](1110_bruteforce.go) | Go 1.14 x64 | bruteforce | O(M log N) | AC | 0.015 s | 1104 KB | 11279203 |
| [1110_bruteforce.java](1110_bruteforce.java) | Java 1.8 | bruteforce | O(M log N) | AC | 0.109 s | 1568 KB | 11279205 |
| [1110_bruteforce.py](1110_bruteforce.py) | Python 3.12 x64 | bruteforce | O(M log N) | AC | 0.078 s | 352 KB | 11279204 |
| [1110_bruteforce.rs](1110_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(M log N) | AC | 0.015 s | 212 KB | 11279206 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1110_bruteforce_optimized.cpp](1110_bruteforce_optimized.cpp) | G++ 13.2 x64 | bruteforce | O(M log N) | AC | 0.015 s | 128 KB | 11303557 |
| [1110_bruteforce_optimized.java](1110_bruteforce_optimized.java) | Java 1.8 | bruteforce | O(M log N) time; O(M) auxiliary space | AC | 0.078 s | 304 KB | 11327344 |
| [1110_bruteforce_optimized.py](1110_bruteforce_optimized.py) | Python 3.12 x64 | bruteforce | O(M log N) | AC | 0.062 s | 656 KB | 11327010 |
| [1110_bruteforce_optimized.go](1110_bruteforce_optimized.go) | Go 1.14 x64 | bruteforce | O(M log N) | AC | 0.031 s | 1020 KB | 11330989 |
