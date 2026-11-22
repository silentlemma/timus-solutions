# 1014. The smallest number with a given product of digits

[Timus 1014](https://acm.timus.ru/problem.aspx?space=1&num=1014) · difficulty 94 · greedy

Original problem from the Ural State University Internal Contest '99 #2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Given `N` (`0 ≤ N ≤ 10^9`), find the smallest positive integer `Q` whose
decimal digits multiply to exactly `N`, or report that there is none.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The integer `N`.

## Output

`Q`, or `-1` if no such number exists.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
36
```

Output:

```
49
```

### Example 2

Input:

```
0
```

Output:

```
10
```

## Solution

Two special cases first:

- `N = 0`: a number has digit product 0 exactly when it contains a zero, and
  the smallest such positive number is `10`;
- `N = 1`: the answer is `1` (not an empty number).

Otherwise no digit is 0 or 1 (a 1 only makes the number longer), so `Q`
consists of digits 2–9. A smaller number has fewer digits, and among numbers
of the same length the one with the digits in increasing order is the
smallest. So the task is to write `N` as a product of the fewest digits.

**Greedy:** divide `N` by 9 as long as possible, then by 8, 7, ..., 2, and
collect the digits. If something other than 1 is left, `N` has a prime
factor above 7 and the answer is `-1`. Print the collected digits in
increasing order.

Why the largest digits first: the powers of 3 are best packed into 9s (two
3s in one digit), the powers of 2 into 8s, and a leftover 3 and 2 form a
6 rather than two digits; dividing by 9, 8, ..., 2 in this order produces
exactly that packing. `O(log N)` division steps.

Pitfalls:

- `N = 0` and `N = 1`;
- the answer can have 12 digits (`10^9 = 2^9 · 5^9` gives `555555555888`):
  do not store it in a 32-bit integer — print the digits as a string.
- counting only divisions misses the cost of prepending digits: even
  [test 05](tests/05.in) builds a 12-digit answer.

## Optimized solutions

`1014_greedy_optimized.py` is reused byte for byte, without another source file or a new algorithm. Its exact-source CPython 3.12 Accepted #11327014 measures 0.078 s / 724 KB. The saved 2026-11-20 current Python-family compiler cohort gives time rank 6/482, memory rank 448/482. Because this run uses less than 1024 KB, the strict top-ten or top-15% gate uses time only; the asterisk still records the separate language rating target. The same unchanged file also has its earlier PyPy 3.10 Accepted #11325471, 0.125 s / 240 KB. These are paired measurements from different runs: CPython supplies the selected time/rank result, while PyPy uses less memory. Earlier memory-saving observations in this section refer to that PyPy measurement, not to the CPython row. All teaching sources remain unchanged.

`1014_greedy_optimized.py`. Keep the same greedy factorization by digits 9 down to 2 and reverse the collected digits. Zero gives 10, one gives 1, and a remaining factor gives -1. Byte input and a standalone execution path replace input() and the wrapper function. Time and auxiliary digit storage remain O(log(N+2)); no new asymptotic speedup is claimed. The Accepted row identifies the actual judge runtime and its paired time/memory. Output is flushed before os._exit(0) skips interpreter teardown; the measured memory improvement is runtime-specific and does not imply an asymptotic speedup.

Compared with `1014_greedy.py`: time 0.093 s → 0.125 s; memory 444 KB → 240 KB.

`1014_greedy_optimized.go`. Keep descending digit factorization and the special answers 10 for zero and 1 for one. Replace prepending formatted strings on every factor by appending byte digits to a fixed 32-cell array, then emit it backwards. Every factor is at least two and N<=10^9, so 32 cells suffice. This removes quadratic copying in the number of factors and repeated formatting; 256-byte input and 64-byte output buffers replace fmt/string machinery. Time O(log(N+2)), auxiliary storage O(1) under the stated input bound. The recorded admission is by ranking, not a claimed 30% measurement gain.

Compared with `1014_greedy.go`: time 0.031 s → 0.031 s; memory 1096 KB → 780 KB.

The optimized Java solution parses the number byte by byte from
`System.in` instead of using `Scanner`, and appends the digits and
reverses the string once instead of inserting each digit at the front:
380 KB instead of 1604 KB, with the same time.

## Language notes

The added sources are compared using the 18 November 2026 snapshot of other authors on current judge compilers. There is no submission-ID or date cutoff. Ties share a place, and times below 0.015 s are compared as 0.015 s. The ranks below concern these new sources; existing sources retain their own historical Accepted metrics.

`1014_greedy_optimized.go`: time place 4/12, memory place 1/12 in this comparable sample.

Earlier PyPy comparison: `1014_greedy_optimized.py`: time place 442/482, memory place 2/482 in this comparable sample.

An asterisk marks a missed rating target: C++ requires top ten or top 15% in both metrics; other families require first place in both. A source can still be admitted under the separate ranking or improvement rule, including at least 30% less time or memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1014_greedy.cpp](1014_greedy.cpp) | G++ 13.2 x64 | greedy | O((log N)^2) | AC | 0.015 s | 192 KB | 11278098 |
| [1014_greedy.go](1014_greedy.go) | Go 1.14 x64 | greedy | O((log N)^2) | AC | 0.031 s | 1096 KB | 11278101 |
| [1014_greedy.java](1014_greedy.java) | Java 1.8 | greedy | O((log N)^2) | AC | 0.125 s | 1604 KB | 11278109 |
| [1014_greedy.py](1014_greedy.py) | Python 3.12 x64 | greedy | O(log N) | AC | 0.093 s | 444 KB | 11278104 |
| [1014_greedy.rs](1014_greedy.rs) | Rust 1.75 x64 | greedy | O(log N) | AC | 0.046 s | 232 KB | 11278114 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1014_greedy_optimized.java](1014_greedy_optimized.java) | Java 1.8 | greedy | O(log N) | AC | 0.109 s | 380 KB | 11303700 |
| [1014_greedy_optimized.go](1014_greedy_optimized.go) \* | Go 1.14 x64 | greedy | O(log(N+2)) | AC | 0.031 s | 780 KB | 11328371 |
| [1014_greedy_optimized.py](1014_greedy_optimized.py) \* | Python 3.12 x64 | greedy | O(log(N+2)) | AC | 0.078 s | 724 KB | 11327014 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
