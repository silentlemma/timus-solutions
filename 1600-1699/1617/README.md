# 1617. Flat Spots

[Timus 1617](https://acm.timus.ru/problem.aspx?space=1&num=1617) · difficulty 65 · implementation

Original problem by Vladimir Yakovlev, from the Twelfth Ural Championship in Sports Programming, March 29, 2008.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A depot has n wheel pairs (1 ≤ n ≤ 150), each of an integer diameter
from 600 to 700 mm. A tram car needs four wheel pairs of the same
diameter. How many cars can be equipped?

Time limit: 0.5 seconds. Memory limit: 64 MB.

## Input

n, then the n diameters.

## Output

The number of cars.

## Examples

### Example 1

Input:

```
9
689
690
690
689
689
690
689
688
688
```

Output:

```
1
```

## Solution

Count the pairs of each diameter. A diameter with c pairs equips ⌊c / 4⌋
cars, and the diameters do not interact, so the answer is the sum over
all diameters. `O(n)`.

Pitfalls:

- leftover pairs of different diameters cannot be combined (test 01);
- eight pairs of one size equip two cars, not one (test 03).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1617_implementation.cpp](1617_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 128 KB |
| [1617_implementation.go](1617_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1092 KB |
| [1617_implementation.java](1617_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1680 KB |
| [1617_implementation.py](1617_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.093 s | 368 KB |
| [1617_implementation.rs](1617_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.015 s | 244 KB |
