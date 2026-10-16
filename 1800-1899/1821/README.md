# 1821. Biathlon

[Timus 1821](https://acm.timus.ru/problem.aspx?space=1&num=1821) · difficulty 178 · sorting

Original problem by Alexander Ipatov and Alexey Samsonov, from the XII USU Open Personal Contest, March 19, 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

In an individual-start race the skiers start one by one, 30 seconds
apart. A board shows the skier with the best time among those who have
already finished. Given the skiers in start order with their race
times, list everyone who appeared on the board.

## Input

n (1 ≤ n ≤ 100), then n lines: a surname (up to 20 English letters,
the first one capital) and a time "mm:ss.d". No two skiers finish at
the same moment and no two have equal times.

## Output

The number of skiers who led the race when they finished, then their
surnames in lexicographic order, one per line.

## Examples

### Example 1

Input:

```
6
Zaitseva 21:38.2
Hauswald 21:21.0
Boulygina 22:04.4
Henkel 22:06.1
Wilhelm 21:11.1
Jonsson 22:05.8
```

Output:

```
3
Hauswald
Wilhelm
Zaitseva
```

## Solution

Work in tenths of a second. Skier i (from 0) starts at 300·i and
finishes at 300·i plus the race time. Sort the skiers by finishing
moment and replay: a skier goes on the board when the race time beats
every time finished so far. Sort the collected surnames and print
them. `O(n log n)`.

In the example the finishes come in the order Zaitseva (12982),
Hauswald (13110), Boulygina (13844), Wilhelm (13911), Henkel (14161),
Jonsson (14758) in tenths; the best time drops at Zaitseva, Hauswald
and Wilhelm.

Pitfalls:

- the order of finishing is not the order of starting, so sort by the
  finishing moment, not by the race time;
- the board is about the best time so far, not the earliest finisher;
- the answer is sorted by surname, not in the order the board changed.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1821_sorting.cpp](1821_sorting.cpp) | G++ 13.2 x64 | sorting | O(n log n) | AC | 0.015 s | 452 KB |
| [1821_sorting.go](1821_sorting.go) | Go 1.14 x64 | sorting | O(n log n) | AC | 0.031 s | 1136 KB |
| [1821_sorting.java](1821_sorting.java) | Java 1.8 | sorting | O(n log n) | AC | 0.156 s | 3936 KB |
| [1821_sorting.py](1821_sorting.py) | Python 3.12 x64 | sorting | O(n log n) | AC | 0.093 s | 460 KB |
| [1821_sorting.rs](1821_sorting.rs) | Rust 1.75 x64 | sorting | O(n log n) | AC | 0.031 s | 228 KB |
