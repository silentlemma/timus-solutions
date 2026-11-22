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

`1494_bitmask_simulation.py`. Represent the pending stack by ordered nonempty 32-bit packets, not one integer slot per ball. A new maximum inserts exactly the skipped range; older balls must equal the highest set bit in the last packet before removal. Each packet stores its index and mask together, so no N-bit integer is copied per step and empty words need no scan. Under N<=100000, packets fit 44 bits; total work is O(N), with O(ceil(N/32)) packets and a 4096-byte token reader. This deterministic bitmask_simulation algorithm is distinct from the retained explicit-stack versions. The current measurement is PyPy; the previous explicit stack has a separate CPython receipt.

Exact-source PyPy 3.10 x64 Accepted #11327514: 0.14 s / 3764 KB. Saved 2026-11-20 compiler-cohort ranks, time then memory: 20/164; 1/164. Strict admission uses both time and memory at 1024 KB or above: top ten or top 15%, ties share rank and percentage cutoff rounds up. An asterisk remains for the separate first-place-in-both language target. The preserved previous variant has its own paired receipt #11326685 (Python 3.12 x64): 0.14 s / 4160 KB; do not mix measurements or runtimes. All teaching sources remain unchanged.

- `1494_bitmask_simulation.py`: 0.14 s / 3764 KB; retained teaching base `1494_simulation.py` (Python 3.12 x64): 0.14 s / 15568 KB.

`1494_simulation_optimized.py`. Simulate the pocket while reading each observed ball. Push consecutive unseen balls up to it, then require that ball at the stack top; stop at the first contradiction. The stack is a preallocated Python list of N cells, replacing packed unsigned-array accesses. Each ball is pushed and popped at most once, so work is O(N). Input order is not stored separately; space is O(N) plus tokens of the current line. The ordinary readable simulation remains.

Exact-source CPython 3.12 Accepted #11326685: 0.14 s / 4160 KB. Saved current-compiler comparison, 2026-11-20: time rank 20/164, memory rank 1/164. Both required metrics pass the strict top-ten or top-15% rule, with percentage cutoffs rounded up. The asterisk tracks Python's separate first-place target in both metrics.

The previously documented optimized run #11303753 (Python 3.12 x64) recorded 0.171 s / 832 KB. The current CPython 3.12 run has lower recorded time and higher memory. These are separate paired judge measurements; interpreter choice and judge variability are part of the comparison.

- `1494_simulation_optimized.py`: 0.14 s / 4160 KB; retained teaching base `1494_simulation.py` (Python 3.12 x64): 0.14 s / 15568 KB.

The optimized solutions simulate the pocket while they read: for each ball taken out they roll in the balls up to that number, then the top of the pocket must be that ball, and the first mismatch ends the program. So the order of the balls is never stored; the pocket is an array used as a stack. C++ parses the numbers with `getchar` (0.031 s instead of 0.093 s and 512 KB instead of 1540 KB), Go parses them by hand, writes the answer without `fmt` and keeps the pocket in a preallocated array of `int32`, since the ball numbers are at most 100 000 (1312 KB instead of 7684 KB, with the same time), Java reads 4 KB blocks and parses them by hand instead of `StreamTokenizer` (844 KB instead of 1300 KB, with the same time), and Rust parses by hand from a 4 KB buffer (604 KB instead of 2704 KB, with the same time).

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
| [1494_simulation_optimized.py](1494_simulation_optimized.py) \* | Python 3.12 x64 | simulation | O(N) time and space | AC | 0.14 s | 4160 KB | 11326685 |
| [1494_bitmask_simulation.py](1494_bitmask_simulation.py) \* | PyPy 3.10 x64 | bitmask, simulation | O(N) time; O(ceil(N/32)) packets + fixed buffer | AC | 0.14 s | 3764 KB | 11327514 |
| [1494_simulation_optimized.rs](1494_simulation_optimized.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.015 s | 604 KB | 11303754 |

\* Accepted; the separate rating target is not yet met: C++ requires top ten or top 15% in both time and memory, and the other language families require first place in both. This marker is separate from the admission criteria; the version may be optimized further.
