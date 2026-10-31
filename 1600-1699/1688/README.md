# 1688. Team.GOV!

[Timus 1688](https://acm.timus.ru/problem.aspx?space=1&num=1688) · difficulty 134 · implementation

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

## Optimized solutions

The optimized Java solution parses the numbers byte by byte from a 4 KB
buffer that it refills from `System.in`, instead of first copying the
whole input into a `StringBuilder` and then into one more string for the
tokenizer. It reads all m bills even after the answer is known, and
keeps the total and 3n in `long`, since both can reach 6 · 10⁹:
{1688_implementation_optimized.java}.

The optimized Python solution takes the tokens line by line from a
generator over `sys.stdin.buffer` instead of reading the whole input and
turning it into a list of up to 3002 integers; the running total is
kept as in the simple solution: {1688_implementation_optimized.py}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `1688_implementation_optimized.java`: time reduction -60.26%; memory
  reduction +62.20%; base: `1688_implementation.java`.

- `1688_implementation_optimized.py`: time reduction +0.00%; memory
  reduction +44.67%; base: `1688_implementation.py`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [1688_implementation.cpp](1688_implementation.cpp).
- [1688_implementation.go](1688_implementation.go).
- [1688_implementation.rs](1688_implementation.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1688_implementation.cpp](1688_implementation.cpp) | G++ 13.2 x64 | implementation | O(m) | AC | 0.015 s | 128 KB | 11304065 |
| [1688_implementation.go](1688_implementation.go) | Go 1.14 x64 | implementation | O(m) | AC | 0.015 s | 1124 KB | 11288883 |
| [1688_implementation.java](1688_implementation.java) | Java 1.8 | implementation | O(m) | AC | 0.078 s | 1016 KB | 11288886 |
| [1688_implementation.py](1688_implementation.py) | Python 3.12 x64 | implementation | O(m) | AC | 0.078 s | 788 KB | 11288885 |
| [1688_implementation.rs](1688_implementation.rs) | Rust 1.75 x64 | implementation | O(m) | AC | 0.015 s | 232 KB | 11304066 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1688_implementation_optimized.java](1688_implementation_optimized.java) | Java 1.8 | implementation | O(m) | AC | 0.125 s | 384 KB | 11304439 |
| [1688_implementation_optimized.py](1688_implementation_optimized.py) \* | Python 3.12 x64 | implementation | O(m) | AC | 0.078 s | 436 KB | 11304440 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
