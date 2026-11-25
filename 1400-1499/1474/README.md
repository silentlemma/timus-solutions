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
- At N = 499 the program prints 249 999 move indices. Use buffered output
  (gen4).

## Optimized solutions

The optimized versions compute the next hole position directly. The slide comes last in a growing run and first in a shrinking run. The middle run consists only of jumps. Reusing the decimal representations of positions reduces output overhead.

G++ 13.2 x64, submission 11320508. Time 0.031 → 0.015 s, memory 1524 → 224 KB.

Go 1.14 x64, submission 11320528. Time 0.046 → 0.046 s, memory 10276 → 1152 KB.

Java 1.8, submission 11320556. Time 0.14 → 0.109 s, memory 8416 → 772 KB.

Python 3.12 x64, submission 11320580. Time 0.25 → 0.109 s, memory 23792 → 2044 KB.

Rust 1.75 x64, submission 11320607. Time 0.031 → 0.015 s, memory 14900 → 248 KB.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322266 · Go 1.14 x64 №11322267 · Java 1.8 №11322268 · Python 3.12 x64 №11322269 · Rust 1.75 x64 №11322270.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1474_constructive.cpp](1474_constructive.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.031 s | 1524 KB | 11322266 |
| [1474_constructive.go](1474_constructive.go) | Go 1.14 x64 | constructive | O(N^2) | AC | 0.046 s | 10276 KB | 11322267 |
| [1474_constructive.java](1474_constructive.java) | Java 1.8 | constructive | O(N^2) | AC | 0.14 s | 8416 KB | 11322268 |
| [1474_constructive.py](1474_constructive.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.25 s | 23792 KB | 11322269 |
| [1474_constructive.rs](1474_constructive.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.031 s | 14900 KB | 11322270 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1474_constructive_optimized.cpp](1474_constructive_optimized.cpp) | G++ 13.2 x64 | constructive | O(N^2) | AC | 0.015 s | 224 KB | 11320508 |
| [1474_constructive_optimized.go](1474_constructive_optimized.go) \* | Go 1.14 x64 | constructive | O(N^2) | AC | 0.046 s | 1152 KB | 11320528 |
| [1474_constructive_optimized.java](1474_constructive_optimized.java) | Java 1.8 | constructive | O(N^2) | AC | 0.109 s | 772 KB | 11320556 |
| [1474_constructive_optimized.py](1474_constructive_optimized.py) | Python 3.12 x64 | constructive | O(N^2) | AC | 0.109 s | 2044 KB | 11320580 |
| [1474_constructive_optimized.rs](1474_constructive_optimized.rs) | Rust 1.75 x64 | constructive | O(N^2) | AC | 0.015 s | 248 KB | 11320607 |

\* The marked versions have room to improve in the ratings.
