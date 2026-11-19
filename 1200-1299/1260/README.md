# 1260. The fussy photographer

[Timus 1260](https://acm.timus.ru/problem.aspx?space=1&num=1260) · difficulty 112 · dp

Original problem by Alexander Ipatov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N students aged 1, 2, …, N years (1 ≤ N ≤ 55) sit in a row. The one
aged 1 sits at the left end, and the ages of any two neighbours differ by
at most 2. How many such rows are there?

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

The number of rows.

## Checking

Repository tests compare the output tokens exactly; whitespace between tokens is insignificant.

## Examples

### Example 1

Input:

```
4
```

Output:

```
4
```

## Solution

Let a(k) be the number of rows for the ages 1..k. Look at who sits
second:

- age 2: the rest is a row of 2..k starting with 2, the same problem
  shifted by one, a(k − 1) ways;
- age 3, then age 2: the next must be 4, and the rest is a row of 4..k
  starting with 4, a(k − 3) ways;
- age 3, but 2 later: the neighbours of 2 can only be 1, 3 and 4, and 1
  and 3 are already taken next to each other, so 2 sits at the right end
  next to 4. This forces the zigzag 1, 3, 5, … up the odd ages and back
  down the even ones to 4, 2: exactly one row.

So a(k) = a(k − 1) + a(k − 3) + 1, with a(1) = a(2) = 1 and a(3) = 2.
Running the rule backwards gives a(0) = 0 and a(−1) = −1, which lets the
loop start from k = 1 with no special cases. a(55) = 1 388 937 263
still fits in 32 bits, but C++, Go, Java and Rust use 64-bit integers,
and Python uses its arbitrary-precision integers. `O(N)`.

Pitfalls:

- the third case is easy to miss: for N = 5 it is the row 1, 3, 5, 4, 2
  (test 05);
- N = 1 and N = 2 both have a single row (tests 02, 03).

The recurrence was compared with listing all permutations for N up to
10.

## Optimized solutions

`1260_dp_optimized.py`. Keep a(k)=a(k-1)+a(k-3)+1 and the same rolling initial state (-1,0,1). Three accumulators replace no additional table: each iteration simultaneously advances all three old values. Time O(N), three bounded integer slots. With N<=55 the counts fit signed 64 bits; a conservative bound a(N)<2^N suffices. Read one byte token and keep the recurrence at module scope, avoiding the wrapper call. The standalone judge program explicitly flushes stdout before os._exit(0), skipping normal interpreter finalization. Its own Accepted measures the memory gain. The exit change alone does not improve asymptotic complexity, and its runtime benefit is not a portable guarantee. The simple version remains unchanged.

Compared with `1260_dp.py`: time 0.109 s → 0.125 s; memory 404 KB → 200 KB.

`1260_dp_optimized.rs`. Keep a(k)=a(k-1)+a(k-3)+1 and the same rolling initial state (-1,0,1). Three accumulators replace no additional table: each iteration simultaneously advances all three old values. Time O(N), three bounded integer slots. With N<=55 the counts fit signed 64 bits; a conservative bound a(N)<2^N suffices. Keep i64 accumulators and emit the final number directly; no decoded input or Rust output formatting is retained. The Rust variant reads and writes through the C runtime, without retaining a decoded input String or building a formatted output String. The simple Accepted source is preserved.

Compared with `1260_dp.rs`: time 0.015 s → 0.031 s; memory 232 KB → 56 KB.

The optimized Java solution reads the single number N digit by digit
straight from `System.in` instead of creating a `Scanner`, whose setup
costs far more than the recurrence itself, at most 54 steps; the
computation is the same: {1260_dp_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1260_dp_optimized.java`: time reduction -17.20%; memory reduction
  +79.59%; base: `1260_dp.java`.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1260_dp_optimized.py`: time place 37/44, memory place 1/44 in this comparable sample.

`1260_dp_optimized.rs`: no comparable rival result establishes a ranking; admission follows its measured improvement over the simple source.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1260_dp.cpp](1260_dp.cpp) | G++ 13.2 x64 | dp | O(N) | AC | 0.015 s | 128 KB | 11284122 |
| [1260_dp.go](1260_dp.go) | Go 1.14 x64 | dp | O(N) | AC | 0.046 s | 1076 KB | 11284124 |
| [1260_dp.java](1260_dp.java) | Java 1.8 | dp | O(N) | AC | 0.093 s | 1568 KB | 11284130 |
| [1260_dp.py](1260_dp.py) | Python 3.12 x64 | dp | O(N) | AC | 0.109 s | 404 KB | 11284128 |
| [1260_dp.rs](1260_dp.rs) | Rust 1.75 x64 | dp | O(N) | AC | 0.015 s | 232 KB | 11284131 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1260_dp_optimized.java](1260_dp_optimized.java) | Java 1.8 | dp | O(N) | AC | 0.109 s | 320 KB | 11304342 |
| [1260_dp_optimized.py](1260_dp_optimized.py) \* | PyPy 3.10 x64 | dp | O(N) | AC | 0.125 s | 200 KB | 11324915 |
| [1260_dp_optimized.rs](1260_dp_optimized.rs) \* | Rust 1.75 x64 | dp | O(N) | AC | 0.031 s | 56 KB | 11325091 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
