# 1388. Photo

[Timus 1388](https://acm.timus.ru/problem.aspx?space=1&num=1388) · difficulty 13892 · geometry, strings

Original problem by Andrew Rumyantsev, from the Petrozavodsk summer training camp, August 2005.

**English** · [Русский](README.ru.md) · [中文](README.zh.md) · [Español](README.es.md)

## Task

A river runs along y = 0 with a dam at the origin, and up to 100 000
trees with integer coordinates up to 20 000 in absolute value grow on
both banks. A photo is taken from the dam with a camera of almost
180 degrees: the film is a line, and the trees in front of it are
projected onto it through the origin, a tree behind another on the same
ray being hidden. Then a piece of the film showing trees of one bank
only is cut out and scaled. Find the largest number of trees on two
matching photos of the two banks, where matching means the same
arrangement of trees along the photo.

Time limit: 1 second. Memory limit: 64 MB.

## Input

Lines with the coordinates of the trees, ending with the line 0 0.

## Output

The largest number of trees on two matching photos.

## Examples

### Example 1

Input:

```
-1 1
0 1
2 1
3 1
7 2
3 -2
1 -1
0 -1
0 -5
-4 -2
-3 -1
0 0
```

Output:

```
4
```

### Example 2

Input:

```
0 1
1 1
2 1
-3 -1
-2 -2
-1 -3
0 0
```

Output:

```
3
```

## Solution

A tree is seen along the line through the origin, so only the number
c = x / y matters, and trees with the same c hide each other. For a film
facing straight away from the river the position of a tree on the
photo is c on both banks, with the photo's right side on the right. A
turned film moves the positions by a projective map of c that keeps the
cyclic order, and scaling is an affine map with a positive factor. The
direction along the river, c = ∞, is never inside a piece of film.

So a photo is a run of consecutive values in the sorted list of
distinct c on one bank, and two runs match exactly when an
orientation-preserving projective map takes the first value of one to
the first of the other, the second to the second, and so on. Any three
points can be sent to any three in the same order, so runs of up to
three trees always match. After that each point is fixed by the three
before it, so the cross-ratio of every four consecutive points must
agree:

(c₃ − c₁)(c₄ − c₂) / ((c₃ − c₂)(c₄ − c₁)).

With c = p / q the denominators cancel, and each factor is a 2 × 2
determinant of at most 8·10⁸, so the cross-ratio is an exact reduced
fraction of 64-bit integers. Number the fractions of both banks, and
the answer is 3 plus the longest common substring of the two sequences,
found with a suffix automaton of one of them; with fewer than four
directions on a bank it is the smaller count, at most 3.
`O(n log n)`.

Pitfalls:

- a mirror image does not count: in example 1 a reversed match would
  give 5 trees, and the answer is 4 (test 08 is the mirror case);
- a tree behind another on the same ray is not on the photo (test 07);
- a projective map can send a direction of a run to the river, which
  splits the image in two (generated test 3);
- runs of up to three trees always match, and a bank without trees
  gives 0 (tests 02 to 06).

The answers were compared on 500 random small sets, half of them with
one bank holding a projective image of the other, against a search that
builds the map from the first three points of every pair of runs and
extends the match while it holds.

## Solutions

| Solution | Language | Approach | Complexity | Verdict | Time | Memory |
|----------|----------|----------|------------|---------|------|--------|
| [1388_strings.cpp](1388_strings.cpp) | G++ 13.2 x64 | strings | O(n log n) | AC | 0.078 s | 5700 KB |
| [1388_strings.go](1388_strings.go) | Go 1.14 x64 | strings | O(n log n) | AC | 0.062 s | 11080 KB |
| [1388_strings.java](1388_strings.java) | Java 1.8 | strings | O(n log n) | AC | 0.250 s | 17148 KB |
| [1388_strings.py](1388_strings.py) | Python 3.12 x64 | strings | O(n log n) | AC | 0.343 s | 27468 KB |
| [1388_strings.rs](1388_strings.rs) | Rust 1.75 x64 | strings | O(n log n) | AC | 0.031 s | 9440 KB |
