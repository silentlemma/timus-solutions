# 1793. Tray 2

[Timus 1793](https://acm.timus.ru/problem.aspx?space=1&num=1793) · difficulty 403 · geometry

Original problem by Sofia Tekhazheva, from the Ural Regional School Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A tray has an a × b bottom and vertical borders of height d. Two plates
are truncated cones of the same height h, each with a bottom radius and
a larger top radius. Can both plates stand with their whole bottoms on
the tray?

## Input

a, b and d; then the bottom and top radius of each plate; then h. All
numbers are whole, from 1 to 1000.

## Output

"YES" if the plates can be placed, otherwise "NO".

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
10 10 10
1 2
1 2
5
```

Output:

```
YES
```

### Example 2

Input:

```
8 4 1
1 2
1 3
1
```

Output:

```
NO
```

## Solution

A plate widens upwards, so inside the borders it is widest at height
min(d, h), where its radius is w = r + (R − r)·min(d, h)/h. Above the
borders it may hang over the edge. So each plate's centre must stay at
least w from every side, which needs 2w ≤ a and 2w ≤ b. Two plates of
the same height are farthest from overlapping at the bottom and
closest at the top, so their centres must be at least R₁ + R₂ apart.
The centres are farthest apart in opposite corners of their allowed
rectangles, a − w₁ − w₂ apart along one side and b − w₁ − w₂ along the
other. Multiplying everything by h keeps it all in whole numbers, and
comparing squared distances avoids roots, so the test is exact.
`O(1)`.

In the first example the borders are higher than the plates, so w = 2
for both; the centres can be 6 apart along each side, about 8.49 in
all, and they need only 4.

Pitfalls:

- with low borders the top of a plate may be wider than the tray;
- the plates collide at their tops, not at the height of the borders;
- plates that just touch still fit, which a floating-point test can get
  wrong.

The answers agree with an independent accepted implementation on 600
random cases, among them plates that exactly touch along a 3-4-5
diagonal.

## Optimized solutions

`1793_geometry_optimized.java`. Java retains the algorithm and its data structures described for the simple version. A fixed byte buffer and FastInput replace Scanner and its regular-expression and locale machinery. Integer tokens are parsed directly; strings still use UTF-8 decoding when requested, and decimal tokens retain explicit numeric conversion. Lookahead keeps a token only when needed. The output algorithm is unchanged. This removes general-purpose parsing overhead; the table describes algorithmic work, with input scanning linear in the number of bytes and a bounded input buffer.

Compared with `1793_geometry.java`: time 0.156 s → 0.109 s; memory 1592 KB → 504 KB.

C++ and Go keep the same exact scaled-radius test. First check whether each plate fits the shorter tray side at the border height. Only then compare the squared separation of the opposite allowed corners with the squared sum of the top radii. The final products use signed 64-bit arithmetic, and output is the constant string YES or NO. Go reads the eight positive integers through a fixed byte buffer, without scanner tokens or string conversion. It uses standard handles directly, retrying interrupted calls and completing partial writes.

The accepted base implementations [1793_geometry.java](1793_geometry.java), [1793_geometry.py](1793_geometry.py), [1793_geometry.rs](1793_geometry.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

`1793_geometry_optimized.java`: time place 8/31, memory place 3/31 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1793_geometry.cpp](1793_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 368 KB | 11325581 |
| [1793_geometry.go](1793_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1076 KB | 11289865 |
| [1793_geometry.java](1793_geometry.java) \* | Java 1.8 | geometry | O(1) | AC | 0.156 s | 1592 KB | 11289867 |
| [1793_geometry.py](1793_geometry.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 432 KB | 11289866 |
| [1793_geometry.rs](1793_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 216 KB | 11325607 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1793_geometry_optimized.cpp](1793_geometry_optimized.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 104 KB | 11310893 |
| [1793_geometry_optimized.go](1793_geometry_optimized.go) \* | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 312 KB | 11311212 |
| [1793_geometry_optimized.java](1793_geometry_optimized.java) \* | Java 1.8 | geometry | O(1) | AC | 0.109 s | 504 KB | 11324814 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
