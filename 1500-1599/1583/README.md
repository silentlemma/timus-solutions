# 1583. Cheese

[Timus 1583](https://acm.timus.ru/problem.aspx?space=1&num=1583) · difficulty 1814 · binary_search

Original problem by Alexander Mironenko, prepared by Denis Musin, from the ACM ICPC 2007–2008 NEERC Eastern Subregional Contest, Yekaterinburg, October 27, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A bar of cheese 10 × 100 × 10 cm weighs one gram per cubic centimetre
and holds up to 100 spherical holes that touch neither each other nor
the sides. A machine cuts it across, one piece of 500 grams after
another: from the last cut it finds the mark where the next piece
reaches 500 grams, rounds it to whole micrometres and cuts there. It
stops when less than 500 grams are left, and never cuts at exactly one
metre. Print the cuts in micrometres.

Time limit: 1 second. Memory limit: 64 MB.

## Input

The first line contains n (0 ≤ n ≤ 100), the number of holes. The next
n lines give each hole as its centre x, y, z and its radius, in
centimetres. Coordinates are measured from a corner of the bar; y runs
along the bar.

## Output

The first line contains the number of cuts, followed by one cut per
line in micrometres from the start of the bar.

## Examples

### Example 1

Input:

```
2
3.2 37.2 1.8 1
4.2 66.6 5.5 2.5
```

Output:

```
19
50000
100000
150000
200000
250000
300000
350000
400419
450419
500419
550419
600419
651114
706964
756964
806964
856964
906964
956964
```

## Solution

The weight of the bar up to a mark y is 100·y minus, for every hole,
the part of the sphere below the mark: a spherical cap of height h
(between 0 and 2r) with volume π·h²·(3r − h)/3. This weight grows with
y, since every cross-section keeps some cheese, so the mark where the
next piece reaches 500 grams is found by bisection, 100 halvings from
the last cut to the end of the bar. The mark is rounded to the
micrometre grid and the next piece starts at that rounded cut, as the
machine does. At most 20 pieces, each search O(100·n). The results
were checked against an independent program on 60 random bars.

Pitfalls:

- each piece is measured from the cut actually made, after rounding,
  not from the exact mark; using the exact mark changes later cuts
  (test 10);
- without holes the twentieth cut would fall at exactly one metre and
  is not made (test 02);
- coordinates are in centimetres and cuts in micrometres: one
  centimetre is 10000 µm.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1583_binary_search.cpp](1583_binary_search.cpp) | G++ 13.2 x64 | binary_search | O(n) | AC | 0.015 s | 216 KB |
| [1583_binary_search.go](1583_binary_search.go) | Go 1.14 x64 | binary_search | O(n) | AC | 0.031 s | 1120 KB |
| [1583_binary_search.java](1583_binary_search.java) | Java 1.8 | binary_search | O(n) | AC | 0.140 s | 2956 KB |
| [1583_binary_search.py](1583_binary_search.py) | Python 3.12 x64 | binary_search | O(n) | AC | 0.187 s | 556 KB |
| [1583_binary_search.rs](1583_binary_search.rs) | Rust 1.75 x64 | binary_search | O(n) | AC | 0.031 s | 280 KB |
