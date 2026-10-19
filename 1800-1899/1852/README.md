# 1852. Cube in a Cube in a Cube

[Timus 1852](https://acm.timus.ru/problem.aspx?space=1&num=1852) · difficulty 2437 · simulation

Original problem by Grigoriy Nazarov, from the Ural SU Team.GOV Contest at the Petrozavodsk summer session, August 2011.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

Vadik made a sequence of face turns on a Rubik's cube with a pattern.
Repeating the same sequence eventually restores that pattern. How many
more times must the sequence be applied to get the original pattern
back?

## Input

One line of at most 10⁵ letters U, D, L, R, F and B, for the top,
bottom, left, right, front and back faces: a lowercase letter turns that
face 90° clockwise, an uppercase letter 90° counter-clockwise.

## Output

The number of further repetitions needed.

## Examples

### Example 1

Input:

```
Ud
```

Output:

```
3
```

### Example 2

Input:

```
RRRR
```

Output:

```
0
```

## Solution

The sequence moves the 54 stickers by a fixed permutation, and
repeating it k times restores the cube exactly when k is a multiple of
the order of that permutation, the least common multiple of its cycle
lengths. The answer is the order minus 1, since the sequence has been
applied once already.

Model a sticker as the position of its cubie, with coordinates in
{−1, 0, 1}, together with the outward normal of its face. Turning a face
with outward normal a moves the stickers whose position p has p·a = 1:
both p and the normal turn a quarter about a. Seen from outside the face,
counter-clockwise is the turn v → a × v + a(a·v) and clockwise the same
with −a × v. Each of the twelve letters thus becomes a table of where
every sticker goes, and the sequence is folded into one permutation
with 54 lookups per letter (in Python, one `bytes.translate` per
letter). `O(54·|s|)`.

In the first example U turned counter-clockwise from above and d turned
clockwise from below spin both outer layers the same way around the
vertical axis, so the pattern returns after four sequences: three more.
In the second example four quarter turns of R already restore the cube.

Pitfalls:

- clockwise is seen from outside each face, so the bottom face turns
  the opposite way to the top for the same letter case;
- the sequence was applied once already, hence the minus one;
- the order stays small (at most 1260 on a cube), but the cycle
  lengths must be combined by lcm, not multiplied.

The answers agree with an independent accepted implementation on three
hundred random sequences and on the known orders, such as 105 for two
clockwise turns of adjacent faces and 6 for a turn, another and both
undone.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1852_simulation.cpp](1852_simulation.cpp) | G++ 13.2 x64 | simulation | O(54 n) | AC | 0.031 s | 524 KB |
| [1852_simulation.go](1852_simulation.go) | Go 1.14 x64 | simulation | O(54 n) | AC | 0.031 s | 1872 KB |
| [1852_simulation.java](1852_simulation.java) | Java 1.8 | simulation | O(54 n) | AC | 0.109 s | 1764 KB |
| [1852_simulation.py](1852_simulation.py) | Python 3.12 x64 | simulation | O(54 n) | AC | 0.109 s | 936 KB |
| [1852_simulation.rs](1852_simulation.rs) | Rust 1.75 x64 | simulation | O(54 n) | AC | 0.015 s | 676 KB |
