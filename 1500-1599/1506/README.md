# 1506. Columns of Numbers

[Timus 1506](https://acm.timus.ru/problem.aspx?space=1&num=1506) · difficulty 134 · implementation

Original problem by Stanislav Vasiliev, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Print N numbers from 0 to 999 (1 ≤ N ≤ 100) in K columns (1 ≤ K ≤ N)
with as few rows as possible. All columns have the same height except
the last, which may be shorter. The numbers fill the first column top
to bottom, then the second, and so on. Each number is right-aligned in
a field of 4 characters, and no line has trailing spaces.
It is guaranteed that a table with exactly K nonempty columns exists.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and K, then the N numbers.

## Output

The table.

## Examples

### Example 1

Input:

```
7 3
1 2 30 40 50 600 700
```

Output:

```
   1  40 700
   2  50
  30 600
```

## Solution

The fewest rows are H = ⌈N / K⌉. Any valid height h must satisfy h ≥ H
and (K − 1)·h < N. The existence guarantee therefore gives
(K − 1)·H < N, so height H leaves the last column nonempty.
Column c holds the numbers with
indices c·H to c·H + H − 1, so row r consists of the numbers c·H + r
that exist, for c = 0, 1, …; they stop at the first column that has run
out, which can only be the last one. Print each in a field of 4 and end
the row there. `O(N)`.

Pitfalls:

- the numbers go down the columns, not along the rows (test 01);
- every number takes 4 characters, the first one too, so each line
  starts with spaces (test 01);
- when the last column is shorter, the lower rows end one number
  earlier, without trailing spaces (test 06);
- the existence guarantee matters: the last column must contain at
  least one number (test 06); not every pair with 1 ≤ K ≤ N is feasible;
- K = N gives a single row and K = 1 a single column (tests 03, 04).

## Optimized solutions

The optimized C++ solution keeps the numbers in a fixed array of 100
`int` on the stack instead of a `std::vector`, since N ≤ 100, so the
program allocates nothing on the heap:
{1506_implementation_optimized.cpp}.

The optimized Java solution pads each cell itself: it converts the
number with `Integer.toString` and puts spaces in front up to
4 characters, instead of calling `String.format`, which creates a new
formatter and parses the pattern for every cell. A number up to 999 has
at most three digits, so every cell gets at least one space in front:
{1506_implementation_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1506_implementation_optimized.cpp`: time reduction +0.00%; memory
  reduction +48.98%; base: `1506_implementation.cpp`.

- `1506_implementation_optimized.java`: time reduction +14.68%; memory
  reduction +56.56%; base: `1506_implementation.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1506_implementation.go](1506_implementation.go).
- [1506_implementation.rs](1506_implementation.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1506_implementation.cpp](1506_implementation.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 196 KB | 11287283 |
| [1506_implementation.go](1506_implementation.go) | Go 1.14 x64 | implementation | O(N) | AC | 0.015 s | 1108 KB | 11287284 |
| [1506_implementation.java](1506_implementation.java) | Java 1.8 | implementation | O(N) | AC | 0.109 s | 976 KB | 11287286 |
| [1506_implementation.py](1506_implementation.py) | Python 3.12 x64 | implementation | O(N) | AC | 0.093 s | 460 KB | 11287285 |
| [1506_implementation.rs](1506_implementation.rs) | Rust 1.75 x64 | implementation | O(N) | AC | 0.015 s | 252 KB | 11287287 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1506_implementation_optimized.cpp](1506_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(N) | AC | 0.015 s | 100 KB | 11304437 |
| [1506_implementation_optimized.java](1506_implementation_optimized.java) | Java 1.8 | implementation | O(N) | AC | 0.093 s | 424 KB | 11304438 |
