# 1424. Minibus

[Timus 1424](https://acm.timus.ru/problem.aspx?space=1&num=1424) · difficulty 708 · greedy

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
excess, and swapping a refused short trip for the farther one it kept
never makes a later stop fuller, since the shorter trip ends first. A
max-heap by end stop finds the farthest rider, and counts of taken
riders per end stop keep the number on board. `O(N + K log K)`.

Pitfalls:

- trips are half-open: whoever leaves at a stop frees the seat for
  someone boarding there (test 05);
- with no people at all the answer is 0 and an empty list (test 02);
- several people may want the very same trip (tests 04, gen3).

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1424_greedy.cpp](1424_greedy.cpp) | G++ 13.2 x64 | greedy | O(N + K log K) | AC | 0.093 s | 4752 KB |
| [1424_greedy.go](1424_greedy.go) | Go 1.14 x64 | greedy | O(N + K log K) | AC | 0.109 s | 12376 KB |
| [1424_greedy.java](1424_greedy.java) | Java 1.8 | greedy | O(N + K log K) | AC | 0.187 s | 13932 KB |
| [1424_greedy.py](1424_greedy.py) | Python 3.12 x64 | greedy | O(N + K log K) | AC | 0.218 s | 30352 KB |
| [1424_greedy.rs](1424_greedy.rs) | Rust 1.75 x64 | greedy | O(N + K log K) | AC | 0.031 s | 10376 KB |
