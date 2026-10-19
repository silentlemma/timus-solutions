# 1826. Minefield

[Timus 1826](https://acm.timus.ru/problem.aspx?space=1&num=1826) · difficulty 310 · greedy

Original problem by Dmitry Teryaev, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A squad of n crosses a minefield with a single mine detector: two cross
together, then one brings the detector back, and so on. Each soldier
has a crossing time, and a pair moves at the speed of the slower one.
Find the least total time for the whole squad to cross.

## Input

n (2 ≤ n ≤ 100), then n crossing times, positive integers up to 600.

## Output

The least total time.

## Examples

### Example 1

Input:

```
4
1
10
5
2
```

Output:

```
17
```

## Solution

This is the bridge-and-torch puzzle. Sort the times a ≤ b ≤ … ≤ y ≤ z.
While more than three soldiers wait, send the two slowest across in
one of two ways and keep the cheaper:

- the fastest escorts each of them: z + a + y + a = 2a + y + z;
- the two fastest cross, a returns, the two slowest cross together, b
  returns: b + a + z + b = a + 2b + z.

Either way the two fastest are back at the start and two fewer remain.
Three soldiers take a + b + c (a escorts both), two take the slower
time. An exchange argument shows that some optimal plan always moves
the two slowest this way. `O(n log n)`.

In the example (1, 2, 5, 10) pairing costs 1 + 2·2 + 10 = 15 against
2 + 5 + 10 = 17 for escorting, and the last two take 2: 17.

Pitfalls:

- always escorting with the fastest is not optimal: 1, 2, 5, 10 would
  take 19;
- always pairing the slow ones is not optimal either when the second
  fastest is slow;
- the choice is made again in every round.

The answers agree with a Dijkstra search over all states for squads
of up to 7 and with an independent accepted implementation on random
squads.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1826_greedy.cpp](1826_greedy.cpp) | G++ 13.2 x64 | greedy | O(n log n) | AC | 0.015 s | 192 KB |
| [1826_greedy.go](1826_greedy.go) | Go 1.14 x64 | greedy | O(n log n) | AC | 0.031 s | 1096 KB |
| [1826_greedy.java](1826_greedy.java) | Java 1.8 | greedy | O(n log n) | AC | 0.109 s | 1764 KB |
| [1826_greedy.py](1826_greedy.py) | Python 3.12 x64 | greedy | O(n log n) | AC | 0.078 s | 464 KB |
| [1826_greedy.rs](1826_greedy.rs) | Rust 1.75 x64 | greedy | O(n log n) | AC | 0.031 s | 240 KB |
