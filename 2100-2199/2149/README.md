# 2149. Turning ASCII pigeons into a neat pattern

[Timus 2149](https://acm.timus.ru/problem.aspx?space=1&num=2149) · difficulty 148 · implementation

Original problem by Kirill Borozdin, from the Ural School Programming Contest 2019.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

n pigeons sit in a row, n even, each looking left or right, and they are
drawn as ASCII art. The row is neat when the left half looks one way and
the right half the other, or when the pigeons at even positions look one
way and those at odd positions the other. Find the fewest pigeons to turn
around. The limits are 0.5 seconds and 256 MB.

## Input

n, 2 ≤ n ≤ 100, then three lines of 5n − 1 characters with the pigeons:
`<@..`, `.OO=`, `./\.` for a pigeon looking left and `..@>`, `=OO.`,
`./\.` for one looking right, separated by columns of dots.

## Output

The fewest turns.

## Examples

### Example 1

Input:

```
8
..@>.<@...<@.....@>...@>...@>.<@...<@..
=OO...OO=..OO=.=OO..=OO..=OO...OO=..OO=
./\.../\.../\.../\.../\.../\.../\.../\.
```

Output:

```
4
```

### Example 2

Input:

```
4
..@>...@>.<@.....@>
=OO..=OO...OO=.=OO.
./\.../\.../\.../\.
```

Output:

```
1
```

## Solution

Only the first line is needed: pigeon i looks left exactly when the
character at position 5i is `<`. There are four neat patterns, in two
pairs of opposites. Count the pigeons that differ from "left half looks
left, right half looks right"; its opposite pattern differs at exactly
the other pigeons, so it needs n minus that count. The same holds for
"even positions look left, odd ones right". The answer is the smallest
of the four numbers, found in O(n).

In the second example only the first pigeon breaks the alternation, so
one turn is enough.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [2149_implementation.cpp](2149_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.031 s | 400 KB |
| [2149_implementation.go](2149_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1100 KB |
| [2149_implementation.java](2149_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1612 KB |
| [2149_implementation.py](2149_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 412 KB |
| [2149_implementation.rs](2149_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 240 KB |
