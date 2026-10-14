# 1539. Intelligence Data

[Timus 1539](https://acm.timus.ru/problem.aspx?space=1&num=1539) · difficulty 1052 · number_theory

Original problem by Stanislav Vasiliev, from the Eighth Ural State University Open Personal Contest, March 3, 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A report gives N averages (1 ≤ N ≤ 100) over the same group of goblins,
each a positive number up to 1000 rounded to exactly d decimal places
(1 ≤ d ≤ 5). Find the smallest possible size of the group.

Time limit: 1 second. Memory limit: 64 MB.

## Input

d and N, then the N averages, one per line.

## Output

The smallest group size.

## Examples

### Example 1

Input:

```
2 3
52.29
0.71
170.86
```

Output:

```
7
```

## Solution

Work in units of 10^−d: an average written as v units comes from a
total of p items over q goblins when p / q rounds to v, that is when
v − 1/2 ≤ 10^d·p / q < v + 1/2, or (2v − 1)·q ≤ 2·10^d·p < (2v + 1)·q
(rounding half up). For a given q this asks whether a half-open
interval contains an integer: take the smallest p allowed by the left
end and check the right end, all in integers.

Only the fractional part of each average matters, since a whole number
of items per goblin can be added to every total, and a whole average
fits any group; duplicates can go too. For q = 10^d the interval is at
least 1 long, so the answer is at most 10^d = 10⁵: try q = 1, 2, … and
stop at the first one that fits every average. An average that rules
out one q tends to rule out the next ones, so it moves to the front of
the list. `O(10^d·N)` at worst.

Pitfalls:

- rounding is half up: 1/4 = 0.25 is written 0.3, so four goblins
  explain both 0.3 and 0.8 (test 05);
- 0.00001 alone already needs 66667 goblins (test 04);
- integer parts change nothing: in test 08, 999.99999 counts like
  0.99999, which needs at least 66667 goblins just as 0.00001 does, and
  the half makes the group even, 66668;
- floating point is not exact enough near the ends of the intervals, so
  the averages are read as integers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1539_number_theory.cpp](1539_number_theory.cpp) | G++ 13.2 x64 | number_theory | O(10^d * N) | AC | 0.015 s | 400 KB |
| [1539_number_theory.go](1539_number_theory.go) | Go 1.14 x64 | number_theory | O(10^d * N) | AC | 0.046 s | 1140 KB |
| [1539_number_theory.java](1539_number_theory.java) | Java 1.8 | number_theory | O(10^d * N) | AC | 0.109 s | 644 KB |
| [1539_number_theory.py](1539_number_theory.py) | Python 3.12 x64 | number_theory | O(10^d * N) | AC | 0.250 s | 516 KB |
| [1539_number_theory.rs](1539_number_theory.rs) | Rust 1.75 x64 | number_theory | O(10^d * N) | AC | 0.015 s | 228 KB |
