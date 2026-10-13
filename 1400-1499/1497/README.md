# 1497. Cutting a Square

[Timus 1497](https://acm.timus.ru/problem.aspx?space=1&num=1497) · difficulty 304 · implementation

Original problem by Alexander Toropov, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An N × N sheet of squares (3 ≤ N ≤ 1000) is cut into a black piece
(cells 1) and a white piece (cells 0), both connected through sides.
The pieces lie together on a table. Can one of them be moved far away
from the other without lifting either off the table? Print "Yes" or
"No".

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then N rows of N characters 0 and 1.

## Output

"Yes" or "No".

## Examples

### Example 1

Input:

```
5
10001
10001
10001
11111
11111
```

Output:

```
Yes
```

### Example 2

Input:

```
5
11011
11011
10001
11111
11111
```

Output:

```
No
```

## Solution

Moving one piece away is the same as moving the other the opposite way,
so only the black piece needs to move. It can slide straight up when no
column has a white cell above a black one, and likewise for down, left
and right. A diagonal slide needs nothing more: every edge between the
pieces must face away from the motion, and then both axis slides that
make up the diagonal are free as well. So it is enough to check the four
directions, one pass over the sheet for each. `O(N²)`.

Pitfalls:

- a piece enclosed by the other can never leave (test 03, gen2);
- a single hook, even one cell long, locks the pieces (tests 05, 07,
  gen4);
- a staircase cut slides apart along an axis, though its edges point
  two ways (test 04, gen1).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1497_implementation.cpp](1497_implementation.cpp) | G++ 13.2 x64 | implementation | O(N^2) | AC | 0.031 s | 868 KB |
| [1497_implementation.go](1497_implementation.go) | Go 1.14 x64 | implementation | O(N^2) | AC | 0.046 s | 2192 KB |
| [1497_implementation.java](1497_implementation.java) | Java 1.8 | implementation | O(N^2) | AC | 0.109 s | 2952 KB |
| [1497_implementation.py](1497_implementation.py) | Python 3.12 x64 | implementation | O(N^2) | AC | 0.109 s | 4276 KB |
| [1497_implementation.rs](1497_implementation.rs) | Rust 1.75 x64 | implementation | O(N^2) | AC | 0.031 s | 2116 KB |
