# 1636. Penalty Time

[Timus 1636](https://acm.timus.ru/problem.aspx?space=1&num=1636) · difficulty 61 · implementation

Original problem by Alex Samsonov, from the Thirteenth Ural State University Open Team Programming Championship.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Teams QXX and ZZZ solved all ten problems; QXX won with penalty time T1
against T2 of ZZZ. Each rejected attempt adds 20 minutes. Given how many
rejected attempts ZZZ made on each problem, decide whether ZZZ would have
won without them. On equal time the teams are ordered by name, so ZZZ
would still be second.

## Input

T1 and T2 (250 ≤ T1 ≤ T2 ≤ 2400) on the first line, then ten counts of
rejected attempts of ZZZ.

## Output

`Dirty debug :(` if the attempts cost ZZZ the first place, otherwise
`No chance.`.

## Examples

### Example 1

Input:

```
290 420
0 0 0 2 1 0 2 0 1 0
```

Output:

```
No chance.
```

### Example 2

Input:

```
300 719
0 0 0 0 0 0 21 0 0 0
```

Output:

```
Dirty debug :(
```

## Solution

Subtract 20 minutes per rejected attempt from T2. ZZZ would have won
only with strictly less time than T1, since a tie goes to QXX by the
alphabet. `O(1)`.

Pitfalls:

- equal clean time is still a loss (test 03), one minute less is a win
  (test 04);
- the answers end in a period and in a sad face, both part of the
  expected text.

The answers match an independent accepted implementation on 100 random
tests.

## Optimized solutions

The optimized Java solution parses the numbers byte by byte from
`System.in` instead of using `Scanner`: 368 KB instead of 1600 KB, with
the same time.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1636_implementation.cpp](1636_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 116 KB | 11303772 |
| [1636_implementation.go](1636_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1064 KB | 11288447 |
| [1636_implementation.java](1636_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.109 s | 1600 KB | 11288449 |
| [1636_implementation.py](1636_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.078 s | 428 KB | 11288448 |
| [1636_implementation.rs](1636_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.015 s | 244 KB | 11303773 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1636_implementation_optimized.java](1636_implementation_optimized.java) | Java 1.8 | implementation | O(1) | AC | 0.093 s | 368 KB | 11303765 |
