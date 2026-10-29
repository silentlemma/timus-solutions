# 1203. The most talks one person can attend

[Timus 1203](https://acm.timus.ru/problem.aspx?space=1&num=1203) · difficulty 78 · greedy

Original problem by Magaz Asanov, from the Ural State University Team Contest, March 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A conference has `N ≤ 10⁵` interesting talks, each running from minute
`Ts` to minute `Te`, `1 ≤ Ts < Te ≤ 30000`. Two attended talks may not
overlap, and there must be at least one minute between them: after a
talk ending at 15 the next one can start at 16 at the earliest. Find the
largest number of talks one person can attend.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `Ts Te` for each talk.

## Output

The largest number of talks.

## Examples

### Example 1

Input:

```
5
3 4
1 5
6 7
4 5
1 3
```

Output:

```
3
```

## Solution

The classic greedy for interval scheduling: repeatedly take the talk that
ends first among those starting after the last chosen one ended. Any
optimal schedule can swap its first talk for that one without losing
anything, and the same argument repeats.

Times are small, so no sorting is needed: for each minute `e` keep the
latest start among the talks ending at `e`. Sweep the minutes in order;
when the latest start at `e` is after the last chosen end, a talk ending
at `e` can be taken, and it is the earliest ending one available.
`O(N + T)` for `T = 30000`.

Pitfalls:

- a talk starting the very minute the previous one ends is not allowed,
  so the test is a strict "start > last end";
- repeated identical talks count once at most.

The answers were compared with a separately written solution on 300
random inputs and on every test.

## Optimized solutions

The optimized solutions (C++, Rust) parse the numbers by hand straight
from the input buffer instead of `scanf` or reading the whole input into
a string, and keep the latest starts as 16-bit numbers, since all times
are at most 30 000. C++ needs 0.001 s instead of 0.109 s and 164 KB
instead of 304 KB; Rust needs 276 KB instead of 4176 KB, with the same
time.

The optimized Python solution reads the input in 16 KB blocks and parses
it lazily, and keeps the latest starts in an `array` of 16-bit numbers
instead of a list: 980 KB instead of 14476 KB, although the time grows
from 0.109 s to 0.140 s.

## Language notes

No language needs anything special.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1203_greedy.cpp](1203_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + T) | AC | 0.109 s | 304 KB | 11283566 |
| [1203_greedy.go](1203_greedy.go) | Go 1.14 x64 | greedy | O(N + T) | AC | 0.125 s | 4420 KB | 11303282 |
| [1203_greedy.java](1203_greedy.java) | Java 1.8 | greedy | O(N + T) | AC | 0.109 s | 620 KB | 11303457 |
| [1203_greedy.py](1203_greedy.py) | Python 3.12 x64 | greedy | O(N + T) | AC | 0.109 s | 14476 KB | 11283574 |
| [1203_greedy.rs](1203_greedy.rs) | Rust 1.75 x64 | greedy | O(N + T) | AC | 0.015 s | 4176 KB | 11283580 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1203_greedy_optimized.cpp](1203_greedy_optimized.cpp) | G++ 13.2 x64 | greedy | O(N + T) | AC | 0.001 s | 164 KB | 11303579 |
| [1203_greedy_optimized.py](1203_greedy_optimized.py) | Python 3.12 x64 | greedy | O(N + T) | AC | 0.140 s | 980 KB | 11303723 |
| [1203_greedy_optimized.rs](1203_greedy_optimized.rs) | Rust 1.75 x64 | greedy | O(N + T) | AC | 0.031 s | 276 KB | 11303580 |
