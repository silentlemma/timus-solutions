# 1753. Bookshelf

[Timus 1753](https://acm.timus.ru/problem.aspx?space=1&num=1753) · difficulty 335 · geometry

Original problem by Dmitry Ivankov, from the XI USU Open Personal Contest, March 13, 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A shelf of length L has rims of height h at both ends. A book of height
H stands upright at the left rim. Its lower edge is dragged to the
right along the shelf while its side keeps leaning on the top of the
left rim, until the book lies flat. Everything has zero thickness. Find
how far to the left of the left rim the middle of the book gets.

## Input

Integers h, H and L (1 ≤ h < H < L ≤ 1000).

## Output

The largest shift of the middle of the book to the left of the rim,
with an error of at most 10⁻⁵.

## Checking

Repository tests compare numeric tokens with |actual-reference| <= 1e-5·max(1,|reference|), reject nonfinite values, and compare nonnumeric tokens exactly.

## Examples

### Example 1

Input:

```
7 120 200
```

Output:

```
39.850361
```

## Solution

Put the top of the left rim at (0, h) and the foot of the book at
(x, 0). The book lies along the line from the foot through the rim
top, which is r = √(x² + h²) long, so its middle at distance H/2 from
the foot is at horizontal position x(1 − H / 2r). The shift to the left
is f(x) = x(H / 2r − 1).

Its derivative is H·h² / 2r³ − 1, so f grows while r³ < H·h²/2 and
falls after, and the best moment is r = ∛(H·h²/2). That r is never
more than H, so the book still leans on the rim then. If this r is not
above h, which happens exactly when H ≤ 2h, the middle never passes
the rim and the answer is 0; otherwise x = √(r² − h²) and the answer is
f(x). L plays no part, since the book always fits on the shelf. `O(1)`.

In the example r = ∛2940 ≈ 14.33, x ≈ 12.50 and the shift is about
39.85.

Pitfalls:

- a book at most twice the rim gives 0, not a negative shift;
- the rim is on the left, so the foot moving right pushes the middle
  left only while the book is steep.

The formula agrees with a scan over 200001 foot positions on 100
random inputs and with an independent accepted implementation on 300
more.

## Optimized solutions

`1753_geometry_optimized.java`. Java keeps the same analytic optimum. For foot distance x and r=hypot(x,h), displacement is x*(H/(2*r)-1), whose derivative is H*h*h/(2*r^3)-1. Thus the maximum is zero when H<=2*h; otherwise r=cbrt(H*h*h/2) and x=sqrt(r*r-h*h) give the maximizing displacement. At that point x<H<L, so shelf length does not constrain the result and need not be parsed. The existing cbrt/sqrt double computation is unchanged. Double.toString emits its round-trip decimal without Formatter or Locale initialization. Time and auxiliary space O(1), including the fixed 1024-byte input buffer; the original floating-point teaching source is preserved.

Exact-source Java 1.8 Accepted #11327331: 0.109 s / 572 KB. Saved 2026-11-20 compiler-cohort comparison: time 10/37, memory 4/37. Below 1024 KB strict admission uses time only: top ten or top 15%, with ties sharing a rank and percentile cutoff rounded up. The asterisk remains for the separate language target of first place in both metrics. The previously documented optimized run #11324797 was 0.125 s / 984 KB; that is a separate historical pair, not this source's current measurement. Teaching sources remain unchanged.

- `1753_geometry_optimized.java`: 0.109 s / 572 KB; retained teaching base `1753_geometry.java`: 0.109 s / 1816 KB.

Go and Rust rewrite the same optimum using the ratio q = cbrt(H/(2h)). When H ≤ 2h the displacement is zero. Otherwise set f = (q−1)(q+1) and compute h·f·sqrt(f). This uses the shared factor once and avoids subtracting two large squared lengths. The result is printed directly with six decimal places. Both versions use fixed byte buffers and round to millionths before writing decimal digits. Go uses the standard handles directly. Rust enters through C main and transfers its buffers through the C runtime.

The accepted base implementations [1753_geometry.cpp](1753_geometry.cpp), [1753_geometry.java](1753_geometry.java), [1753_geometry.py](1753_geometry.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. Teaching algorithms are retained. Revalidated basic-source rows use their own new exact-source Accepted metrics and IDs; those checks do not count as optimizations.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1753_geometry.cpp](1753_geometry.cpp) | G++ 13.2 x64 | geometry | O(1) | AC | 0.015 s | 132 KB | 11325580 |
| [1753_geometry.go](1753_geometry.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.031 s | 1088 KB | 11289561 |
| [1753_geometry.java](1753_geometry.java) \* | Java 1.8 | geometry | O(1) | AC | 0.109 s | 1816 KB | 11289563 |
| [1753_geometry.py](1753_geometry.py) \* | Python 3.12 x64 | geometry | O(1) | AC | 0.078 s | 400 KB | 11289562 |
| [1753_geometry.rs](1753_geometry.rs) | Rust 1.75 x64 | geometry | O(1) | AC | 0.046 s | 236 KB | 11325633 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1753_geometry_optimized.go](1753_geometry_optimized.go) | Go 1.14 x64 | geometry | O(1) | AC | 0.015 s | 284 KB | 11311227 |
| [1753_geometry_optimized.rs](1753_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(1) | AC | 0.015 s | 56 KB | 11311226 |
| [1753_geometry_optimized.java](1753_geometry_optimized.java) | Java 1.8 | geometry | O(1) | AC | 0.109 s | 572 KB | 11327331 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
