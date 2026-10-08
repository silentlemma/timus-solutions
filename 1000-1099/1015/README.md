# 1015. Grouping dice that are rotations of each other

[Timus 1015](https://acm.timus.ru/problem.aspx?space=1&num=1015) · difficulty 455 · hashing, implementation

Original problem from the Ural State University Internal Contest '99 #2.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` dice (`1 ≤ N ≤ 100 000`), numbered from 1 in the input order.
A die is given by the numbers on its left, right, top, front, bottom and back
faces, in this order — a permutation of `1..6`. Two dice are of the same kind
if some rotation of one gives the other (a mirror image is not a rotation).
Split the dice into kinds.

Time limit: 2 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines of six numbers: left, right, top, front, bottom, back.

## Output

The number `Q` of kinds, then `Q` lines, one per kind: the numbers of its
dice in increasing order. The lines are ordered by their first number, so
the first line starts with 1.

## Checking

The output is compared line by line; within a line, token by token.

## Examples

### Example 1

Input:

```
4
1 6 2 3 5 4
2 5 6 3 1 4
1 6 2 4 5 3
3 4 1 2 6 5
```

Output:

```
2
1 2 4
3
```

### Example 2

Input:

```
1
4 3 1 6 2 5
```

Output:

```
1
1
```

## Solution

**The 24 rotations.** Write a rotation as a permutation of the six
positions. Two quarter turns generate all of them: around the vertical axis
(left ← front ← right ← back ← left, top and bottom stay) and around the
left-right axis (top ← back ← bottom ← front ← top). Starting from the
identity and applying the two turns until nothing new appears gives exactly
24 position permutations. Only rotations are produced, never reflections, so
a die and its mirror image stay apart.

**A key for every die.** Apply all 24 rotations to a die, read each result
as a 6-digit number (base 7 is enough) and take the smallest: dice of the
same kind get the same key, dice of different kinds different keys. There
are only `720 / 24 = 30` kinds.

**Grouping.** Go through the dice in order; a hash map from key to group
creates a new group the first time a key appears and appends the die
otherwise. Groups are thus created in the order of their smallest die, and
each group's list is increasing — exactly the required output.

`O(24 · 6 · N)` time. Alternatively, precompute the key of each of the 720
possible dice once and look it up, as the Python version does.

Pitfalls:

- reflections: the six faces can be permuted in 720 ways but only 24 of them
  are rotations — a key built from the multiset of opposite pairs alone
  merges mirror images;
- up to `10^5` numbers in the output: build it in a buffer.

## Language notes

- **C++**, **Go**, **Java**, **Rust**: 24 rotations per die.
- **Python**: a table of the keys of all 720 dice, then one dictionary
  lookup per die.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1015_hashing.cpp](1015_hashing.cpp) | G++ 13.2 x64 | hashing | O(24 · 6 · N) | AC | 0.031 s | 356 KB |
| [1015_hashing.go](1015_hashing.go) | Go 1.14 x64 | hashing | O(24 · 6 · N) | AC | 0.001 s | 1280 KB |
| [1015_hashing.java](1015_hashing.java) | Java 1.8 | hashing | O(24 · 6 · N) | AC | 0.093 s | 1524 KB |
| [1015_hashing.py](1015_hashing.py) | Python 3.12 x64 | hashing | O(N) after a 720-entry table | AC | 0.093 s | 2748 KB |
| [1015_hashing.rs](1015_hashing.rs) | Rust 1.75 x64 | hashing | O(24 · 6 · N) | AC | 0.015 s | 856 KB |
