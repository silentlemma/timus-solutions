# 1443. Rails

[Timus 1443](https://acm.timus.ru/problem.aspx?space=1&num=1443) · difficulty 670 · math

Original problem by Stanislav Vasiliev, from the Tenth Ural Collegiate Team Programming Championship, March 24–25, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A magic railway with N lines (1 ≤ N ≤ 18) of length S metres each
(1 ≤ S ≤ 10000) is laid from rails of length L (10 ≤ L ≤ 10000). Rails
may be cut, and pieces may be joined, each connection making a joint.
The number of joints must be as small as possible, and among such plans
the number of rails used must be the smallest. The lengths are given to
a tenth of a millimetre. Print that number of rails.

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

N, S and L, one per line.

## Output

The smallest number of rails.

## Examples

### Example 1

Input:

```
3
1005.6712
20.0001
```

Output:

```
151
```

## Solution

Read the lengths exactly as whole numbers of tenths of a millimetre,
since floating point would blur cases like a road a tenth of a
millimetre longer than a rail. Write S = q L + rest with 0 ≤ rest < L.
A line made of k pieces has k − 1 joints and needs k L ≥ S, so the
fewest joints come with ⌈S / L⌉ pieces in every line.

If rest = 0, every line is q whole rails, N q in total. Otherwise every
line takes q whole rails and one short piece of length rest, and the
short pieces are packed into rails, ⌊L / rest⌋ of them per rail, which
gives N q + ⌈N / ⌊L / rest⌋⌉. Spreading the shortage over several pieces
of a line does not save a rail: every piece of a line is at least rest
long, because the other q pieces are at most L. `O(1)`.

Pitfalls:

- lengths may have fewer than four decimals or none at all (tests 02,
  09, 10);
- a road just over or just under a rail length (tests 05, 11);
- the road may be shorter than one rail (tests 03, 08);
- five lines with two short pieces per rail need three extra rails, not
  the two that the total length suggests (test 07).

## Optimized solutions

The optimized versions convert the lengths to integer units of 0.0001 m and count full rails and offcuts by integer division.

Java 1.8, submission 11319248. Time 0.109 → 0.093 s, memory 1652 → 512 KB.

Rust 1.75 x64, submission 11319421. Time 0.015 → 0.015 s, memory 228 → 244 KB.

Python 3.12 x64, submission 11319468. Time 0.078 → 0.093 s, memory 404 → 396 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11321871 · Go 1.14 x64 №11322257 · Java 1.8 №11322258 · Python 3.12 x64 №11322259 · Rust 1.75 x64 №11322260.

Go reads both lengths as scaled integers and counts full rails and the rails needed for the remaining pieces separately. Go 1.14 x64, submission 11322863. Time 0.031 → 0.015 s, memory 1068 → 300 KB.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1443_math.cpp](1443_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 388 KB | 11321871 |
| [1443_math.go](1443_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1068 KB | 11322257 |
| [1443_math.java](1443_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1652 KB | 11322258 |
| [1443_math.py](1443_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 404 KB | 11322259 |
| [1443_math.rs](1443_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 228 KB | 11322260 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1443_math_optimized.java](1443_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 512 KB | 11319248 |
| [1443_math_optimized.rs](1443_math_optimized.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 244 KB | 11319421 |
| [1443_math_optimized.py](1443_math_optimized.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 396 KB | 11319468 |
| [1443_math_optimized.go](1443_math_optimized.go) \* | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 300 KB | 11322863 |

\* The marked versions have room to improve in the ratings.
