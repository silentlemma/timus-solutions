# 1127. The tallest tower of cubes whose four sides are each one colour

[Timus 1127](https://acm.timus.ru/problem.aspx?space=1&num=1127) · difficulty 322 · bruteforce

Original problem by Ekaterina Vasilyeva, from the Sixth Ural State University Collegiate Programming Contest, October 21, 2001.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

There are `N` cubes (`1 < N ≤ 1000`); each face of a cube has a colour
(one of 10 letters), and the six faces of a cube all differ. The faces
are given as front, right, left, back, top, bottom. Stack as many cubes
as possible, each turned any way, so that each of the four side faces of
the tower is a single colour. Print the height.

Time limit: 0.4 seconds. Memory limit: 64 MB.

## Input

`N`, then `N` lines of six colour letters.

## Output

The greatest height.

## Checking

The output is compared token by token; extra whitespace does not matter.

## Examples

### Example 1

Input:

```
4
GYVABW
AOCGYV
CABVGO
OVYWGA
```

Output:

```
3
```

## Solution

A tower is determined by the ring of colours on its sides: front, right,
back, left. A cube fits a ring if one of its 24 orientations shows
exactly that ring. Since its six colours differ, a cube shows each ring
in at most one orientation, so counting, for every ring, the cubes that
can show it gives the height of the tallest tower with that ring. The 24
orientations are generated once from two quarter turns, one about the
vertical axis and one about the left-right axis, as permutations of the
six face positions. `O(24·N)`.

Pitfalls:

- the turns must be rotations, not reflections: a quarter turn moves the
  front to the right, the right to the back, and so on, keeping the
  handedness;
- a mirror image of a cube still fits: turned upside down about the
  front-back axis it shows the same ring of sides, only top and bottom
  swapped, and those do not matter;
- the colours of the top and bottom faces never matter.

The answers were checked against a separate construction of the 24
rotations as the signed permutation matrices with determinant +1 acting
on the face normals, on every test.

## Language notes

- All languages generate the orientations by a small search over the two
  turns and count rings in a hash map.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1127_bruteforce.cpp](1127_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(24·N) | AC | 0.015 s | 300 KB |
| [1127_bruteforce.go](1127_bruteforce.go) | Go 1.14 x64 | bruteforce | O(24·N) | AC | 0.031 s | 1344 KB |
| [1127_bruteforce.java](1127_bruteforce.java) | Java 1.8 | bruteforce | O(24·N) | AC | 0.171 s | 6664 KB |
| [1127_bruteforce.py](1127_bruteforce.py) | Python 3.12 x64 | bruteforce | O(24·N) | AC | 0.093 s | 768 KB |
| [1127_bruteforce.rs](1127_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(24·N) | AC | 0.031 s | 440 KB |
