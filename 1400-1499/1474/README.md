# 1474. About Frogs

[Timus 1474](https://acm.timus.ru/problem.aspx?space=1&num=1474) · difficulty 725 · constructive

Original problem by Alexander Ipatov, from the contest of the Ural State University and Orel State Technical University at the Petrozavodsk Summer Training Camp, August 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Hummocks 0 … 2N (1 ≤ N ≤ 499) hold N white frogs on 0 … N − 1, an empty
hummock N and N black frogs on N + 1 … 2N. A white frog moves right
onto the empty neighbour or jumps right over one black frog onto the
empty hummock; a black frog does the same to the left. Moves come in
any order. Swap the colours within a million moves, printing the number
of moves and the hummock each move starts from, or −1 if it is
impossible.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N.

## Output

K, then the K starting hummocks. Any correct sequence is accepted.

## Examples

### Example 1

Input:

```
1
```

Output:

```
3
2 0 1
```

## Solution

Frogs only move forward, so every white frog passes every black frog
exactly once, and only a jump passes a frog: N² jumps. All frogs
together travel 2N(N + 1) hummocks, two per jump and one per slide, so
there are 2N slides. Every successful game therefore takes N² + 2N
moves, 249 999 for N = 499, and the answer is never −1; the only danger
is a dead end, where two frogs of one colour block each other.

The moves go in runs of 1, 2, …, N, then N once more, then N, …, 1,
the black and white frogs taking turns, black first. Within a run,
jump into the hole when possible and slide otherwise. This pattern
avoids dead ends, so a move is always available; replaying it
confirms the swap for every N from 1 to 499. `O(N²)`.

Pitfalls:

- the order matters: moving greedily without the run pattern can strand
  two frogs of one colour behind each other (02, the checker
  replays every move);
- −1 is never the answer (all tests);
- N = 499 prints 249 999 move indices, which should be built in one
  buffer (gen4).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1474_constructive.cpp](1474_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.031 s | 1536 KB |
| [1474_constructive.go](1474_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.031 s | 11672 KB |
| [1474_constructive.java](1474_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.125 s | 8428 KB |
| [1474_constructive.py](1474_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.234 s | 24648 KB |
| [1474_constructive.rs](1474_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.062 s | 14840 KB |
