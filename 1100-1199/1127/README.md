# 1127. The tallest tower of cubes whose four sides are each one colour

[Timus 1127](https://acm.timus.ru/problem.aspx?space=1&num=1127) · difficulty 323 · bruteforce

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
- in a fixed orientation, the top and bottom colours do not matter.

The answers were checked against a separate construction of the 24
rotations as the signed permutation matrices with determinant +1 acting
on the face normals, on every test.

## Optimized solutions

Go and Rust count the three side rings obtained by choosing each pair of opposite faces as top and bottom. Since all six colours of a cube differ, a ring has a unique smallest colour. Rotate to it and choose the smaller direction to identify equivalent rings. Encode four colours in base C = 10 and count them in a flat array of 16-bit counters.

The accepted Go 1.14 x64 run takes 0.046 s versus 0.031 s for the base and uses 896 KB versus 1344 KB.

The accepted base implementations [1127_bruteforce.cpp](1127_bruteforce.cpp), [1127_bruteforce.java](1127_bruteforce.java), [1127_bruteforce.py](1127_bruteforce.py) also cover the fast set: they already meet the top-15% or top-ten ranking admission rule for both time and memory in the saved comparison snapshot. Their source files are reused without identical copies. A star marks a version that still falls short of its language’s rating target.

## Language notes

These notes describe the simple implementations.

- All languages generate the orientations by a small search over the two
  turns; C++ counts rings in an ordered map, the others in a hash map.

## Solutions

### Simple

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1127_bruteforce.cpp](1127_bruteforce.cpp) | G++ 13.2 x64 | bruteforce | O(24·N) | AC | 0.015 s | 300 KB | 11279333 |
| [1127_bruteforce.go](1127_bruteforce.go) | Go 1.14 x64 | bruteforce | O(24·N) | AC | 0.031 s | 1344 KB | 11279335 |
| [1127_bruteforce.java](1127_bruteforce.java) \* | Java 1.8 | bruteforce | O(24·N) | AC | 0.171 s | 6664 KB | 11279344 |
| [1127_bruteforce.py](1127_bruteforce.py) \* | Python 3.12 x64 | bruteforce | O(24·N) | AC | 0.093 s | 768 KB | 11279338 |
| [1127_bruteforce.rs](1127_bruteforce.rs) | Rust 1.75 x64 | bruteforce | O(24·N) | AC | 0.031 s | 440 KB | 11279345 |

### Optimized

| Solution | Language | Approach | Complexity | Verdict | Time | Memory | Submission |
|---|---|---|---|---|---|---|---|
| [1127_bruteforce_optimized.go](1127_bruteforce_optimized.go) \* | Go 1.14 x64 | bruteforce | O(N + C⁴) | AC | 0.046 s | 896 KB | 11311096 |
| [1127_bruteforce_optimized.rs](1127_bruteforce_optimized.rs) \* | Rust 1.75 x64 | bruteforce | O(N + C⁴) | AC | 0.015 s | 220 KB | 11311098 |

\* Accepted; the rating target is not yet met. This version may be optimized further.
