# 1101. A robot steered by a boolean expression

[Timus 1101](https://acm.timus.ru/problem.aspx?space=1&num=1101) · difficulty 527 · parsing, simulation

Original problem by Pavel Atnashev, from the Tetrahedron Team Contest, May 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A robot starts at `(0, 0)` in the field `[−N..N] × [−N..N]` (`N ≤ 100`)
heading in the direction `(1, 0)`. It moves one cell at a time. At each
of `M ≤ 100` forks it evaluates a boolean expression (up to 250
characters, with `NOT`, `AND`, `OR` from the highest priority to the
lowest, parentheses, `TRUE`, `FALSE` and registers `A`–`Z`, all `FALSE` at
first) and turns right if the value is `TRUE`, left otherwise. Each of
`K ≤ 100` other cells flips one register when the robot is on it. Print
every cell of the robot's route until it leaves the field.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The expression; `N`, `M` and `K`; `M` lines with a fork; `K` lines with
a cell and the register it flips.

## Output

The cells of the route, one per line.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
NOT((A OR NOT B) AND (A OR B)) OR NOT (A AND NOT B OR TRUE)
1 5 2
1 0
1 1
1 -1
-1 -1
-1 1
0 1 A
-1 0 D
```

Output:

```
0 0
1 0
1 -1
0 -1
-1 -1
-1 0
-1 1
0 1
1 1
```

## Solution

Split the expression into words (`NOT`, `AND`, `OR`, `TRUE`, `FALSE`, a
register) and parentheses, and build a tree once by recursive descent
with one function per priority level: an `OR` of `AND`s of `NOT`s of
atoms, where an atom is a constant, a register or an expression in
parentheses.

Then walk. On each cell inside the field: print it; if it is a switch,
flip its register; if it is a fork, evaluate the tree and turn right
(`(dx, dy) → (dy, −dx)`) for `TRUE` or left (`(dx, dy) → (−dy, dx)`) for
`FALSE`; step forward. Stop as soon as the robot is outside the field.
`O(L · |E|)` for a route of `L` cells and an expression of length `|E|`.

Pitfalls:

- `NOT A AND B` means `(NOT A) AND B`, and `A OR B AND C` means
  `A OR (B AND C)`;
- words may stand right next to parentheses, as in `NOT(A OR(B))`, so
  the words are cut out of the text rather than split at spaces;
- the turn depends on the registers at the moment the robot reaches the
  fork, after the switches it passed earlier.

The answers were checked against a walk that translates the expression
into Python's `not`, `and` and `or`, which have the same priorities, and
evaluates it with `eval`.

## Optimized solutions

C++ and Go use recursive descent with NOT > AND > OR to emit postfix bytecode and collect a mask of the registers the expression reads. The current registers occupy 26 bits. At each fork, reuse a cached result if those relevant bits match its mask. Otherwise evaluate the full bytecode with a small Boolean stack. Each cell occupies one byte and an 8192-byte buffer streams the route. Print the current cell before applying its switch or turn. Let E be the expression length, S the number of printed cells and F the number of fork visits that require evaluation. Grid setup costs O(N²), so the total time is O(N² + E + S + FE) and space is O(N² + E). The admitted Java, Python and Rust bases also serve as fast versions.

The accepted G++ 13.2 x64 run takes 0.031 s versus 0.015 s for the base and uses 224 KB versus 628 KB.

The accepted base implementations [1101_parsing.java](1101_parsing.java), [1101_parsing.py](1101_parsing.py), [1101_parsing.rs](1101_parsing.rs) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

Original files retain their syntax trees and source-bound Accepted. New C++/Go use fixed postfix storage, a direct byte grid and bounded route output; only the relevant register mask is cached. The grid uses O(N²) cells even when few objects exist, while route storage stays bounded. Actual memory/time gains come from the attached judge receipt, not a claim of uniformly faster evaluation.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1101_parsing.cpp](1101_parsing.cpp) | G++ 13.2 x64 | parsing | O(L·len(E)) | AC | 0.015 s | 628 KB | 11279157 |
| [1101_parsing.go](1101_parsing.go) | Go 1.14 x64 | parsing | O(L·len(E)) | AC | 0.031 s | 1780 KB | 11279158 |
| [1101_parsing.java](1101_parsing.java) \* | Java 1.8 | parsing | O(L·len(E)) | AC | 0.093 s | 2192 KB | 11279160 |
| [1101_parsing.py](1101_parsing.py) \* | Python 3.12 x64 | parsing | O(L·len(E)) | AC | 0.078 s | 1408 KB | 11279159 |
| [1101_parsing.rs](1101_parsing.rs) \* | Rust 1.75 x64 | parsing | O(L·len(E)) | AC | 0.015 s | 552 KB | 11279161 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1101_parsing_optimized.cpp](1101_parsing_optimized.cpp) \* | G++ 13.2 x64 | parsing | O(N² + E + S + FE) | AC | 0.031 s | 224 KB | 11315671 |
| [1101_parsing_optimized.go](1101_parsing_optimized.go) \* | Go 1.14 x64 | parsing | O(N² + E + S + FE) | AC | 0.031 s | 912 KB | 11315890 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
