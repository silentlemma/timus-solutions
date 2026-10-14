# 1552. Brainfuck

[Timus 1552](https://acm.timus.ru/problem.aspx?space=1&num=1552) · difficulty 1156 · dp

Original problem from the Novosibirsk SU Contest at the Petrozavodsk Training Camp, September 2007.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A brainfuck machine with only the commands > < + − . has 30000 byte
cells, all 0, and a pointer at the leftmost one; the pointer and the
bytes wrap around. Write a shortest program that prints a given string
of at most 50 lowercase letters. An optimal program never needs more
than four cells.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

The string.

## Output

A shortest program, on one line. Any one is accepted.

## Examples

### Example 1

Input:

```
a
```

Output:

```
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.
```

## Solution

Only the cells the program uses matter, and squeezing out unused cells
between them, or moving them next to the start cell, only shortens the
walks, so they form a block of four neighbouring cells with the start
cell somewhere inside it; walking left of cell 0 is fine thanks to the
wrap-around. A cell that is changed without being printed could just as
well be changed later, so every cell holds 0 or the last letter printed
from it.

Print the letters one by one. After a letter, the state is the cell
under the pointer (holding that letter) and the values of the other
three cells, 0 or a letter: 4·27³ ≈ 79000 states. To print the next
letter from cell q costs the walk |p − q|, the change of the value
(from 0 up to a letter takes its code, between letters their
difference, never cheaper by wrapping around 256) and the dot. The DP
keeps the cheapest way to each state and the state it came from, so the
program is rebuilt by walking back. `O(n·4·27³·4)` steps.

Pitfalls:

- the sample program is shown over several lines, but the answer is a
  single line;
- a fresh cell starts at 0, 97 steps below a, while a used one may be
  much closer (tests 03, 04);
- far-apart letters mixed together spread over three cells, one of
  them left of the start, reached by wrapping around (test 08);
- Python runs under PyPy: the 50-letter tests take about 3.2 s with
  CPython and about 0.2 s with PyPy.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1552_dp.cpp](1552_dp.cpp) | G++ 13.2 x64 | dp | O(n * 4 * 27^3 * 4) | AC | 0.046 s | 16232 KB |
| [1552_dp.go](1552_dp.go) | Go 1.14 x64 | dp | O(n * 4 * 27^3 * 4) | AC | 0.062 s | 30712 KB |
| [1552_dp.java](1552_dp.java) | Java 1.8 | dp | O(n * 4 * 27^3 * 4) | AC | 0.140 s | 27348 KB |
| [1552_dp.py](1552_dp.py) | PyPy 3.10 x64 | dp | O(n * 4 * 27^3 * 4) | AC | 0.390 s | 22812 KB |
| [1552_dp.rs](1552_dp.rs) | Rust 1.75 x64 | dp | O(n * 4 * 27^3 * 4) | AC | 0.078 s | 16100 KB |
