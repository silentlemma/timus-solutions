# 1468. Fraction

[Timus 1468](https://acm.timus.ru/problem.aspx?space=1&num=1468) · difficulty 836 · math

Original problem by Dmitry Zhukov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

For up to 100 tests a, b, k (1 ≤ a, b ≤ 10000, 2 ≤ k ≤ 36), write a / b
in base k with digits 0–9 and A–Z: the whole part, then, if the number is
not whole, a point and the fractional digits, with the repeating part in
brackets. No needless zeros may appear. The input ends with "0 0".

Time limit: 0.4 seconds. Memory limit: 64 MB.

## Input

Lines a b k, then "0 0".

## Output

One line per test.

## Examples

### Example 1

Input:

```
10 5 2
1 2 8
8780 1 29
2794 6083 23
157 7 19
1 12 10
0 0
```

Output:

```
10
0.4
ACM
0.(ACM)
13.(82DAG5)
0.08(3)
```

## Solution

The whole part a div b is written in base k as usual. The fraction is
long division: multiply the remainder by k, the quotient by b is the
next digit and the new remainder is what is left. There are only b possible
remainders, so either one becomes 0 (the fraction ends) or one comes
back. Recording the position at which each remainder first appeared
gives the period exactly: the digits from that position on repeat
forever, and since a remainder decides everything after it, this is the
shortest period, starting as early as possible. `O(b)` per test.

Pitfalls:

- whole results print no point at all (tests 01, 02);
- the period may start after some non-repeating digits, as in 0.08(3)
  (test 01);
- periods can be almost 10000 digits long (test 03, gen2).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1468_math.cpp](1468_math.cpp) | G++ 13.2 x64 | math | O(b) per test | AC | 0.031 s | 380 KB |
| [1468_math.go](1468_math.go) | Go 1.14 x64 | math | O(b) per test | AC | 0.031 s | 6576 KB |
| [1468_math.java](1468_math.java) | Java 1.8 | math | O(b) per test | AC | 0.125 s | 10144 KB |
| [1468_math.py](1468_math.py) | Python 3.12 x64 | math | O(b) per test | AC | 0.343 s | 5672 KB |
| [1468_math.rs](1468_math.rs) | Rust 1.75 x64 | math | O(b) per test | AC | 0.015 s | 1820 KB |
