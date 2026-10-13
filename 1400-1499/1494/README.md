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

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1494_simulation.cpp](1494_simulation.cpp) | G++ 13.2 x64 | simulation | O(N) | AC | 0.093 s | 1540 KB |
| [1494_simulation.go](1494_simulation.go) | Go 1.14 x64 | simulation | O(N) | AC | 0.031 s | 8204 KB |
| [1494_simulation.java](1494_simulation.java) | Java 1.8 | simulation | O(N) | AC | 0.109 s | 1336 KB |
| [1494_simulation.py](1494_simulation.py) | Python 3.12 x64 | simulation | O(N) | AC | 0.140 s | 15568 KB |
| [1494_simulation.rs](1494_simulation.rs) | Rust 1.75 x64 | simulation | O(N) | AC | 0.031 s | 2704 KB |
