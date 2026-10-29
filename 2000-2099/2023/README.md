# 2023. Walking between three destinations

[Timus 2023](https://acm.timus.ru/problem.aspx?space=1&num=2023) · difficulty 40 · implementation

Original problem by Alex Samsonov, from the NEERC 2014 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Three destinations occupy consecutive positions 0, 1 and 2 on a line.
Each recipient label belongs to exactly one destination according to
this complete table:

| Position | Recipient labels |
| --- | --- |
| 0 | Alice, Ariel, Aurora, Phil, Peter, Olaf, Phoebus, Ralph, Robin |
| 1 | Bambi, Belle, Bolt, Mulan, Mowgli, Mickey, Silver, Simba, Stitch |
| 2 | Dumbo, Genie, Jiminy, Kuzko, Kida, Kenai, Tarzan, Tiana, Winnie |

Process a sequence of `n` labels in its given order, starting at
position 0. Moving to an adjacent position costs one step; processing a
label at its destination costs nothing. Find the total steps needed. The
route ends at the final destination: there is no required return to
position 0. Labels may repeat. Limits: `1 ≤ n ≤ 1000`, 1 second, 64 MB.

## Input

The first line contains `n`. Each of the following `n` lines contains
one label from the table, with exactly the displayed spelling and
capitalization. The line order is the processing order. All labels
contain only letters and have length at most seven.

## Output

Print one integer: the total number of steps, between 0 and `2n` inclusive.

## Checking

Outputs are compared token by token.

## Examples

```
4
Aurora
Tiana
Ariel
Mulan
```

```
5
```

## Solution

Look up the position of every label in the table and walk there: going
from position p to position q takes |p − q| steps. Add up these
distances, starting at position 0. `O(n)`.

In the example the positions are 0 → 0 → 2 → 0 → 1, and the steps are
0 + 2 + 2 + 1 = 5.

Pitfalls:

- the walk starts at position 0 before the first label;
- there is no walk back after the last label.

## Optimized solutions

The optimized solutions (C++, Java) read the input byte by byte and
store no names. A label's only capital letter is its first one, and the
first letters tell the positions apart: A, P, O and R stand for
position 0, B, M and S for position 1, all the others for position 2.
The digits of `n` contain no capital letters, so every capital letter in
the input starts the next label. C++: 100 KB instead of 400 KB, with the
same time; Java: 0.078 s instead of 0.140 s and 344 KB instead of
1964 KB.

The optimized Rust solution scans the input byte by byte for capitals,
as the C++ and Java ones do, instead of reading the names and looking
them up in a table: 232 KB instead of 424 KB, with the same time.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2023_implementation.cpp](2023_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 400 KB | 11303356 |
| [2023_implementation.go](2023_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1156 KB | 11303357 |
| [2023_implementation.java](2023_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.140 s | 1964 KB | 11303358 |
| [2023_implementation.py](2023_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 400 KB | 11303359 |
| [2023_implementation.rs](2023_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 424 KB | 11303360 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [2023_implementation_optimized.cpp](2023_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 100 KB | 11303660 |
| [2023_implementation_optimized.java](2023_implementation_optimized.java) | Java 1.8 | implementation | O(n) | AC | 0.078 s | 344 KB | 11303663 |
| [2023_implementation_optimized.rs](2023_implementation_optimized.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.031 s | 232 KB | 11303793 |
