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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1443_math.cpp](1443_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 404 KB |
| [1443_math.go](1443_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1088 KB |
| [1443_math.java](1443_math.java) | Java 1.8 | math | O(1) | AC | 0.125 s | 1652 KB |
| [1443_math.py](1443_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 432 KB |
| [1443_math.rs](1443_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.046 s | 236 KB |
