# 1572. Yekaterinozavodsk Great Well

[Timus 1572](https://acm.timus.ru/problem.aspx?space=1&num=1572) · difficulty 146 · geometry

Original problem by Alexander Ipatov and Alex Samsonov, from the USU Junior Contest (the Fourteenth Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region), October 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

The opening of a well and up to 100 manhole covers are each a circle
(type 1, size = radius), a square (type 2) or an equilateral triangle
(type 3, size = side), with integer sizes 1 … 100. A flat cover may be
turned and moved in space in any way. Count the covers that can be
dropped into the well.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The type and size of the well, then N (1 ≤ N ≤ 100) and the type and
size of each cover.

## Output

The number of covers that fit through.

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation.

## Examples

### Example 1

Input:

```
2 10
3
3 20
1 5
2 11
```

Output:

```
2
```

### Example 2

Input:

```
1 5
2
2 10
1 6
```

Output:

```
1
```

## Solution

A cover held upright and pushed straight down meets the plane of the
opening along parallel chords of itself, so it passes when, in some
direction, its longest chord fits into the opening. The cover's best
direction gives a circle's diameter 2r, a square's side a and a
triangle's height a·√3/2 (the chords parallel to a height). The opening
holds segments up to its longest one: a circle's diameter 2R, a
square's diagonal A·√2 and a triangle's side A.

Squared and multiplied by 4, all these lengths are integers: 16r², 4a²
and 3a² for the covers, 16R², 8A² and 4A² for the well, so the
comparison is exact and a cover that just touches still passes. `O(N)`.
The answers agree with an independent program for every pair of a well
and a cover of any shape and size.

Pitfalls:

- the size of a circle is its radius, not its diameter;
- a triangle passes by its height, not by its side, so a triangle of
  side 16 still goes into a square well of side 10 (test 06);
- equal sizes pass: a square of side 10 goes through a circle of
  radius 5 (the second example), so floating-point comparisons need care.

## Optimized solutions

`1572_geometry_optimized.py` is reused byte for byte. Its exact-source CPython 3.12 Accepted #11325457 records 0.078 s / 720 KB; the saved 2026-11-20 current Python-family compiler comparison gives time rank 4/28 and memory rank 18/28. Below 1024 KB, strict admission uses time only, so the top-ten criterion passes. The asterisk remains because the separate language target requires first place in both metrics. The unchanged source also has PyPy 3.10 Accepted #11325701, 0.14 s / 264 KB: PyPy uses less memory, while the selected CPython run has lower recorded time. These are paired measurements from different runs, not a combined result. No new source, algorithm or submission is needed; all teaching sources remain.

`1572_geometry_optimized.py`. Keep exact squared-chord comparisons using NARROWEST/WIDEST shape coefficients, including equality. Read each cover, test its scaled integer square, then discard it instead of retaining the covers list. O(n) time and constant geometric state plus token buffers. Flush the single answer before direct interpreter exit; the simple geometric derivation remains.

Compared with `1572_geometry.py`: selected CPython time 0.093 s → 0.078 s; memory 384 KB → 720 KB. Time is lower by 16.13%, while memory increases by 87.5%; this run qualifies by its time rank, not a 30% improvement. The earlier 0.14 s / 264 KB PyPy measurement is retained above as a memory tradeoff.

`1572_geometry_optimized.rs`. Keep the same exact squared-chord comparison using NARROWEST and WIDEST shape factors, including equality. Read each cover directly, compare its u64 scaled square with the hole and discard it, instead of retaining the whole parsed vector. Direct output replaces formatting. O(n) time and O(1) auxiliary space; the readable geometric derivation and basic source remain.

Compared with `1572_geometry.rs`: time 0.031 s → 0.046 s; memory 228 KB → 60 KB.

The optimized Java solution parses the numbers by hand from a 4 KB
buffer filled from `System.in` instead of creating a `Scanner`, so the
JVM does not load the scanner and its regular expressions; the
comparison of the squared lengths is the same:
{1572_geometry_optimized.java}.

### Measured gains

Each optimized version has Accepted and qualifies by the applicable ranking or improvement rule. The selected Python run qualifies by time rank; the Java reductions below describe its own paired metrics. The base sources are retained. Negative reduction means increased cost. The asterisk concerns the separate rating target only.

- `1572_geometry_optimized.java`: time reduction +44.29%; memory
  reduction +80.86%; base: `1572_geometry.java`.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1572_geometry_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1572_geometry.cpp](1572_geometry.cpp) | G++ 13.2 x64 | geometry | O(N) | AC | 0.015 s | 128 KB | 11287799 |
| [1572_geometry.go](1572_geometry.go) | Go 1.14 x64 | geometry | O(N) | AC | 0.031 s | 1072 KB | 11287801 |
| [1572_geometry.java](1572_geometry.java) | Java 1.8 | geometry | O(N) | AC | 0.140 s | 1776 KB | 11287805 |
| [1572_geometry.py](1572_geometry.py) | Python 3.12 x64 | geometry | O(N) | AC | 0.093 s | 384 KB | 11287803 |
| [1572_geometry.rs](1572_geometry.rs) | Rust 1.75 x64 | geometry | O(N) | AC | 0.031 s | 228 KB | 11287810 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1572_geometry_optimized.java](1572_geometry_optimized.java) | Java 1.8 | geometry | O(N) | AC | 0.078 s | 340 KB | 11304529 |
| [1572_geometry_optimized.rs](1572_geometry_optimized.rs) \* | Rust 1.75 x64 | geometry | O(n) time; O(1) space | AC | 0.046 s | 60 KB | 11325506 |
| [1572_geometry_optimized.py](1572_geometry_optimized.py) \* | Python 3.12 x64 | geometry | O(n) time; O(1) state plus bounded token buffers | AC | 0.078 s | 720 KB | 11325457 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
