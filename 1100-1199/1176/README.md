# 1176. Laying every missing one-way channel in one round trip

[Timus 1176](https://acm.timus.ru/problem.aspx?space=1&num=1176) · difficulty 335 · graphs

Original problem by Pavel Atnashev, from the Third USU Personal Programming Contest, Ekaterinburg, February 16, 2002.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

`N ≤ 1000` planets have some one-way channels, given as an adjacency
matrix. Every ordered pair of different planets must get a channel. A
builder starts at planet `A`, can only move by laying a new channel, must
lay exactly the missing ones and must return to `A`. At most 32,000
channels are missing, and a solution is guaranteed. Print the channels in
the order they are laid.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N` and `A`, then the `N×N` matrix.

## Output

The laid channels, one `from to` pair per line.

## Checking

Any order is accepted if it is a walk from `A` back to `A` that uses
every missing channel exactly once and nothing else.

## Examples

### Example 1

Input:

```
4 2
0 0 1 0
0 0 1 0
1 1 0 1
0 0 1 0
```

Output:

```
2 4
4 1
1 2
2 1
1 4
4 2
```

## Solution

The builder's route is a closed walk through all missing channels, each
once: an Euler circuit of the graph of missing channels. A solution is
promised, so every planet has as many missing channels out as in, and
the ones with any are reachable from `A`.

Hierholzer's algorithm builds the circuit with an explicit stack. Keep
walking along unused channels from the planet on top of the stack. When a
planet has none left, pop it onto the answer. Popped planets come out in
reverse order of the circuit, with every side loop spliced in where it
was found. `O(N² + M)`, where reading the matrix dominates.

Pitfalls:

- the matrix has a million numbers, so the input should be read in bulk;
- the diagonal is not a missing channel;
- if nothing is missing, the answer is empty;
- a recursive walk could go 32,000 levels deep, hence the explicit stack.

Every printed route was checked against the missing channels on 100
random small empires and on generated ones with a thousand planets and
32,000 missing channels.

## Language notes

- C++ and Rust read the matrix with their usual parsers, Go with a
  word scanner, Java with a hand-written byte reader, and Python by
  splitting the whole input once.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1176_graphs.cpp](1176_graphs.cpp) | G++ 13.2 x64 | graphs | O(N² + M) | AC | 0.531 s | 368 KB |
| [1176_graphs.go](1176_graphs.go) | Go 1.14 x64 | graphs | O(N² + M) | AC | 0.062 s | 5968 KB |
| [1176_graphs.java](1176_graphs.java) | Java 1.8 | graphs | O(N² + M) | AC | 0.156 s | 2608 KB |
| [1176_graphs.py](1176_graphs.py) | Python 3.12 x64 | graphs | O(N² + M) | AC | 0.203 s | 18940 KB |
| [1176_graphs.rs](1176_graphs.rs) | Rust 1.75 x64 | graphs | O(N² + M) | AC | 0.031 s | 3560 KB |
