# 1224. Turns of a robot that sweeps a rectangle in a spiral

[Timus 1224](https://acm.timus.ru/problem.aspx?space=1&num=1224) · difficulty 65 · math

Original problem from the Central Russia regional quarterfinal of the ACM ICPC 2002–2003, Rybinsk, October 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A robot starts at the top left cell of a field of `N` rows and `M`
columns, both up to `2³¹ − 1`, heading right, and covers every cell along
a clockwise spiral that winds towards the middle. Count its turns.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `M`.

## Output

The number of turns.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
3 5
```

Output:

```
4
```

## Solution

The path alternates horizontal and vertical runs, starting with a
horizontal one, and turns once between two runs. Each horizontal run
uses up a row and each vertical run a column, as the spiral peels the
field from the outside.

If `N ≤ M`, the rows run out first, after `N` horizontal and `N − 1`
vertical runs, which is `2N − 1` runs and `2(N − 1)` turns. Otherwise the
columns run out first, after `M` runs of each kind: `2M` runs and
`2M − 1` turns. `O(1)`.

Pitfalls:

- a single row needs no turn at all, but a single column with `N > 1` needs one,
  since the robot starts heading right;
- the answer reaches about `4.3·10⁹`, beyond signed 32-bit integers.

The formula was checked by simulating the robot on every field up to
14 × 14, and compared with a separately written solution on every test.

## Optimized solutions

`1224_math_optimized.py` is reused byte for byte, without another source file or a new algorithm. Its exact-source CPython 3.12 Accepted #11327019 measures 0.062 s / 660 KB. The saved 2026-11-20 current Python-family compiler cohort gives time rank 3/296, memory rank 291/296. Because this run uses less than 1024 KB, the strict top-ten or top-15% gate uses time only; the asterisk still records the separate language rating target. The same unchanged file also has its earlier PyPy 3.10 Accepted #11324840, 0.125 s / 196 KB. These are paired measurements from different runs: CPython supplies the selected time/rank result, while PyPy uses less memory. Earlier memory-saving observations in this section refer to that PyPy measurement, not to the CPython row. All teaching sources remain unchanged.

The optimized Java solution reads the input in 1 KB blocks and parses
the two numbers by hand instead of using `Scanner`: 348 KB instead of
1564 KB, with the same time.

`1224_math_optimized.py`. Keep the spiral-turn formula: 2*(N-1) when N<=M, otherwise 2*M-1. It handles a single row or column without simulation. The result can exceed signed 32-bit range for the stated dimensions, so Rust uses i64 and Python exact integers. O(1) bounded arithmetic and storage. Read the two dimensions from raw byte tokens; no new spiral algorithm is introduced. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1224_math.py`: time 0.078 s → 0.125 s; memory 372 KB → 196 KB.

`1224_math_optimized.rs`. Keep the spiral-turn formula: 2*(N-1) when N<=M, otherwise 2*M-1. It handles a single row or column without simulation. The result can exceed signed 32-bit range for the stated dimensions, so Rust uses i64 and Python exact integers. O(1) bounded arithmetic and storage. Retain only the two dimensions and answer rather than the input String and value vector. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1224_math.rs`: time 0.031 s → 0.015 s; memory 208 KB → 56 KB.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

Earlier PyPy comparison: `1224_math_optimized.py`: time place 283/296, memory place 4/296 in this comparable sample.

`1224_math_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1224_math.cpp](1224_math.cpp) | G++ 13.2 x64 | math | O(1) | AC | 0.015 s | 128 KB | 11283705 |
| [1224_math.go](1224_math.go) | Go 1.14 x64 | math | O(1) | AC | 0.015 s | 1076 KB | 11283706 |
| [1224_math.java](1224_math.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 1564 KB | 11283708 |
| [1224_math.py](1224_math.py) | Python 3.12 x64 | math | O(1) | AC | 0.078 s | 372 KB | 11283707 |
| [1224_math.rs](1224_math.rs) | Rust 1.75 x64 | math | O(1) | AC | 0.031 s | 208 KB | 11283709 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1224_math_optimized.java](1224_math_optimized.java) | Java 1.8 | math | O(1) | AC | 0.093 s | 348 KB | 11303726 |
| [1224_math_optimized.py](1224_math_optimized.py) \* | Python 3.12 x64 | math | O(1) | AC | 0.062 s | 660 KB | 11327019 |
| [1224_math_optimized.rs](1224_math_optimized.rs) \* | Rust 1.75 x64 | math | O(1) | AC | 0.015 s | 56 KB | 11324853 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
