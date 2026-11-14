# 1424. Minibus

[Timus 1424](https://acm.timus.ru/problem.aspx?space=1&num=1424) · difficulty 697 · greedy

Original problem by Dmitry Kovalioff, Ilya Grebnov and Nikita Rybak (idea by Sergey Sofronov), from Timus Top Coders: First Challenge.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A minibus with M seats (M ≤ 1000) drives once from stop 1 to stop N
(N ≤ 100 000). K people (K ≤ 50 000) want to ride, person i from stop
S[i] to stop F[i], each paying P whatever the distance. The driver may
refuse anyone. Print the largest profit and the numbers of the people
to take, in any order; any best set will do.

Time limit: 1 second. Memory limit: 64 MB.

## Input

N, M, K and P, then K lines S F.

## Output

The profit, then the people to take.

## Examples

### Example 1

Input:

```
6 2 6 9
1 4
2 6
1 5
2 3
4 6
3 6
```

Output:

```
36
1 5 6 4
```

## Solution

Every passenger pays the same, so the task is to take as many people as
possible with at most M on board at once; a seat left at a stop can be
taken at that same stop. Go through the stops in order. At each stop
the people whose trips end there leave, everybody waiting there gets
on, and while more than M are on board the one going farthest is
refused, as if never taken.

Refusing the farthest rider is safe: among the people on board after a
stop, any best plan must leave out at least as many of them as the
excess, and swapping the farther trip it kept for a refused shorter one
never makes a later stop fuller, since the shorter trip ends first. A
max-heap by end stop finds the farthest rider, and counts of taken
riders per end stop keep the number on board. `O(N + K log K)`.

Pitfalls:

- trips are half-open: whoever leaves at a stop frees the seat for
  someone boarding there (test 05);
- with no people at all the answer is 0 and an empty list (test 02);
- several people may want the very same trip (tests 04, gen3).

## Optimized solutions

Process trips by increasing destination. Assign each to the seat whose last trip finished latest among the seats free at its start.

Group trips by start stop in compact arrays. A single heap key stores both destination and passenger number, so the farthest active trip can be removed when seats run out.

**Timus submissions for the optimized versions**

`1424_sorting_greedy.cpp` (G++ 13.2 x64) №11317526 · `1424_greedy_optimized.go` (Go 1.14 x64) №11317540 · `1424_greedy_optimized.java` (Java 1.8) №11317543 · `1424_greedy_optimized.py` (Python 3.12 x64) №11317528 · `1424_greedy_optimized.rs` (Rust 1.75 x64) №11317532.

**Timus submissions for the simple versions**

G++ 13.2 x64 №11322134 · Go 1.14 x64 №11322135 · Java 1.8 №11322136 · Python 3.12 x64 №11322137 · Rust 1.75 x64 №11322139.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1424_greedy.cpp](1424_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + K log K) | AC | 0.078 s | 4772 KB | 11322134 |
| [1424_greedy.go](1424_greedy.go) | Go 1.14 x64 | greedy | O(N + K log K) | AC | 0.109 s | 12396 KB | 11322135 |
| [1424_greedy.java](1424_greedy.java) | Java 1.8 | greedy | O(N + K log K) | AC | 0.218 s | 13936 KB | 11322136 |
| [1424_greedy.py](1424_greedy.py) | Python 3.12 x64 | greedy | O(N + K log K) | AC | 0.203 s | 30052 KB | 11322137 |
| [1424_greedy.rs](1424_greedy.rs) | Rust 1.75 x64 | greedy | O(N + K log K) | AC | 0.046 s | 10368 KB | 11322139 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|----------|----------|----------|------------|---------|------|--------|---|
| [1424_sorting_greedy.cpp](1424_sorting_greedy.cpp) \* | G++ 13.2 x64 | sorting, greedy | O(N + M + K log M) | AC | 0.078 s | 1032 KB | 11317526 |
| [1424_greedy_optimized.py](1424_greedy_optimized.py) | Python 3.12 x64 | greedy | O(N + K log K) | AC | 0.203 s | 3804 KB | 11317528 |
| [1424_greedy_optimized.rs](1424_greedy_optimized.rs) \* | Rust 1.75 x64 | greedy | O(N + K log K) | AC | 0.046 s | 1752 KB | 11317532 |
| [1424_greedy_optimized.go](1424_greedy_optimized.go) | Go 1.14 x64 | greedy | O(N + K log K) | AC | 0.031 s | 3916 KB | 11317540 |
| [1424_greedy_optimized.java](1424_greedy_optimized.java) | Java 1.8 | greedy | O(N + K log K) | AC | 0.14 s | 4604 KB | 11317543 |

\* The marked solutions can improve their target rankings.
