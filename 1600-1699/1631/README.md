# 1631. Drunk King 2

[Timus 1631](https://acm.timus.ru/problem.aspx?space=1&num=1631) · difficulty 493 · math

Original problem by Igor Chevdar, from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A king tours an m × n chessboard with odd sides: it starts and ends in a
corner, visits every other square exactly once, never crosses its own
path, and, being drunk, never makes two moves in a row in the same
direction. Find the length of the shortest such tour, measuring between
square centres (a straight move is 1, a diagonal one √2).

## Input

One line with m and n (6 < m, n < 500, both odd).

## Output

The length of the shortest tour with precision 10⁻⁹.

## Examples

### Example 1

Input:

```
7 7
```

Output:

```
55.213203435596425732025330863145
```

## Solution

A tour has mn moves. With D diagonal moves its length is
mn + D·(√2−1), so we want the smallest D. The implementations evaluate
the accepted formula with D=m+n+1 using constant time and space.

To see why fewer diagonals are impossible, split the squares into four
classes by row and column parity: A=even/even, B=even/odd, C=odd/even,
D₀=odd/odd. For odd dimensions, |A|−|D₀|=(m+n)/2. The checkerboard colour
A∪D₀ has one more square than B∪C.

Let x count B–C diagonals and y count A–D₀ diagonals. Orthogonal moves
join the two colours and cancel when subtracting their degree sums.
Each diagonal contributes twice to its own colour, hence y−x=1.
Similarly, subtracting the degree sum on D₀ from that on A cancels
all A–D₀ diagonals. It leaves a difference of m+n between orthogonal
incidences at A and D₀.

Count that difference at the other ends, in B∪C. A square without a
diagonal must have one horizontal and one vertical edge: two along
one axis would go straight or revisit a square. Its two neighbours
are therefore one in A and one in D₀, giving zero difference. A square
with one diagonal contributes at most one; with two it contributes
zero. There are at most 2x such one-diagonal squares. Thus m+n≤2x,
and x+y=2x+1≥m+n+1.

The 7×7 example attains this bound with 15 diagonals. Cut its tour
between zero-based rows 3 and 4, where the only crossings are vertical
in columns 1, 2, 4 and 6. Insert two rows. Replace those edges with
the move sequences `↓←↓→↓`, `↓→↓←↓`, `↓→↙↓` and `↓↙→↓`, respectively.
They cover all 14 new squares and use two diagonals in distinct unit
squares. Both ends of each replacement keep the old vertical direction.
The top cut has the same crossings, so repetition gives optimal tours
for every odd height with width seven. Transposition swaps the sides.
To widen the sample, first reflect it left to right. Insert four columns
after column 4. The two edges across this cut start at (2,4) and (5,4)
on the left. Replace them by `↗↑→↘↑→↓→` and `↘→↑←↑→↑←↑→↑↘→↓←↓→↙↓→↑↘`,
respectively, keeping their original right endpoints shifted by four.
These paths cover the new block and add four diagonals. Their turns
also allow another copy at the same cut. At the row cut, the first three
columns keep their two outer vertical edges. Every other pair of
columns, including both new pairs, has one vertical edge. The same
two-row construction works block by block, reflecting the two-column
path when needed. This attains the bound when at least one dimension
is 3 modulo 4.
[Official diagram](https://sp.urfu.ru/usu/okt_08/USU_champ_08.pdf#page=4)

At the largest sizes binary64 evaluation is accurate enough for 10⁻⁹;
use a decimal point regardless of the locale.

### Both sides are 1 modulo 4

Start with this 9×9 tour. Visit the cells in order, then return from 81 to 1. It has 19 diagonals.

```text
 1 81 79 78 75 74 72 70 69
 3  2 80 77 76 51 73 71 68
 4  5 45 46 49 50 52 67 66
 6 43 44 47 48 54 53 64 65
 7 42 41 39 38 55 56 63 62
 9  8 40 37 35 34 57 61 60
10 11 19 20 36 33 32 58 59
12 15 18 21 23 24 27 31 30
13 14 16 17 22 25 26 28 29
```

The following four-row strips have paths listed in port order. For ports 0 and 1 use `↓↘←↓→↙↓` / `↓→↓→↑→↓↙→↓←↖↓←↓`. For ports 0 and 3 use `↓→↙↓↘←↓` / `↓→↓←↖↓←↓→↓↗→↓←↓`. Each strip covers four new rows of five cells, adds four diagonals, and keeps the boundary moves vertical. In a two-column block with one port, repeat its two-row U-shaped insertion twice.

First widen at the cut after column 4. The horizontal crossings are in rows 0, 2, 5 and 7. Transpose the strip for ports 0 and 3 onto rows 2 through 6, and use the transposed pair paths in rows 0–1 and 7–8. The cut repeats, and each insertion adds one vertical crossing per new column pair at the cut after row 3. Then extend the height at that row cut. Use the strip for ports 0 and 1 in the first five columns and the pair paths everywhere else. Each extension adds four diagonals for four rows or columns. The two starting boards now cover every allowed rectangle.

## Optimized solutions

The Go and Java alternatives evaluate the identical closed formula mn + (m+n+1)(√2−1). They change only I/O: Go parses the two integers with fixed64-byte buffers and writes the integer and twelve-digit fractional parts directly, without fmt, strconv or whole-input storage; Java reads the two integers directly and prints the double without Scanner, Locale or String.format. Go prints twelve fractional digits; Java Double.toString preserves sufficient significant digits. Independent 60-digit checks include every allowed square and every 7-by-n board; they validate numerical evaluation, not a new proof of the tour formula. Time and space remain O(1). All ordinary sources remain; C++, Python and Rust reuse admitted bases.

The accepted base implementations [1631_math.cpp](1631_math.cpp), [1631_math.py](1631_math.py), [1631_math.rs](1631_math.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

### Accepted source update

The entries below use the shared [rating criteria](../../RATING_CRITERIA.md) and exact-source Accepted evidence. Earlier performance discussions describe historical runs and snapshots, not a separate current admission rule. Meaningful simple versions and earlier distinct implementations remain available.

`1631_geometry_parsing_optimized.java`. Keep the geometric formula and write an explicitly rounded fixed-point answer with nine decimal places instead of loading general decimal formatting. All 61009 legal board pairs were checked against a high-precision reference; absolute rounding error stays below 1e-9. Place the bounded input buffer and parsing methods directly in Main, removing one helper-class load and allocation. The complete mathematical formula, output scale and fixed-point formatter are unchanged. Flush both output streams before Runtime.halt(0), after the complete standalone answer has been written.

Accepted #11329242 (Java 1.8): **0.093 s / 472 KB**. Archived comparison: `1631_math.java` (Java 1.8) — 0.109 s / 1800 KB (#11288424).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1631_math.cpp](1631_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 140 KB | 11288421 |
| [1631_math.go](1631_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.031 s | 1084 KB | 11288422 |
| [1631_math.java](1631_math.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 1800 KB | 11288424 |
| [1631_math.py](1631_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.093 s | 412 KB | 11288423 |
| [1631_math.rs](1631_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 252 KB | 11328279 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1631_math_optimized.java](1631_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.109 s | 460 KB | 11315360 |
| [1631_math_optimized.go](1631_math_optimized.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 292 KB | 11315798 |
| [1631_geometry_parsing_optimized.java](1631_geometry_parsing_optimized.java) | Java 1.8 | geometry, parsing | O(1) | AC | 0.093 s | 472 KB | 11329242 |
