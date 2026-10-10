# 1203. The most talks one person can attend

[Timus 1203](https://acm.timus.ru/problem.aspx?space=1&num=1203) · difficulty 79 · greedy

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

## Language notes

- Go and Java read the input with hand-written byte readers.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1203_greedy.cpp](1203_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + T) | AC | 0.109 s | 304 KB |
| [1203_greedy.go](1203_greedy.go) | Go 1.14 x64 | greedy | O(N + T) | AC | 0.031 s | 1344 KB |
| [1203_greedy.java](1203_greedy.java) | Java 1.8 | greedy | O(N + T) | AC | 0.109 s | 704 KB |
| [1203_greedy.py](1203_greedy.py) | Python 3.12 x64 | greedy | O(N + T) | AC | 0.109 s | 14476 KB |
| [1203_greedy.rs](1203_greedy.rs) | Rust 1.75 x64 | greedy | O(N + T) | AC | 0.015 s | 4176 KB |
