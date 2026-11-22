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

## Checking

Repository tests compare the complete output text, ignoring only trailing whitespace. Preserve meaningful spaces, line breaks, case and punctuation. In particular, preserve the table alignment and leading padding in each field.

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

`1506_implementation_optimized.py` is reused byte for byte, without another source file or a new algorithm. Its exact-source CPython 3.12 Accepted #11327027 measures 0.046 s / 720 KB. The saved 2026-11-20 current Python-family compiler cohort gives time rank 1/291, memory rank 285/291. Because this run uses less than 1024 KB, the strict top-ten or top-15% gate uses time only; the asterisk still records the separate language rating target. The same unchanged file also has its earlier PyPy 3.10 Accepted #11325476, 0.125 s / 248 KB. These are paired measurements from different runs: CPython supplies the selected time/rank result, while PyPy uses less memory. Earlier memory-saving observations in this section refer to that PyPy measurement, not to the CPython row. All teaching sources remain unchanged.

`1506_implementation_optimized.py`. Keep height=ceil(n/k) and the same column-major layout. Parse the numbers once and visit indices row,row+height,... directly, emitting one right-justified width-four row at a time. This removes the list of all formatted output rows and the sliced string-number list. The numeric input list remains: O(n) time and O(n) storage. Leading padding and line breaks are meaningful. The Accepted row identifies the actual judge runtime and its paired time/memory. Output is flushed before os._exit(0) skips interpreter teardown; the measured memory improvement is runtime-specific and does not imply an asymptotic speedup.

Compared with `1506_implementation.py`: time 0.093 s → 0.125 s; memory 460 KB → 248 KB.

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

`1506_implementation_optimized.rs`. Store at most 100 values in one fixed u16 array, index them by column and row, and emit the required padding directly. No per-value strings, joined rows or output builder are retained. The work is O(N); storage is bounded by that fixed array and numeric output state. Rust uses the C runtime for input/output, avoiding full decoded input/output String values and Rust formatting. The simple accepted source remains unchanged.

Compared with `1506_implementation.rs`: time 0.015 s → 0.031 s; memory 252 KB → 52 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

Earlier PyPy comparison: `1506_implementation_optimized.py`: time place 279/291, memory place 2/291 in this comparable sample.

`1506_implementation_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

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
| [1506_implementation_optimized.rs](1506_implementation_optimized.rs) \* | Rust 1.75 x64 | implementation | O(N) | AC | 0.031 s | 52 KB | 11325099 |
| [1506_implementation_optimized.py](1506_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(n) time; O(n) space | AC | 0.046 s | 720 KB | 11327027 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
