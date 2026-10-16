# 1790. Searching for the Truth

[Timus 1790](https://acm.timus.ru/problem.aspx?space=1&num=1790) · difficulty 1336 · simulation

Original problem by Mikhail Rubinchik, from the Ural Regional Team Programming Contest 2010.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

An artifact stands on one of n pedestals in a row. Each turn one
pedestal is touched: if the artifact is there it is found, otherwise it
moves to a neighbouring pedestal of its choice. Given a sequence of m
touches, decide whether it always finds the artifact, whatever its
start and its moves.

## Input

n and m (2 ≤ n, m ≤ 100000), then m pedestal numbers from 1 to n.

## Output

"YES" if the sequence always finds the artifact, otherwise "NO".

## Examples

### Example 1

Input:

```
3 2
2 2
```

Output:

```
YES
```

### Example 2

Input:

```
3 3
1 2 3
```

Output:

```
NO
```

## Solution

Follow the set of pedestals where the artifact may still be. Every
move flips the parity of its pedestal, so the set splits into an even
part and an odd part, and each part is always a run lo, lo + 2, …, hi
of one parity with no gaps. A touch at an end of a run shrinks it by
one place. A touch inside a run leaves a hole, but after the move both
neighbours of the hole are reached from the places two steps away, so
nothing changes. A move turns the run lo…hi into lo − 1…hi + 1 of the
other parity, except that a run touching the wall at 1 or n is pushed
inwards: 1 becomes 2 and n becomes n − 1. The answer is YES when both
runs are empty at the end. `O(m)`.

In the second example an artifact that starts on 2 slips through: touch
1 misses, it goes to 3; touch 2 misses, it comes back to 2; touch 3
misses again.

Pitfalls:

- a set of up to 100000 pedestals over 100000 turns is too slow to
  follow place by place, hence the two runs;
- a touch strictly inside a run is wasted, not a hole that stays;
- at a wall the run does not grow beyond it but steps back inwards.

The answers agree with a direct simulation of the whole set on 400
random short sequences on a few pedestals, and with an independent
accepted implementation on long sweeps, broken sweeps and random
sequences.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1790_simulation.cpp](1790_simulation.cpp) | G++ 13.2 x64 | simulation | O(m) | AC | 0.062 s | 128 KB |
| [1790_simulation.go](1790_simulation.go) | Go 1.14 x64 | simulation | O(m) | AC | 0.031 s | 1544 KB |
| [1790_simulation.java](1790_simulation.java) | Java 1.8 | simulation | O(m) | AC | 0.125 s | 4592 KB |
| [1790_simulation.py](1790_simulation.py) | Python 3.12 x64 | simulation | O(m) | AC | 0.140 s | 7036 KB |
| [1790_simulation.rs](1790_simulation.rs) | Rust 1.75 x64 | simulation | O(m) | AC | 0.031 s | 2128 KB |
