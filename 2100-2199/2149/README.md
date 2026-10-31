# 2149. Turning ASCII pigeons into a neat pattern

[Timus 2149](https://acm.timus.ru/problem.aspx?space=1&num=2149) · difficulty 148 · implementation

Original problem by Kirill Borozdin, from the Ural Team Programming Contest 2019.

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

Only the first line is needed: with zero-based indices, pigeon i looks
left exactly when the character at position 5i is `<`. Check four
candidate neat patterns, in two pairs of opposites. Count the pigeons
that differ from "left half looks left, right half looks right"; its
opposite pattern differs at exactly the other pigeons, so it needs n
minus that count. The same holds for "even positions look left, odd ones
right". The answer is the smallest of the four numbers, found in O(n).

In the second example only the first pigeon breaks the alternation, so
one turn is enough.

## Optimized solutions

The optimized C++ solution reads with `scanf` into one fixed `char`
buffer of 500 bytes instead of `std::cin` into a `std::string`, so the
program does without the `iostream` library; a line holds at most
5 · 100 − 1 = 499 characters, since `n ≤ 100`:
{2149_implementation_optimized.cpp}.

The optimized Java solution reads the bytes from a 4 KB buffer instead
of `Scanner` and counts the pigeons straight from the bytes of the first
line, at every fifth column, without making a `String` of it; the other
two lines are read and dropped: {2149_implementation_optimized.java}.

### Measured gains

Each optimized version has Accepted and reduces time or memory by at
least 30% against the base version in the same language. The base
sources are retained. Negative reduction means increased cost. The
asterisk concerns the rating target only.

- `2149_implementation_optimized.cpp`: time reduction +0.00%; memory
  reduction +73.47%; base: `2149_implementation.cpp`.

- `2149_implementation_optimized.java`: time reduction -12.00%; memory
  reduction +75.13%; base: `2149_implementation.java`.

## Language notes

In the rating snapshot of 2026-10-31, the following base implementations
already meet the time and memory targets. Their existing files are kept
as the base solutions; the rating target needs no additional
implementation for these languages.

- [2149_implementation.rs](2149_implementation.rs).

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2149_implementation.cpp](2149_implementation.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 392 KB | 11304075 |
| [2149_implementation.go](2149_implementation.go) | Go 1.14 x64 | implementation | O(n) | AC | 0.015 s | 1100 KB | 11295005 |
| [2149_implementation.java](2149_implementation.java) | Java 1.8 | implementation | O(n) | AC | 0.125 s | 1576 KB | 11304076 |
| [2149_implementation.py](2149_implementation.py) | Python 3.12 x64 | implementation | O(n) | AC | 0.078 s | 412 KB | 11295006 |
| [2149_implementation.rs](2149_implementation.rs) | Rust 1.75 x64 | implementation | O(n) | AC | 0.046 s | 240 KB | 11295008 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [2149_implementation_optimized.cpp](2149_implementation_optimized.cpp) | G++ 13.2 x64 | implementation | O(n) | AC | 0.015 s | 104 KB | 11304538 |
| [2149_implementation_optimized.java](2149_implementation_optimized.java) \* | Java 1.8 | implementation | O(n) | AC | 0.140 s | 392 KB | 11304539 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
