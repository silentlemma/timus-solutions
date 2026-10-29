# 1510. Order

[Timus 1510](https://acm.timus.ru/problem.aspx?space=1&num=1510) · difficulty 87 · greedy

Original problem by Den Raskovalov, from the Yekaterinburg quarterfinal of the 31st ACM ICPC, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are N banknotes (1 ≤ N ≤ 500000) with values from 0 to 10⁹, and
more than half of them have the same value. Print that value.

Time limit: 1 second. Memory limit: 16 MB.

## Input

N, then the N values, one per line.

## Output

The value of the majority.

## Examples

### Example 1

Input:

```
5
3
3
2
2
3
```

Output:

```
3
```

## Solution

Boyer–Moore voting: keep a candidate and a counter. A note equal to the
candidate raises the counter, any other lowers it, and when the counter
is zero the next note becomes the candidate. Each decrease cancels one
note of the candidate against one other note; the majority has more
notes than all the others together, so it cannot be cancelled out and
is the candidate at the end. `O(N)` time and `O(1)` memory.

Pitfalls:

- 16 MB is tight: in Python, reading the whole input at once and
  splitting it can take about 29 MB, so every solution reads the notes
  one at a time;
- the majority can come after all the other notes (test 03, gen2) or
  alternate with them (test 04);
- the majority value can be 0 (test 05).

## Optimized solutions

The optimized solutions (C++, Java) parse the up to 500 000 numbers by
hand from 16 KB blocks instead of `scanf` and `StreamTokenizer`, and
keep the values in `int`, which holds `10⁹`. C++ takes 0.031 s instead
of 0.437 s and 104 KB instead of 136 KB; Java 0.140 s instead of
0.265 s, although its memory grows from 488 KB to 584 KB. The vote is
the same.

The optimized Python solution relies on one value per line and converts
each of the `n` lines as it is, with no splitting into tokens: 0.203 s
instead of 0.375 s, with the same memory.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1510_greedy.cpp](1510_greedy.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.437 s | 136 KB | 11287306 |
| [1510_greedy.go](1510_greedy.go) | Go 1.14 x64 | greedy | O(N) | AC | 0.093 s | 6024 KB | 11287307 |
| [1510_greedy.java](1510_greedy.java) | Java 1.8 | greedy | O(N) | AC | 0.265 s | 488 KB | 11287309 |
| [1510_greedy.py](1510_greedy.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.375 s | 444 KB | 11287308 |
| [1510_greedy.rs](1510_greedy.rs) | Rust 1.75 x64 | greedy | O(N) | AC | 0.109 s | 232 KB | 11287310 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1510_greedy_optimized.cpp](1510_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N) | AC | 0.031 s | 104 KB | 11303963 |
| [1510_greedy_optimized.java](1510_greedy_optimized.java) | Java 1.8 | greedy | O(N) | AC | 0.140 s | 584 KB | 11303964 |
| [1510_greedy_optimized.py](1510_greedy_optimized.py) | Python 3.12 x64 | greedy | O(N) | AC | 0.203 s | 432 KB | 11303965 |
