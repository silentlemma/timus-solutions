# 1494. Monobilliards

[Timus 1494](https://acm.timus.ru/problem.aspx?space=1&num=1494) · difficulty 90 · simulation

Original problem by Alex Samsonov, from the Thirteenth Team Programming Championship for Schoolchildren of the Sverdlovsk Region, October 14, 2006.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Balls 1, 2, …, N (1 ≤ N ≤ 100000) should be rolled into the only pocket
in this order. From time to time an inspector took the last ball that
had rolled in back out of the pocket, and in the end took out every
ball. Given the order in which the inspector took the balls out, print
"Cheater" if the balls cannot have been rolled in the right order, and
"Not a proof" otherwise.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, then the N balls in the order the inspector took them out.

## Output

"Cheater" or "Not a proof".

## Examples

### Example 1

Input:

```
2
2
1
```

Output:

```
Not a proof
```

### Example 2

Input:

```
3
3
1
2
```

Output:

```
Cheater
```

## Solution

The pocket is a stack: balls go in as 1, 2, …, N, and the inspector
always takes the top one. Replay it: roll the balls in order, and after
each one take out balls as long as the top of the pocket is the next
ball in the inspector's list. Waiting can never help, because a ball
that is not on top stays covered until everything above it is gone. If
the whole list is taken out this way, the order was possible. `O(N)`.

Pitfalls:

- a ball buried under a later one cannot come out first: 3, 4, 1, 2 is
  impossible (tests 02, 05);
- taking every ball out only at the end reverses the order, and taking
  each one out at once keeps it; both are possible (gen4, gen5);
- a single swap in a real game is usually enough to make it impossible
  (gen3).

## Optimized solutions

The optimized solutions simulate the pocket while they read: for each
ball taken out they roll in the balls up to that number, then the top of
the pocket must be that ball, and the first mismatch ends the program.
So the order of the balls is never stored; the pocket is an array used
as a stack. C++ parses the numbers with `getchar` (0.031 s instead of
0.093 s and 512 KB instead of 1540 KB), Go parses them by hand, writes
the answer without `fmt` and keeps the pocket in a preallocated array of
`int32`, since the ball numbers are at most 100 000 (1312 KB instead of
7684 KB, with the same time), Java reads 4 KB blocks and parses them by
hand instead of `StreamTokenizer` (844 KB instead of 1300 KB, with the
same time), Python parses line by line and keeps the pocket in an
`array` (832 KB instead of 15568 KB, although the time grows from
0.140 s to 0.171 s), and Rust parses by hand from a 4 KB buffer (604 KB
instead of 2704 KB, with the same time).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1494_simulation.cpp](1494_simulation.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.093 s | 1540 KB | 11287211 |
| [1494_simulation.go](1494_simulation.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.062 s | 7684 KB | 11303301 |
| [1494_simulation.java](1494_simulation.java) | Java 1.8 | simulation | O(N) | AC | 0.109 s | 1300 KB | 11303468 |
| [1494_simulation.py](1494_simulation.py) | Python 3.12 x64 | simulation | O(N) | AC | 0.140 s | 15568 KB | 11287213 |
| [1494_simulation.rs](1494_simulation.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.031 s | 2704 KB | 11287216 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|------------|
| [1494_simulation_optimized.cpp](1494_simulation_optimized.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.031 s | 512 KB | 11303751 |
| [1494_simulation_optimized.go](1494_simulation_optimized.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.046 s | 1312 KB | 11303612 |
| [1494_simulation_optimized.java](1494_simulation_optimized.java) | Java 1.8 | simulation | O(N) | AC | 0.125 s | 844 KB | 11303752 |
| [1494_simulation_optimized.py](1494_simulation_optimized.py) \* | Python 3.12 x64 | simulation | O(N) | AC | 0.171 s | 832 KB | 11303753 |
| [1494_simulation_optimized.rs](1494_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.015 s | 604 KB | 11303754 |

\* Not in the top 10 or the top 15% of the solutions in its language on
the current judge; it may be optimized further.
