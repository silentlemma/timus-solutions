# 1283. Dwarf

[Timus 1283](https://acm.timus.ru/problem.aspx?space=1&num=1283) · difficulty 116 · math

Original problem by Leonid Volkov (prepared by Ivan Dashkevich), from the Ural State University Personal Contest 2004.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A dwarf has G units of gold, and every year a bank keeps p percent of
it as a fee (1 ≤ p ≤ 99), so the gold shrinks to (100 − p)/100 of
itself. Once the gold is at most L, the dwarf gives up. G and L are
integers not exceeding 2³¹ − 1. How many years are left?

Time limit: 1 second. Memory limit: 64 MB.

## Input

G, L and p.

## Output

The number of years.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
81 64 20
```

Output:

```
2
```

### Example 2

Input:

```
625 256 20
```

Output:

```
4
```

## Solution

After k years the gold is exactly G · ((100 − p)/100)^k, and the answer
is the first k with that at most L. In whole numbers the test is

```text
G · (100 − p)^k ≤ L · 100^k
```

so both sides are multiplied each year, by 100 − p and by 100, until
the left one is no longer larger. The loop runs at most about 2140
times, for G = 2³¹ − 1, L = 1 and p = 1, and the numbers grow to a few
thousand digits. For `Y` years and the bounded positive initial inputs,
each product has `O(Y+1)` digits or fixed-base limbs. The simple versions
therefore take `O((Y+1)²)` digit operations and `O(Y+1)` live auxiliary
digits/limbs, including multiplication temporaries. The `+1` includes
the immediate zero-year case. Input storage and I/O buffers are additional:
Rust retains the input string, Python retains its input line, and the
other simple versions use bounded scanner/stdio buffers. All contain
only three bounded numbers in the specified format.

The bound on the loop assumes positive G and L, while the statement
gives no lower bounds for them: with G > 0 and L = 0, the gold stays
positive after every finite number of years, and there is no finite
answer.

Pitfalls:

- the gold can land exactly on the limit, and floating point then
  misses it: 300 · 0.81 comes out as 243.00000000000003, one year too
  many for L = 243 (test 05), and ln(9801/10000) / ln(0.99) rounds up to
  three years instead of two (test 06);
- if the gold is already at most L, the answer is 0 (tests 03, 04).

## Optimized solutions

`1283_binary_search_math.py`. Find the first year Y with G(100−p)^Y≤L100^Y by exponential bracketing and binary search on exact integer powers. No logarithm, gcd/math import or per-year big-integer multiplication loop is needed. Handle G≤L immediately, including zero; preserve exact equality boundaries. If D bounds operand bits and M(D) multiplication cost, conservative O(log²(Y+2)·M(D)) time and O(D) space. This search algorithm has a separate filename and the simple year-by-year version remains.

Compared with `1283_math.py`: time 0.078 s → 0.125 s; memory 480 KB → 264 KB.

The optimized Java solution keeps each side as an array of base-10⁹
digits that it multiplies in place, growing the array only when a new
digit appears, instead of creating two new `BigInteger` objects every
year; a digit times at most 100 plus the carry stays below 10¹¹ and fits
in `long`. It reads G, L and p digit by digit straight from `System.in`
into `int`, which holds them since they are at most 2³¹ − 1, instead of
creating a `Scanner`: [1283_math_optimized.java](1283_math_optimized.java).

### Measured gains

The percentages below describe the paired historical table receipts, not
another 30%-improvement admission rule. Meaningful simple versions remain
available. Java uses the same annual exact comparison with mutable limbs;
with bounded initial inputs its live storage is `O(Y+1)` limbs plus I/O
buffers, including temporary arrays during capacity growth.

- `1283_math_optimized.java`: time reduction +0.00%; memory reduction
  +93.57%; base: `1283_math.java`.

`1283_math_optimized.rs`. Preserve exact comparison of G*(100-p)^Y and L*100^Y, but reduce G/L and (100-p)/100 by their gcds first. Keep both products in u128 while checked multiplication succeeds; on overflow promote both unchanged pre-multiplication values to base-10^9 u32 limbs and continue exactly. The guard G<=L returns zero before reduction. No logarithms, floating point or epsilon decide the stopping boundary. With Y years and at most D limbs, time O((Y+1)·D), storage O(D); narrow limbs and the native-integer fast path reduce overhead. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1283_math.rs`: time 0.015 s → 0.031 s; memory 232 KB → 68 KB.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

The current Go source only extracts the unchanged 24-byte output capacity
into a named constant to satisfy the structural linter. All other judge sources remain unchanged.

`1283_parsing_optimized.go`. Unlike `1283_math.go`, which uses `math/big`
and the unreduced factors `100-p` and `100`, this version introduces
mutable little-endian `[]uint32` limbs in base 10⁹. It divides both annual
factors by their gcd before growing the two exact products; it does not
reduce the initial `G/L` ratio. Limb multiplication and length/high-limb
comparison replace generic big-integer operations. A 256-byte refill
buffer parses the three integers with a local cursor and negative decimal
accumulation; fixed scratch buffers format the year count. The stopping
inequality is unchanged, including equality. With at most `D` limbs,
time is `O((Y+1)·D)` and live auxiliary storage is `O(D+B)` for fixed
I/O storage `B`; bounded initial values give `D = O(Y+1)`.

Accepted #11329132 (Go 1.14 x64): **0.015 s / 812 KB**. Archived comparison: `1283_math.go` (Go 1.14 x64) — 0.031 s / 1276 KB (#11284478).

## Language notes

The shared [rating criteria](../../RATING_CRITERIA.md) apply to all
families: ordinary top ten or top 15% for the required metrics, with the
1–10 exact-compiler rival reference override. Below 1024 KB, only time
is compared. Rival rows faster than `0.015 s` are excluded; only our own
time is floored to that value. There is no first-place or separate
30%-improvement admission requirement, nor an ID or date cutoff.

The saved audit admits both Rust sources by ordinary time ranking,
including optimized Rust (`0.031 s / 68 KB`); the earlier no-reference
explanation is superseded. C++, simple CPython and optimized Java also
pass ordinary time ranking. Optimized Go passes the sparse exact-compiler
reference on time only. Simple Go and Java miss their required comparisons
but remain teaching versions. The additional PyPy binary-search source
misses its time target, so its existing marker is retained; CPython
already closes the Python position. Earlier snapshot discussion from
18 November 2026 is historical, while all paired Accepted measurements
below remain unchanged.

The source revisions discussed above have now received their own Accepted results. The solution tables list the final source-matched submission IDs and paired time/memory measurements; earlier observations describe previous revisions. All meaningful simple implementations remain available.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1283_math.cpp](1283_math.cpp) | G++ 13.2 x64 | math | O((Y+1)²) | AC | 0.015 s | 204 KB | 11284476 |
| [1283_math.go](1283_math.go) | Go 1.14 x64 | math | O((Y+1)²) | AC | 0.031 s | 1276 KB | 11284478 |
| [1283_math.java](1283_math.java) | Java 1.8 | math | O((Y+1)²) | AC | 0.109 s | 5600 KB | 11284490 |
| [1283_math.py](1283_math.py) | Python 3.12 x64 | math | O((Y+1)²) | AC | 0.078 s | 480 KB | 11284484 |
| [1283_math.rs](1283_math.rs) | Rust 1.75 x64 | math | O((Y+1)²) | AC | 0.015 s | 232 KB | 11284494 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1283_math_optimized.java](1283_math_optimized.java) | Java 1.8 | math | O((Y+1)²) | AC | 0.109 s | 360 KB | 11304347 |
| [1283_math_optimized.rs](1283_math_optimized.rs) | Rust 1.75 x64 | math | O((Y+1)·D) | AC | 0.031 s | 68 KB | 11325092 |
| [1283_binary_search_math.py](1283_binary_search_math.py) \* | PyPy 3.10 x64 | binary_search, math | O(log²(Y+2)·M(D)) time; O(D) space | AC | 0.125 s | 264 KB | 11325857 |
| [1283_parsing_optimized.go](1283_parsing_optimized.go) | Go 1.14 x64 | parsing | O((Y+1)²) | AC | 0.031 s | 808 KB | 11331000 |

\* Accepted; the rating target under [RATING_CRITERIA.md](../../RATING_CRITERIA.md) is not yet met. This version may be optimized further.
