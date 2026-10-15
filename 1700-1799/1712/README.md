# 1712. Cipher Grille

[Timus 1712](https://acm.timus.ru/problem.aspx?space=1&num=1712) · difficulty 86 · implementation

Original problem by Alex Samsonov, prepared by Alexander Ipatov, from the NEERC 2009 Eastern Subregional Contest.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A 4 × 4 grille has four windows. Laid on a 4 × 4 sheet, it shows four
cells, and the next four letters of a 16-letter password are written
into them in reading order. Then the grille turns 90° clockwise, and
this repeats four times, so every cell gets exactly one letter. Given
the grille in its starting position and the filled sheet, recover the
password.

## Input

Four lines of the grille, with X for a window and . for paper, then
four lines of the sheet: Latin letters of both cases.

## Output

The password, 16 letters.

## Examples

### Example 1

Input:

```
....
X..X
.X..
...X
Pwoo
Khaa
smrs
odbk
```

Output:

```
KamkohobPassword
```

## Solution

Replay the writing. In each of the four positions, collect the letters
under the windows row by row and left to right, then turn the grille.
A clockwise turn moves the cell (r, c) to (c, 3 − r), so the turned
grille has at (r, c) what the old one had at (3 − c, r). `O(1)`.

Pitfalls:

- within one position the letters follow the reading order of the
  windows, not the order in which they were found in the previous
  position;
- the turn is clockwise: turning the other way reads the same cells in
  a different order (test 04 has all four windows in one corner);
- the input has no spaces, so reading words works in every language.

The answers match an independent accepted implementation on 300 random
valid grilles.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1712_implementation.cpp](1712_implementation.cpp) | G++ 13.2 x64 | implementation | O(1) | AC | 0.015 s | 352 KB |
| [1712_implementation.go](1712_implementation.go) | Go 1.14 x64 | implementation | O(1) | AC | 0.031 s | 1076 KB |
| [1712_implementation.java](1712_implementation.java) | Java 1.8 | implementation | O(1) | AC | 0.140 s | 1568 KB |
| [1712_implementation.py](1712_implementation.py) | Python 3.12 x64 | implementation | O(1) | AC | 0.093 s | 484 KB |
| [1712_implementation.rs](1712_implementation.rs) | Rust 1.75 x64 | implementation | O(1) | AC | 0.046 s | 228 KB |
