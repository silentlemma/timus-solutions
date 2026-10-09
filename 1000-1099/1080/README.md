# 1080. Colouring a map with two colours

[Timus 1080](https://acm.timus.ru/problem.aspx?space=1&num=1080) · difficulty 190 · bfs, graphs

Original problem by Emil Kelevedzhiev, from the Informatics Tournament of the Winter Mathematical Festival, Varna 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A map has `N` countries (`0 < N < 99`); every country can be reached
from every other one by crossing borders. Colour the countries red (0)
and blue (1) so that neighbours always differ, with country 1 red. Print
the colours as one string of digits, or `-1` if it cannot be done.

Time limit: 1 second. Memory limit: 64 MB.

## Input

`N`, then `N` lines: line `i` lists the neighbours of country `i` with
larger numbers and ends with 0.

## Output

The string of colours, or `-1`.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
3
2 0
3 0
0
```

Output:

```
010
```

## Solution

A map can be coloured this way exactly when its graph of borders is
bipartite. Start a breadth-first search from country 1 with colour 0 and
give every newly reached country the colour opposite to the one it was
reached from. If a border ever joins two countries of the same colour,
there is an odd cycle and the answer is `-1`. Since the map is connected,
the colour of country 1 fixes all others, so the answer is unique.
`O(N + M)`.

Pitfalls:

- each line lists only the neighbours with larger numbers, so every
  border must be added in both directions;
- a country with no larger neighbours has a line with just 0;
- the digits are printed without separators.

The answers were checked with a union-find that keeps the parity of the
path to the root, a method that does not walk the map at all.

## Language notes

- All languages read the neighbours token by token until the 0 that
  closes each line.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1080_bfs.cpp](1080_bfs.cpp) | G++ 13.2 x64 | bfs | O(N + M) | AC | 0.001 s | 284 KB |
| [1080_bfs.go](1080_bfs.go) | Go 1.14 x64 | bfs | O(N + M) | AC | 0.031 s | 1364 KB |
| [1080_bfs.java](1080_bfs.java) | Java 1.8 | bfs | O(N + M) | AC | 0.125 s | 5556 KB |
| [1080_bfs.py](1080_bfs.py) | Python 3.12 x64 | bfs | O(N + M) | AC | 0.078 s | 816 KB |
| [1080_bfs.rs](1080_bfs.rs) | Rust 1.75 x64 | bfs | O(N + M) | AC | 0.031 s | 296 KB |
