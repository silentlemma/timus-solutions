# 1263. Elections

[Timus 1263](https://acm.timus.ru/problem.aspx?space=1&num=1263) · difficulty 43 · implementation

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

## Language notes

- C++, Go, Python and Rust format the double directly; all four round
  the exact value of the double half to even.
- Java's `String.format` rounds half up, so Java takes `BigDecimal` of
  the same double and rounds it with `HALF_EVEN`.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1263_implementation.cpp](1263_implementation.cpp) | G++ 13.2 x64 | implementation | O(N + M) | AC | 0.031 s | 252 KB |
| [1263_implementation.go](1263_implementation.go) | Go 1.14 x64 | implementation | O(N + M) | AC | 0.031 s | 1456 KB |
| [1263_implementation.java](1263_implementation.java) | Java 1.8 | implementation | O(N + M) | AC | 0.156 s | 5696 KB |
| [1263_implementation.py](1263_implementation.py) | Python 3.12 x64 | implementation | O(N + M) | AC | 0.078 s | 1948 KB |
| [1263_implementation.rs](1263_implementation.rs) | Rust 1.75 x64 | implementation | O(N + M) | AC | 0.015 s | 468 KB |
