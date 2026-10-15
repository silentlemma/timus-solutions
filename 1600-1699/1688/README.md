# 1688. Team.GOV!

[Timus 1688](https://acm.timus.ru/problem.aspx?space=1&num=1688) · difficulty 133 · implementation

Original problem by Alexander Ipatov, from the Tenth Ural State University Open Personal Contest, February 28, 2009.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three teammates eat alike and one of them pays every bill. Another
member may leave once the money paid for that member, a third of each
bill, exceeds n. Given the bills in order, tell after which visit that
happens.

## Input

n and m (1 ≤ n ≤ 2 · 10⁹; 0 ≤ m ≤ 3000), then m bills, integers from 1
to 2 · 10⁶.

## Output

"Free after x times." for the first such visit x, or "Team.GOV!" if it
never happens.

## Examples

### Example 1

Input:

```
1666 5
2000
1024
900
1156
1200
```

Output:

```
Free after 4 times.
```

### Example 2

Input:

```
3000 5
2000
1024
900
1156
1200
```

Output:

```
Team.GOV!
```

## Solution

Keep the running total of the bills. The share total / 3 exceeds n
exactly when total > 3n, which avoids fractions; stop at the first
visit where that holds. `O(m)`.

Pitfalls:

- 3n reaches 6 · 10⁹ and so can the total: use 64-bit integers
  (test 06);
- a share equal to n is not enough, the comparison is strict (tests 04
  and 06).

The answers match an independent accepted implementation.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1688_implementation.cpp](1688_implementation.cpp) | G++ 13.2 x64 | implementation | O(m) | AC | 0.015 s | 136 KB |
| [1688_implementation.go](1688_implementation.go) | Go 1.14 x64 | implementation | O(m) | AC | 0.015 s | 1124 KB |
| [1688_implementation.java](1688_implementation.java) | Java 1.8 | implementation | O(m) | AC | 0.078 s | 1016 KB |
| [1688_implementation.py](1688_implementation.py) | Python 3.12 x64 | implementation | O(m) | AC | 0.078 s | 788 KB |
| [1688_implementation.rs](1688_implementation.rs) | Rust 1.75 x64 | implementation | O(m) | AC | 0.015 s | 224 KB |
