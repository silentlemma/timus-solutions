# 1139. Counting the blocks a diagonal flight passes over in a grid of streets

[Timus 1139](https://acm.timus.ru/problem.aspx?space=1&num=1139) · difficulty 78 · number_theory

Original problem from the Central Russia regional quarterfinal, Rybinsk, October 17–18, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N` avenues and `M` streets, `1 < N, M < 32000`, cut a city into square
blocks. A helicopter flies straight from the south-west corner to the
north-east corner. Count the blocks it flies over; a block is the open
inside of its square, so touching a corner does not count.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `M`.

## Output

The number of blocks.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
4 3
```

Output:

```
4
```

### Example 2

Input:

```
3 3
```

Output:

```
2
```

## Solution

The blocks form an `a × b` grid with `a = N − 1` and `b = M − 1`, and the
flight is its diagonal. It first enters one block, and each time it
crosses a line of the grid it enters a new block. It crosses the
`a − 1` inner vertical lines and the `b − 1` inner horizontal lines, but
at an inner corner of the grid it crosses one of each at the same moment
and enters only one new block. The diagonal passes through the points
`(k·a/g, k·b/g)`, so it meets exactly `g − 1` inner corners, where
`g = gcd(a, b)`. In total
`1 + (a − 1) + (b − 1) − (g − 1) = a + b − gcd(a, b)`. `O(log min(a, b))`.

Pitfalls:

- the input counts lines, not blocks: subtract one from each;
- in a square grid the diagonal goes through every corner on its way and
  crosses only `a` blocks;
- with a single row or column the flight crosses every block in it.

The answers were compared with a column-by-column count of the blocks
under the diagonal, using exact floor and ceiling, for all `N, M ≤ 40` and
on every test.

## Optimized solutions

`1139_number_theory_optimized.py`. Keep the grid-crossing formula a+b-gcd(a,b), with a=N-1,b=M-1. Compute gcd by the iterative Euclidean remainder loop. This preserves the corner-crossing correction and uses O(log min(N,M)) bounded-integer steps with O(1) auxiliary state; it is not a new geometric algorithm. Inline the gcd loop instead of importing math.gcd and parse the two byte tokens directly. The measured benefit is lower judge memory, not a claim that Python-level gcd runs faster than the native library. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1139_number_theory.py`: time 0.078 s → 0.125 s; memory 400 KB → 220 KB.

`1139_number_theory_optimized.rs`. Keep the grid-crossing formula a+b-gcd(a,b), with a=N-1,b=M-1. Compute gcd by the iterative Euclidean remainder loop. This preserves the corner-crossing correction and uses O(log min(N,M)) bounded-integer steps with O(1) auxiliary state; it is not a new geometric algorithm. The iterative loop replaces recursive gcd, while direct numeric I/O removes the retained input String. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1139_number_theory.rs`: time 0.015 s → 0.031 s; memory 248 KB → 56 KB.

The optimized Java solution reads the two numbers byte by byte with
`System.in.read` instead of `Scanner` and computes the gcd in a loop
instead of by recursion. The formula is the same; the solution takes
360 KB instead of 1592 KB, with the same time.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1139_number_theory_optimized.py`: time place 47/57, memory place 1/57 in this comparable sample.

`1139_number_theory_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1139_number_theory.cpp](1139_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 128 KB | 11279432 |
| [1139_number_theory.go](1139_number_theory.go) | Go 1.14 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 1060 KB | 11279433 |
| [1139_number_theory.java](1139_number_theory.java) | Java 1.8 | number_theory | O(log min(N, M)) | AC | 0.109 s | 1592 KB | 11279436 |
| [1139_number_theory.py](1139_number_theory.py) | Python 3.12 x64 | number_theory | O(log min(N, M)) | AC | 0.078 s | 400 KB | 11279435 |
| [1139_number_theory.rs](1139_number_theory.rs) | Rust 1.75 x64 | number_theory | O(log min(N, M)) | AC | 0.015 s | 248 KB | 11279438 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1139_number_theory_optimized.java](1139_number_theory_optimized.java) | Java 1.8 | number_theory | O(log min(N, M)) | AC | 0.093 s | 360 KB | 11303570 |
| [1139_number_theory_optimized.py](1139_number_theory_optimized.py) \* | PyPy 3.10 x64 | number_theory | O(log min(N,M)) | AC | 0.125 s | 220 KB | 11324847 |
| [1139_number_theory_optimized.rs](1139_number_theory_optimized.rs) \* | Rust 1.75 x64 | number_theory | O(log min(N,M)) | AC | 0.031 s | 56 KB | 11324856 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
