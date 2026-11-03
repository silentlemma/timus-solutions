# 1010. The steepest chord above a discrete function

[Timus 1010](https://acm.timus.ru/problem.aspx?space=1&num=1010) · difficulty 295 · math

Original problem from the Third Open USTU Collegiate Programming Contest (PhysTech Cup), 2000.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A function is given by its values `f(1), ..., f(N)` (`2 ≤ N ≤ 100 000`,
`-2^31 ≤ f(i) ≤ 2^31 - 1`). A pair of points `A = (a, f(a))` and
`B = (b, f(b))`, `a < b`, is **valid** if every point `(i, f(i))` with
`a < i < b` lies strictly below the line `AB`. Among the valid pairs find one
with the largest absolute value of the slope of `AB`; if there are several,
the one with the smallest `a`.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then the `N` values `f(1), ..., f(N)`, one per line.

## Output

`a` and `b`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
1
5
2
-4
```

Output:

```
3 4
```

### Example 2

Input:

```
2
7
7
```

Output:

```
1 2
```

## Solution

The answer is always a pair of neighbours `(a, a + 1)`: the first one with
the largest `|f(a + 1) - f(a)|`.

Why: the slope of a chord from `a` to `b` is the mean of the slopes of the
`b - a` unit steps under it, so its absolute value is at most the largest
absolute step slope. Neighbouring pairs are always valid (there is nothing
between them), so the maximum is reached on a step. A longer chord can only
tie if all its steps have the same slope — but then the points between lie on
the line, not strictly below it, and the chord is not valid. So the steps
with the largest `|difference|` are exactly the optimal pairs, and the first
of them has the smallest `a`.

`O(N)` time and `O(1)` memory (or `O(N)` if the values are stored).

Pitfalls:

- a difference of two values can reach `2^32 - 1`: use 64-bit integers;
- ties: keep the first maximum (a strict comparison while scanning left to
  right);
- the validity condition looks like it needs a convex hull, but it never
  matters for the answer.

## Optimized solutions

The maximum absolute chord slope is attained by adjacent points. The optimized scan keeps only the previous value and the first greatest difference, so it never retains all values or a difference array. Strict improvement preserves the required first tie; subtract in 64-bit arithmetic before taking the absolute value. Buffered native input and line-by-line Python input reduce overhead without changing this proof.

- `1010_math_optimized.cpp`: 0.015 s / 88 KB; base `1010_math.cpp`: 0.046 s / 136 KB; relative change: time -67.4%, memory -35.3%.
- `1010_math_optimized.java`: 0.093 s / 388 KB; base `1010_math.java`: 0.109 s / 580 KB; relative change: time -14.7%, memory -33.1%.
- `1010_math_optimized.py`: 0.078 s / 360 KB; base `1010_math.py`: 0.062 s / 14648 KB; relative change: time +25.8%, memory -97.5%.

## Language notes

The saved rating snapshot is from 1–2 November 2026. C++ requires the top 15% or the first 10 places in both time and memory; other families require first place in both. Equal results share a place. Empty competitor samples establish formal coverage only.

- C++: preferred teaching base `1010_math.cpp`; covering source `1010_math_optimized.cpp`; time/memory places 1/1, other-author entries 73/73.

- Go: preferred teaching base `1010_math.go`; covering source `1010_math.go`; time/memory places 1/1, other-author entries 0/0.

- Java: preferred teaching base `1010_math.java`; covering source `1010_math_optimized.java`; time/memory places 3/1, other-author entries 9/9.

- Python/PyPy: preferred teaching base `1010_math.py`; covering source `1010_math_optimized.py`; time/memory places 1/1, other-author entries 12/12.

- Rust: preferred teaching base `1010_math.rs`; covering source `1010_math.rs`; time/memory places 1/1, other-author entries 0/0.

## Solutions

The simple table includes the preferred teaching sources and preserved Accepted alternatives. The language notes identify the preferred base for each family.

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1010_math.cpp](1010_math.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.046 s | 136 KB | 11277744 |
| [1010_math.go](1010_math.go) | Go 1.14 x64 | math | O(N) | AC | 0.031 s | 2668 KB | 11277751 |
| [1010_math.java](1010_math.java) | Java 1.8 | math | O(N) | AC | 0.109 s | 580 KB | 11277761 |
| [1010_math.py](1010_math.py) | Python 3.12 x64 | math | O(N) | AC | 0.062 s | 14648 KB | 11277757 |
| [1010_math.rs](1010_math.rs) | Rust 1.75 x64 | math | O(N) | AC | 0.046 s | 3696 KB | 11277762 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1010_math_optimized.cpp](1010_math_optimized.cpp) | G++ 13.2 x64 | math | O(N) | AC | 0.015 s | 88 KB | 11309321 |
| [1010_math_optimized.java](1010_math_optimized.java) \* | Java 1.8 | math | O(N) | AC | 0.093 s | 388 KB | 11309322 |
| [1010_math_optimized.py](1010_math_optimized.py) | Python 3.12 x64 | math | O(N) | AC | 0.078 s | 360 KB | 11309320 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
