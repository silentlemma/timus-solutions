# 1263. Elections

[Timus 1263](https://acm.timus.ru/problem.aspx?space=1&num=1263) · difficulty 42 · implementation

Original problem by Den Raskovalov, from the Open Team Programming Contest for Schoolchildren of the Sverdlovsk Region, October 11, 2003.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

N candidates (1 ≤ N ≤ 10 000) and M voters (1 ≤ M ≤ 10 000); each
voter names one candidate. For every candidate, print the share of the
votes as a percentage with two digits after the point and a `%` sign.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N and M, then M candidate numbers from 1 to N.

## Output

N lines with the percentages.

## Examples

### Example 1

Input:

```
3 6
1
2
3
2
1
1
```

Output:

```
50.00%
33.33%
16.67%
```

## Solution

Count the votes of each candidate and print 100 · votes / M with two
decimals. `O(N + M)`.

Pitfalls:

- candidates without votes still get a line, `0.00%` (test 03);
- a share can end exactly in a half of the last printed digit, such as
  1/32 = 3.125% (tests 04, 05). These solutions round such ties to even,
  as `printf` in C does: 3.12%;
- printing one line at a time is slow in some languages for N = 10 000:
  collect the output first.

## Optimized solutions

The optimized Python solution reads the votes line by line through a
generator instead of splitting the whole input at once, and formats the
percentage of each distinct vote count only once: candidates with the
same count share the formatted line. The lines go out one by one through
the buffered `sys.stdout.write` instead of being joined first: 856 KB
instead of 1948 KB, with the same time.

The optimized C++ solution parses the numbers with `getchar` instead of
`scanf` and counts the votes in a fixed array of 16-bit counters: 128 KB
instead of 252 KB, with the same time. The optimized Rust solution
parses the numbers by hand from the bytes of the locked standard input
instead of reading the whole input into a string, counts in 16-bit
counters and writes through a 1 KB buffered writer: 252 KB instead of
468 KB, with the same time.

## Language notes

- C++, Go, Python and Rust format the double directly; all four round
  the exact value of the double half to even.
- Java's `String.format` rounds half up, so Java takes `BigDecimal` of
  the same double and rounds it with `HALF_EVEN`.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1263_implementation.cpp](1263_implementation.cpp) | G++ 13.2 x64 | implementation | O(N + M) | AC | 0.031 s | 252 KB | 11284152 |
| [1263_implementation.go](1263_implementation.go) | Go 1.14 x64 | implementation | O(N + M) | AC | 0.031 s | 1456 KB | 11284153 |
| [1263_implementation.java](1263_implementation.java) | Java 1.8 | implementation | O(N + M) | AC | 0.156 s | 5696 KB | 11284158 |
| [1263_implementation.py](1263_implementation.py) | Python 3.12 x64 | implementation | O(N + M) | AC | 0.078 s | 1948 KB | 11284154 |
| [1263_implementation.rs](1263_implementation.rs) | Rust 1.75 x64 | implementation | O(N + M) | AC | 0.015 s | 468 KB | 11284161 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1263_implementation_optimized.cpp](1263_implementation_optimized.cpp) \* | G++ 13.2 x64 | implementation | O(N + M) | AC | 0.031 s | 128 KB | 11303730 |
| [1263_implementation_optimized.py](1263_implementation_optimized.py) | Python 3.12 x64 | implementation | O(N + M) | AC | 0.078 s | 856 KB | 11303586 |
| [1263_implementation_optimized.rs](1263_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(N + M) | AC | 0.015 s | 252 KB | 11303731 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
